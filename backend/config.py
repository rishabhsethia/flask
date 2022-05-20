import os
basedir = os.path.abspath(os.path.dirname(__file__))

BASEDIR = basedir
#Security configuration
CSRF_ENABLED = True
SECRET_KEY = 'sdfsdf/sdf\sdf'


##################### Azure - Connection - sample ###################
connection_string ="DefaultEndpointsProtocol=https;AccountName=sdf;AccountKey=sdfsdfsd+KPvfmQ==;EndpointSuffix=core.windows.net";
container_name = "NewContainer"

##################### Sql sERVER COnnection String ###################
sql_conn_string = "Driver={SQL Server};Server=sdfsdf;Database=sdf;TRUSTED_CONNECTION=yes;TrustServerCertificate=yes"

##################### Cors Origin Allow #######################
corsOriginAllow = "VUEappuRL"