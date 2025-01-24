"""
Datasets API calls.
"""

def getDatasets(self, workspaceId, datasetId=None, name=None, email=None):
    response = self.session.post(
        url = self.url, 
        headers = self.headers, 
        json = {
            "operationName": "getDatasets",
            "variables": {
                "workspaceId": workspaceId,
                "datasetId": datasetId,
                "name": name,
                "email": email
            },
            "query": """query 
                getDatasets($workspaceId: String!, $datasetId: String, $name: String, $email: String) {
                    getDatasets(workspaceId: $workspaceId, datasetId: $datasetId, name: $name, member: $email) {
                        datasetId: datasetid
                        name
                        channel
                        channelId
                        graphId: source
                        interpretations: scenarios
                        user
                        type
                        status
                        priority
                        seed
                        count
                        files
                        size
                        description
                    }
                }"""})
    return self.errorhandler(response, "getDatasets")


def getDatasetJobs(self, workspaceId, datasetId=None):
    response = self.session.post(
        url = self.url, 
        headers = self.headers, 
        json = {
            "operationName": "getDatasetJobs",
            "variables": {
                "workspaceId": workspaceId,
                "datasetId": datasetId
            },
            "query": """query 
                getDatasetJobs($workspaceId: String!, $datasetId: String) {
                    getDatasetJobs(workspaceId: $workspaceId, datasetId: $datasetId) {
                        datasetId
                        workspaceId
                        name
                        channel
                        channelId
                        graphId
                        runs
                        priority
                        seed
                        createdBy
                        createdAt
                        estimatedEndAt
                        updatedAt
                        status
                        runsCancelled
                        runsFailed
                        runsQueued
                        runsRunning
                        runsStarting
                        runsSuccess
                        runsTimeout
                        instancesQueued
                        instancesRunning
                        instancesStarting
                    }
                }"""})
    return self.errorhandler(response, "getDatasetJobs")


def createDataset(self, workspaceId, graphId, name, runs, seed, priority, description=None):
    response = self.session.post(
        url = self.url, 
        headers = self.headers, 
        json = {
            "operationName": "createDataset",
            "variables": {
                "workspaceId": workspaceId,
                "graphId": graphId,
                "name": name,
                "description": description,
                "interpretations": runs,
                "seed": seed,
                "priority": priority
            },
            "query": """mutation 
                createDataset($workspaceId: String!, $graphId: String!, $name: String!, $description: String, $interpretations: Int!, $seed: Int!, $priority: Int!) {
                    createDataset(workspaceId: $workspaceId, graphId: $graphId, name: $name, description: $description, interpretations: $interpretations, seed: $seed, priority: $priority)
                }"""})
    return self.errorhandler(response, "createDataset")


def deleteDataset(self, workspaceId, datasetId):
    response = self.session.post(
        url = self.url, 
        headers = self.headers, 
        json = {
            "operationName": "deleteDataset",
            "variables": {
                "workspaceId": workspaceId,
                "datasetId": datasetId
            },
            "query": """mutation 
                deleteDataset($workspaceId: String!, $datasetId: String!) {
                    deleteDataset(workspaceId: $workspaceId, datasetId: $datasetId)
                }"""})
    return self.errorhandler(response, "deleteDataset")


def editDataset(self, workspaceId, datasetId, name=None, description=None):
    response = self.session.post(
        url = self.url, 
        headers = self.headers, 
        json = {
            "operationName": "editDataset",
            "variables": {
                "workspaceId": workspaceId,
                "datasetId": datasetId,
                "name": name,
                "description": description
            },
            "query": """mutation 
                editDataset($workspaceId: String!, $datasetId: String!, $name: String, $description: String) {
                    editDataset(workspaceId: $workspaceId, datasetId: $datasetId, name: $name, description: $description)
                }"""})
    return self.errorhandler(response, "editDataset")


def downloadDataset(self, workspaceId, datasetId):
    response = self.session.post(
        url = self.url, 
        headers = self.headers, 
        json = {
            "operationName": "downloadDataset",
            "variables": {
                "workspaceId": workspaceId,
                "datasetId": datasetId
            },
            "query": """mutation 
                downloadDataset($workspaceId: String!, $datasetId: String!) {
                    downloadDataset(workspaceId: $workspaceId, datasetId: $datasetId)
                }"""})
    return self.errorhandler(response, "downloadDataset")


def cancelDataset(self, workspaceId, datasetId):
    response = self.session.post(
        url = self.url, 
        headers = self.headers, 
        json = {
            "operationName": "cancelDataset",
            "variables": {
                "workspaceId": workspaceId,
                "datasetId": datasetId
            },
            "query": """mutation 
                cancelDataset($workspaceId: String!, $datasetId: String!) {
                    cancelDataset(workspaceId: $workspaceId, datasetId: $datasetId)
                }"""})
    return self.errorhandler(response, "cancelDataset")


def datasetUpload(self, workspaceId, filename, filesize, description):
    response = self.session.post(
        url = self.url, 
        headers = self.headers, 
        json = {
            "operationName": "uploadDatasetV2",
            "variables": {
                "workspaceId": workspaceId,
                "name": filename,
                "size": filesize,
                "description": description,
            },
            "query": """mutation 
                uploadDatasetV2($workspaceId: String!, $name: String!, $size: Float!, $description: String!) {
                    uploadDatasetV2(workspaceId: $workspaceId, name: $name, size: $size, description: $description){
                        key
                        uploadId
                        datasetId
                        partSize
                        urls
                    }
                }"""})
    return self.errorhandler(response, "uploadDatasetV2")

def datasetUploadFinalizer(self, workspaceId, uploadId, key, parts):
    response = self.session.post(
        url = self.url, 
        headers = self.headers, 
        json = {
            "operationName": "uploadDatasetV2Finalizer",
            "variables": {
                "workspaceId": workspaceId,
                "uploadId": uploadId,
                "key": key,
                "parts": parts,
            },
            "query": """mutation 
                uploadDatasetV2Finalizer($workspaceId: String!, $uploadId: String!, $key: String!, $parts: [MultipartInput!]) {
                    uploadDatasetV2Finalizer(workspaceId: $workspaceId, uploadId: $uploadId, key: $key, parts: $parts)
                }"""})
    return self.errorhandler(response, "uploadDatasetV2Finalizer")


def getDatasetRuns(self, workspaceId, datasetId, state=None):
    response = self.session.post(
        url = self.url, 
        headers = self.headers, 
        json = {
            "operationName": "getDatasetRuns",
            "variables": {
                "workspaceId": workspaceId,
                "datasetId": datasetId,
                "state": state,
            },
            "query": """query 
                getDatasetRuns($workspaceId: String!, $datasetId: String!, $state: String) {
                    getDatasetRuns(workspaceId: $workspaceId, datasetId: $datasetId, state: $state) {
                        runId
                        datasetId
                        workspaceId
                        channelId
                        startTime
                        endTime
                        state
                        run
                    }
                }"""})
    return self.errorhandler(response, "getDatasetRuns")


def getDatasetLog(self, workspaceId, datasetId, runId):
    response = self.session.post(
        url = self.url, 
        headers = self.headers, 
        json = {
            "operationName": "getDatasetLog",
            "variables": {
                "workspaceId": workspaceId,
                "datasetId": datasetId,
                "runId": runId
            },
            "query": """query 
                getDatasetLog($workspaceId: String!, $datasetId: String!, $runId: String!) {
                    getDatasetLog(workspaceId: $workspaceId, datasetId: $datasetId, runId: $runId) {
                        runId
                        datasetId
                        workspaceId
                        channelId
                        startTime
                        endTime
                        state
                        email
                        run
                        log
                    }
                }"""})
    return self.errorhandler(response, "getDatasetLog")