
#import Lab42_dboperations

from Lab42_dboperations import MySQLDatabase


#Lab42_dboperations.addnum(10,20)
#print(Lab42_dboperations.dbinfo)

dbobj = MySQLDatabase()

dbobj.getall_databases()

dbobj.getdatabaseinfo()

dbobj.close()
