#coding=utf-8
import pymssql

class DBchat(object):
    def __init__(self,dbname = 'TestDB'):
        self.conn = pymssql.connect(host='127.0.0.1',user='sa',
                               password='SYN123456',database=dbname,
                               charset="utf8")
    def pull(self):
        self.cursor = self.conn.cursor()
        self.sql = 'SELECT * FROM Inventory WHERE quantity > 152;'
        self.cursor.execute(self.sql)
        # 用一个rs变量获取数据
        self.rs = self.cursor.fetchall()
        return(self.rs)

    def push(self,id):
        pass


'''    
#查看连接是否成功
print(conn)
cursor = conn.cursor()
sql = 'SELECT * FROM Inventory WHERE quantity > 152;'
cursor.execute(sql)
#用一个rs变量获取数据
rs = cursor.fetchall()
print(rs)'''