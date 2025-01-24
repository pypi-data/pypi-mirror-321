"""
Channels Functions
"""

def get_channels(self, organizationId=None, workspaceId=None, channelId=None):
    """Shows all channels available to the user. Can filter by organizationId, workspaceId, or channelId.
    
    Parameters
    ----------
    organizationId : str
        Filter channel list on what's available to the organization.
    workspaceId : str    
        Filter channel list on what's available to the workspace.
    channelId: str
        Filter channel list on the specific channelId.
    
    Returns
    -------
    list[dict]
        List of channels associated with user, workspace, organization or channelId.
    """
    if self.check_logout(): return
    if organizationId is None and self.user is None: organizationId = self.organization
    channels = self.ana_api.getChannels(organizationId=organizationId, workspaceId=workspaceId, channelId=channelId)
    if channels:
        for channel in channels:
            self.channels[channel['channelId']] = channel['name']
    return channels
       
                

def get_managed_channels(self, channelId=None, organizationId=None):
    """Get information for all managed channels that you own within your organization.
    
    Parameters
    ----------
    channelId : str
        Channel Id to filter.
    organizationId : str
        Organization ID. Defaults to current if not specified.
   
    Returns
    -------
    list[dict]
        channel data
    """
    if self.check_logout(): return
    if organizationId is None: organizationId = self.organization
    return self.ana_api.getManagedChannels(organizationId=organizationId, channelId=channelId)


def create_managed_channel(self, name, description=None, organizationId=None, volumes=[], instance='p2.xlarge', timeout=120, interfaceVersion=1):
    """Create a managed channel for your organization.
    
    Parameters
    ----------
    name : str
        Channel name.
    description : str
        Description of the channel
    organizationId : str
        Organization ID. Defaults to current if not specified.
    volumes : list[str]
        List of the data volume names to associate with this channel.
    instance: str
        AWS Instance type.
    timeout: int
        Maximum runtime of a channel run.
    interface: int
        The ana interface version number.
   
    Returns
    -------
    list[dict]
        channel data
    """
    if self.check_logout(): return
    if organizationId is None: organizationId = self.organization
    result = self.ana_api.createManagedChannel(organizationId=organizationId, name=name, description=description, volumes=volumes, instance=instance, timeout=timeout, interfaceVersion=interfaceVersion)
    self.get_channels()
    return result

def edit_managed_channel(self, channelId, name=None, description=None, volumes=None, instance=None, timeout=None, status=None, interfaceVersion=None, preview=None):
    """Edit a managed channel for your organization.
    
    Parameters
    ----------
    channelId : str
        ChannelId ID of the channel to edit.
    name : name
        The new name to give the channel.
    description : str
        Description of the channel
    volumes : list[str]
        Data volumes for the channel.
    instance: str
        Instance type to run the channel on.
    timeout: int
        Maximum runtime for the channel run.
    status: str
        The status of the channel.
    interface: int
        The ana interface version number.
    preview: bool
        Enable or disable the preview for the channel.
    
    Returns
    -------
    bool
        If true, the channel was successfully edited.
    """
    if self.check_logout(): return
    if channelId is None: raise Exception('ChannelId must be specified.')
    result = self.ana_api.editManagedChannel(channelId=channelId, name=name, description=description, volumes=volumes, instance=instance, timeout=timeout, status=status, interfaceVersion=interfaceVersion, preview=preview)
    self.get_channels()
    return result

def delete_managed_channel(self, channelId):
    """Delete a managed channel of your organization.
    
    Parameters
    ----------
    channelId : str
        Id of channel to delete.
    
    Returns
    -------
    str
        Status
    """
    if self.check_logout(): return
    if channelId is None: raise Exception('ChannelId must be specified.')
    result = self.ana_api.deleteManagedChannel(channelId=channelId)
    self.get_channels()
    return result


def build_managed_channel(self, channelfile, ignore=['data/', 'output/']):
    """Build the Docker image of a channel.
    
    Parameters
    ----------
    channelfile : str
        The channel file for the channel to build.

    Returns
    -------
    bool
        A boolean that indicates if the channel Docker image was successfully built.
    """
    import os
    import docker
    import time
    from anatools.lib.print import print_color

    # make sure we can connect to docker
    try: dockerclient = docker.APIClient(base_url='unix://var/run/docker.sock')
    except: raise Exception('Cannot connect to Docker host.')

    # build dockerfile
    print('Building Channel Image...', end='', flush=True)    
    if not os.path.isfile(channelfile): raise Exception(f'No channel file {channelfile} found.')
    channeldir, channelfile = os.path.split(channelfile)
    if channeldir == "": channeldir = "./"   
    if not os.path.isdir(os.path.join(channeldir, '.devcontainer')): raise Exception(f'No .devcontainer directory found in channel directory.')
    if not os.path.isfile(os.path.join(channeldir, '.devcontainer/Dockerfile')): raise Exception(f'Issue detected with .devcontainer directory, build requires Dockerfile.')

    # check if dockerfile already exists, if so rename it
    if os.path.isfile(os.path.join(channeldir, 'Dockerfile')):
        os.rename(os.path.join(channeldir, 'Dockerfile'), os.path.join(channeldir, 'Dockerfile.old'))

    # create new Dockerfile
    with open(os.path.join(channeldir, 'Dockerfile'), 'w+') as buildfile:
        with open(os.path.join(channeldir,'.devcontainer/Dockerfile')) as dockerfile: buildfile.write(dockerfile.read())
        deploycommands = """
# Commands used for deployment
RUN sudo mkdir /ana /data
COPY . /ana/
WORKDIR /ana
RUN sudo /home/$USERNAME/miniconda3/bin/pip install -r /ana/requirements.txt > /dev/null 2>&1 && \\
    sudo /home/$USERNAME/miniconda3/envs/anatools/bin/pip install -r /ana/requirements.txt > /dev/null 2>&1
ENTRYPOINT []
CMD ["bash"]
USER root"""
        buildfile.write(deploycommands)

    # build the dockerignore for docker context, ignore specified files and directories
    if os.path.isfile(os.path.join(channeldir, '.dockerignore')):
        os.rename(os.path.join(channeldir, '.dockerignore'), os.path.join(channeldir, '.dockerignore.old'))
    with open(os.path.join(channeldir, '.dockerignore'), 'w+') as ignorefile:
        for i in ignore: ignorefile.write(f'{i}\n')

    # call the docker build command
    status = False
    try:
        t0 = time.time()
        streamer = dockerclient.build(path=channeldir, tag=channelfile.split('.')[0], decode=True)
        if self.verbose != 'debug': logfile = open(os.path.join(channeldir, 'dockerbuild.log'), 'w')
        while True:
            try:
                output = streamer.__next__()
                if self.verbose == 'debug':
                    if 'stream' in output: print(output['stream'].strip('\n'), flush=True)
                    if 'error' in output: print_color(f'{output["error"]}', 'ff0000')
                else: 
                    try:
                        if 'stream' in output: logfile.write(output['stream'].strip('\n'))
                        if 'error' in output: logfile.write(f'{output["error"]}', 'ff0000')
                    except: pass
                    print(f'\rBuilding Channel Image...  [{time.time()-t0:.3f}s]', end='', flush=True)
            except StopIteration:
                time.sleep(5)
                print(f"\rBuilding Channel Image...done.  [{time.time()-t0:.3f}s]", flush=True)
                try:
                    dockerclient = docker.from_env()
                    dockerclient.images.get(channelfile.split('.')[0])
                    status = True
                    if self.verbose != 'debug': logfile.close()
                except:
                    print('Failed to build Docker image, see dockerbuild.log for more information.')
                    break

                break
    except Exception as e:
        print(f'Error encountered while building Docker image: {e}')
        pass

    # cleanup
    os.remove(os.path.join(channeldir, '.dockerignore'))
    os.remove(os.path.join(channeldir, 'Dockerfile'))
    if os.path.isfile(os.path.join(channeldir, '.dockerignore.old')):
        os.rename(os.path.join(channeldir, '.dockerignore.old'), os.path.join(channeldir, '.dockerignore'))
    if os.path.isfile(os.path.join(channeldir, 'Dockerfile.old')):
        os.rename(os.path.join(channeldir, 'Dockerfile.old'), os.path.join(channeldir, 'Dockerfile'))
    
    return status


def __check_docker_image_size(image):
    """ Helper function that computes size of docker image. 
    
    Parameters
    ----------
    image : object
        Docker Image Object
    
    Returns
    -------
    bool
        True if size is less than 7.5GB. False if it's bigger.
    """
    from anatools.lib.print import  print_color
    # limit size to 7.5GB
    size_of_image = 0

    size = image.attrs.get('Size')
    virtual_size = image.attrs.get('VirtualSize')

    if size is None and virtual_size is None:
        print_color('WARNING: Docker Image size cannot be determined. Skipping size check.', 'ff0000')
        return True
    elif virtual_size is None:
        size_of_image = size
    elif size is None:
        size_of_image = virtual_size
    else:
        size_of_image = max(size, virtual_size)

    size_in_gb = size_of_image / (1024 ** 3)
    print_color(f'Docker image size: {size_in_gb:.2f}', 'ff0000')
    return


def deploy_managed_channel(self, channelId=None, channelfile=None, image=None):
    """Deploy the Docker image of a channel.
    
    Parameters
    ----------
    channelId : str
        Channel ID that you are pushing the image to. If the channelId isn't specified, it will use the image name to lookup the channelId.
    channelfile: str
        Name of the channel file to look for. 
    image: str
        The Docker image name. This should match the channel name when running ana. If image is not specified, it will use the channel name for the channelId.
    
    Returns
    -------
    str
        deploymentId for current round of deployment or an error message if something went wrong
    """
    import os
    import docker
    import time
    import sys
    import base64
    if self.check_logout(): return
    if channelId is None and image is None: print('The channelId or local image must be specified.'); return
    self.get_channels()

    # make sure we can connect to docker
    try: dockerclient = docker.from_env()
    except: raise Exception('Cannot connect to Docker host.')

    if channelfile:
        if self.build_managed_channel(channelfile):
            image = os.path.split(channelfile)[1].split('.')[0]
        else: return False
    
    # check if channel image is in Docker
    if image and channelId:
        channel = image
        if channelId not in self.channels: 
            print(f'User does not have permissions to deploy to a channel with ID \"{channelId}\" on the Rendered.ai Platform.'); return
    elif image:   
        channel = image
        channels = self.get_managed_channels()
        filteredchannels = [channel for channel in channels if channel['name'] == image]
        if len(filteredchannels) == 1: channelId = filteredchannels[0]['channelId']
        elif len(filteredchannels) == 0: print(f'User does not have permissions to deploy to a channel named \"{image}\" on the Rendered.ai Platform.'); return
        else: print('User has access to multiple channels with name \"{image}\" on the Rendered.ai Platform, please specify channelId.'); return
    else:
        if channelId in self.channels: channel = self.channels[channelId]
        else: print(f'User does not have permissions to deploy to a channel with ID \"{channelId}\" on the Rendered.ai Platform.'); return
    try: 
        channelimage = dockerclient.images.get(channel)
        if self.verbose == 'debug': __check_docker_image_size(channelimage)
    except docker.errors.ImageNotFound: print(f'Could not find Docker image with name \"{channel}\".'); return
    except: raise Exception('Error connecting to Docker.')

    # get repository info
    print(f"Pushing Channel Image...", end='', flush=True)
    dockerinfo = self.ana_api.deployManagedChannel(channelId, image)
    deploymentId = dockerinfo['deploymentId']
    reponame = dockerinfo['ecrEndpoint']
    encodedpass = dockerinfo['ecrPassword']
    if encodedpass:
        encodedbytes = encodedpass.encode('ascii')
        decodedbytes = base64.b64decode(encodedbytes)
        decodedpass = decodedbytes.decode('ascii').split(':')[-1]
    else: print('Failed to retrieve credentials from Rendered.ai platform.'); sys.exit(1)

    # tag and push image
    channelimage.tag(reponame)
    largest = 0
    t0 = time.time()
    for line in dockerclient.images.push(reponame, auth_config={'username':'AWS', 'password':decodedpass}, stream=True, decode=True):
        if 'status' and 'progressDetail' in line:
            if 'current' and 'total' in line['progressDetail']:
                progressDetail = line['progressDetail']
                if progressDetail['total'] >= largest:
                    largest = progressDetail['total']
                    print(f"\rPushing Channel Image...  [{time.time()-t0:.3f}s, {min(100,round((progressDetail['current']/progressDetail['total']) * 100))}%]", end='', flush=True)
    print(f"\rPushing Channel Image...done.  [{time.time()-t0:.3f}s]     ", flush=True)
    
    # cleanup docker and update channels
    dockerclient.images.remove(reponame)
    dockerclient.images.remove(channel)
    dockerclient.close()
    if self.check_logout(): return
    self.get_channels()
    return deploymentId


def get_deployment_status(self, deploymentId, stream=False):
    """Retrieves status for a channel's deployment.
    
    Parameters
    ----------
    deploymentId: str
        The deploymentId to retrieve status for
    stream: bool
        Flag to print information to the terminal so the user can avoid constant polling to retrieve status.

    Returns
    -------
    list[dict]
        Deployment status. 
    """
    import time
    if self.check_logout(): return
    if deploymentId is None: raise Exception('DeploymentId must be specified.')
    if stream:
        data = self.ana_api.getChannelDeployment(deploymentId=deploymentId)
        print(f"\r\tStep {data['status']['step']} - {data['status']['message']}", end='', flush=True)
        while (data['status']['state'] not in ['Channel Deployment Complete','Channel Deployment Failed']):
            time.sleep(10)
            print(f"\r\tStep {data['status']['step']} - {data['status']['message']}", end='', flush=True)
            if self.check_logout(): return
            data = self.ana_api.getChannelDeployment(deploymentId=deploymentId)
        print(f"\r\tStep {data['status']['step']} - {data['status']['message']}", flush=True)
    else: return self.ana_api.getChannelDeployment(deploymentId=deploymentId)

    
def get_channel_documentation(self, channelId, localDir=None):
    """Downloads a markdown file for channel documentation.
    
    Parameters
    ----------
    channelID: str
        The channelId of the channel
    localDir: str
        The location to download the file to.

    Returns
    -------
    list[str]
        The list of filenames downloaded.
    """
    import os
    import requests

    if channelId not in self.channels: raise ValueError(f'Could not find channel with ID "{channelId}"')
    if localDir is None: localDir = './'
    elif not os.path.isdir(localDir): raise ValueError(f'Could not find directory {localDir}')

    docfile = self.ana_api.getChannelDocumentation(channelId=channelId)[0]
    downloadresponse = requests.get(url=docfile['markdown'])
    filename = os.path.join(localDir, channelId+"."+docfile['markdown'].split('?')[0].split('/')[-1].split('.')[1])
    with open(filename, 'wb') as outfile:
        outfile.write(downloadresponse.content)
    return filename


def upload_channel_documentation(self, channelId, mdfile):
    """Uploads a markdown file for channel documentation.
    
    Parameters
    ----------
    channelID: str
        The channelId of the channel
    mdfile: str
        The filepath of the markdown file used for channel documentation.

    Returns
    -------
    bool
        Success/Failure of channel documenation upload.
    """
    import os
    import requests

    if channelId not in self.channels: raise ValueError(f'Could not find channel with ID "{channelId}"')
    if not os.path.isfile(mdfile): raise ValueError(f'Could not find file {mdfile}')
    if os.path.splitext(mdfile)[1] != '.md': raise ValueError('The channel documentation file must be in markdown format with .md extension.') 
    fileinfo = self.ana_api.uploadChannelDocumentation(channelId=channelId, keys=[os.path.basename(mdfile)])[0]
    with open(mdfile, 'rb') as filebytes:
        files = {'file': filebytes}
        data = {
            "key":                  fileinfo['fields']['key'],
            "bucket":               fileinfo['fields']['bucket'],
            "X-Amz-Algorithm":      fileinfo['fields']['algorithm'],
            "X-Amz-Credential":     fileinfo['fields']['credential'],
            "X-Amz-Date":           fileinfo['fields']['date'],
            "X-Amz-Security-Token": fileinfo['fields']['token'],
            "Policy":               fileinfo['fields']['policy'],
            "X-Amz-Signature":      fileinfo['fields']['signature'],
        }
        response = requests.post(fileinfo['url'], data=data, files=files)
        if response.status_code != 204: 
            print(response.status_code)
            raise Exception('Failed to upload channel documentation file.')
    return True
