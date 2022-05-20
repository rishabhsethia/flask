import pyodbc
import config
sql_conn_string = config.sql_conn_string

class sqlConnection : 
    def __init__(self) -> None:
        self.connectionString = sql_conn_string
    def getConnection(self): 
        print(self.connectionString)
        con = pyodbc.connect(self.connectionString)      
        return con

    def IsUserAuthorized(self, email,password):
        con = self.getConnection()
        cursor = con.cursor()
        query =  "select count(*) count from [flaskApp].[USER].[user_master] where EMAIL='" + email + "' and password='" + password + "';"
        print("query is " + query)
        cursor.execute(query) 
        row = cursor.fetchone() 
        count = 0
        while row: 
            count = row[0]
            row = cursor.fetchone()
        if(count > 0):
             return True 
        return False
        
    def runDmlScript(self, script):
        print("script" + script)
        con = self.getConnection()
        con.execute(script)
        con.commit()         
        return True
    def getBlolbUrlfromDb(self, script):
        print("script" + script)
        con = self.getConnection()
        cursor = con.cursor()
        cursor.execute(script) 
        row = cursor.fetchone()      
        bloburlList= []  
         
        while row: 
            bloburlList.append(row[1])
            row = cursor.fetchone()
        return bloburlList
        
    

    
    