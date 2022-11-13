#coding=utf-8
import pymssql

class bank(object):
    def __init__(self, dbname = 'monopoly'):
        self.conn = pymssql.connect(host='127.0.0.1:1433', user='sa',
                                    password='SYN123456', database=dbname,
                                    charset="utf8")
        #try:
        self.cursor = self.conn.cursor()
        #self.sql = 'create table bank(id INT, name INT, deposit INT, PRIMARY KEY(id))'

        #self.sql = 'select * from bank'
        #self.sql = 'SELECT NAME FROM SYS.DATABASES;'

        self.cursor.execute('''
        IF OBJECT_ID('bank','U') IS NOT NULL 
        DROP TABLE bank
        create table bank(id INT NOT NULL, name NVARCHAR(50), deposit INT, PRIMARY KEY(id))
        ''')
        self.conn.commit()

        # 用一个rs变量获取数据
        #self.rs = self.cursor.fetchall()
        #print(self.rs)
        #except:
            #print('Database server error')


    def Earn(self, account, amount_of_money):
        pass


    def Pay(self, account, amount_of_money):
        pass


    def Transfer(self,account1,account2,amount_of_money):
        try:self.Pay(account1,amount_of_money);self.Earn(account2,amount_of_money)
        except: print('unable to Transfer')

