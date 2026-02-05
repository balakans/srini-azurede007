
#import Lab42_dboperations

from Lab42_dboperations import MySQLDatabase


#Lab42_dboperations.addnum(10,20)
#print(Lab42_dboperations.dbinfo)

dbobj = MySQLDatabase()

dbobj.getall_databases()

dbobj.getdatabaseinfo()

dbobj.close()

"""git commands 
git init
git config --global user.name "srinikg"
git config --global user.email "srinikg@gmail.com`"


git add .
git commit -m "First Commit"
git log
git log --oneline
git branch #list branch
git branch dev #create branch
git checkout dev #switch branch

"""