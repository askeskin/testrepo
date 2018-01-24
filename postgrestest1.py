from postgres import Postgres

class PostgresHelper:
    def __init__(self,server,dbname,username):
        self.server=server
        self.dbname=dbname
        self.username=username
        self.db = Postgres("postgres://"+self.username+"@"+self.server+"/"+self.dbname)

    def executeCommand(self,commandStr):
        self.db.run(sql=commandStr)

    def getMultipleCursor(self,spname,parameters,refcursors):
        paramstr=""
        cursorstr=""
        for refcursor in refcursors:
            cursorstr+="'"+refcursor+"',"

        for param in parameters:
             paramstr+=param +","
        if paramstr.endswith(','):
            paramstr=paramstr[:-1]

        if cursorstr.endswith(','):
            cursorstr = cursorstr[:-1]
        data = {}
        with self.db.get_cursor() as cursor:
            cursor.run("select "+spname+"("+paramstr+","+cursorstr+");")
            for refcursor in refcursors:
                fetchstr = 'FETCH ALL IN "' + refcursor + '";'               

                tempdata= cursor.all(fetchstr)
                ##print(tempdata)                

                data[refcursor]=tempdata

        return data
       ## kayit = self.db.run(sql="select "+spname+"("+paramstr+","+cursorstr+");")
    def getSingleCursor(self,spname,parameters):
        return self.getMultipleCursor(spname=spname,parameters=parameters,refcursors=["rc1"])

p  = PostgresHelper(server="localhost",dbname="testdb",username="postgres")
data = p.getSingleCursor(spname="getTypes2",parameters=["1::smallint"])
print(data)