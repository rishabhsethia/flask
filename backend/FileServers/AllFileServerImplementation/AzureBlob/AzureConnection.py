import os, uuid, config
from Database.getDbConnection import sqlConnection
import string
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
# todo os environment
connection_string = config.connection_string
container_name = config.container_name

class AzureBlobImageFileServer:
    def __init__(self, constr=connection_string, containerName = container_name):
        self.connectionString = constr
        self.containerName = container_name
    def createContainer(self) -> string: 
        try:            
            container_client =  ContainerClient.from_connection_string( conn_str=self.connectionString, container_name=self.containerName)            
            return container_client.create_container(self.containerName)                    
        except Exception as ex:
            print('Exception:  "container Already Exist"')
            return "container Already Exist"

    def uploadImageToContainer(self, filename, compressedImageInBytes) -> bool: 
        try:       
            self.createContainer();
            container_client =  ContainerClient.from_connection_string( conn_str=self.connectionString, container_name=self.containerName)
            message = container_client.upload_blob(name=filename,data=compressedImageInBytes)      
            blolburl = f"https://imageuploaderflaskapp.blob.core.windows.net/{self.containerName}/{filename}"
            script = f"INSERT INTO [IMAGE].[IMAGES]([USERID],[URL]) VALUES(1,'{blolburl}')"
            sqlConnection().runDmlScript(script)
            return True      
        except Exception as ex:
            print('Exception:')
            print(ex)
            return ex.__str__() 
    def identify(self):
        return "yes I am Azure"
    def downloadUserImages(self, userId) -> bool: 
        try:            
            container_client =  ContainerClient.from_connection_string( conn_str=self.connectionString, container_name=self.containerName)
            script = f"select [PHOTOID],[URL] FROM [IMAGE].[IMAGES] WHERE [USERID] = {userId};"
            blolburlList = sqlConnection().getBlolbUrlfromDb(script)
            return blolburlList      
        except Exception as ex:
            print('Exception:')
            print(ex)
            return ex.__str__() 
    def identify(self):
        return "yes I am Azure"    