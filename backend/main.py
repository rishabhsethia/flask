import io
import json
from sre_constants import SUCCESS
from flask import Flask, Response, jsonify, request, session
from flask_cors import CORS
from requests import session
from Database.getDbConnection import sqlConnection
from FileServers.AllFileServerImplementation.AzureBlob.AzureConnection import AzureBlobImageFileServer
from PIL import Image
import os
from FileServers.GetFileServer.FileServerFactory import getFileServer
import config
app = Flask(__name__)

app.config.from_object(__name__)
CORS(app, resources={r"/*":{'origins' : "*"}})
CORS(app, resources=
    {r"/*":{
        'origins' : config.corsOriginAllow, 
        "allow_headers": "Access-Control-Allow-Origin"""
        }
    }
)
#todo seperate class structure 
@app.route('/uploadImage', methods=['GET', 'POST'])
def uploadImageService():
    #image_data = request.get_data(cache = False)
    for file in request.files.getlist("photos"):  
        output += file.filename + " "      
        imageInBytes = Image.open(file.stream)
        compressesimagebytes = io.BytesIO()
        fileExtension = os.path.splitext(file.filename)[1].removeprefix(".")    
        imageInBytes.save(compressesimagebytes,format=fileExtension.upper())            
        isItUploaded = AzureBlobImageFileServer(config.connection_string, config.container_name).uploadImageToContainer(file.filename, compressesimagebytes.getvalue())
        output += " upload Completed successfully"
    return "<p>Uploaded: {}</p>".format(output)

@app.route('/downloadImage', methods=['GET', 'POST'])
def downloadImageService():
    #image_data = request.get_data(cache = False)
    blolbUrlList = AzureBlobImageFileServer(config.connection_string, config.container_name).downloadUserImages(1)   
    print(blolbUrlList) 
    return Response(json.dumps(blolbUrlList), mimetype='application/json')
    

@app.route('/login', methods=['GET', 'POST'])
def login():    
    if request.method == "POST":        
        data = request.get_json(force=True)
        email = data["username"]
        password = data["password"]
        sqlConObj = sqlConnection()        
        IsUserAuthorized = sqlConObj.IsUserAuthorized(email, password)
        #password = request.form.get("password")
        return IsUserAuthorized.__str__()
    return 

if __name__ == "__main__":
    app.run(debug=True)
