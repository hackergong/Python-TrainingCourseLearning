from mysqlall import MySqlAll

s = MySqlAll("localhost","root","tracy","eddy")
reslist = s.get_all("select * from bankcard where money>400")
for row in reslist:
    print("%d--%d" % (row[0],row[1]))
