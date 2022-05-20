import string
from typing import Dict
from FileServers.AllFileServerImplementation.AzureBlob.AzureConnection import AzureBlobImageFileServer
from PIL import Image
import io
import os


class getFileServer:
    def __init__(self,  loadFileServersFromConfig : Dict):
        self.fileServerList = dict()
    def registerFileServer(self, fileServername):
        if (fileServername ==  "Azure") :             
            self.fileServerList[fileServername] =  AzureBlobImageFileServer()
    def getFileServer(self, fileServerName : string = "Azure"):
        return self.fileServerList.get(fileServerName)
        


