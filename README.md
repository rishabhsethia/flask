# flask
Flask-Vue Demo App

This Demo App architecture is as follows : 

  Frontent(using Node+vue as webserver) -> Backend(FLask) -> FileServer used here is Azure BLOB
                                                          -> Db Server Azure Sql Server
 
 Flow Chart of The Process : 
 
 ![image](https://user-images.githubusercontent.com/17291821/169574804-bd5baf2e-663c-40b2-b765-4280a73270f6.png)


Upload Image Flow : 

Azure Blob Storage is chosen as File Server - for reliability, scalability, read speeds(load balanced), maintainance
1) Image uploaded by user -> is sent to node server
2) Node Server sends this image to Flask Backend
3) Flask receives this image and compresses the image(in memory)
4) Image(bytes) is uploaded to Azure Blob
5) Image(blolb url), user info is stored in sql server

Download Image Flow : 

1) User Image URL are retreived from Sql Server
2) These Url are sent to User in api Request
3) Images Are cached in browser(multiple request of same images, would be server from browser cache)

