import  pymysql




class MyMetaclass(type):
    def __new__(cls, classname,supername,sttrs):


        create_dict = {}

        for key,value in sttrs.items():

            if isinstance(value,tuple):
                create_dict[key] = value[0]

        sttrs['create_dict'] = create_dict
        sttrs['table_name'] = classname.lower()


        return type.__new__(cls,classname,supername,sttrs)

class YuQiong(object,metaclass=MyMetaclass):
    uid = ("int unsigned ",)
    name = ("varchar(30)",)
    email = ("varchar(30)",)
    password = ("varchar(30)",)

    def __init__(self):
        self.connect = pymysql.connect(host="localhost",port=3306 ,database="stock_db",user="root",password="mysql",charset="utf8")
        self.cur = self.connect.cursor()



    def create_table(self):

        create_list = []

        for key,value in self.create_dict.items():

            create_list.append("%s  %s"%(key,value))

        print(create_list,'11\n')

        create_sql = """CREATE TABLE IF NOT EXISTS %s(%s);""" % (self.table_name, ",".join(create_list),)

        self.cur.execute(create_sql)

        self.connect.commit()


    def insert(self,**kwargs):

        insert_keys = []

        insert_values = []

        for key,value in kwargs.items():

            insert_keys.append(key)

            if isinstance(value , int):
                insert_values.append(str(value))
            else:
                insert_values.append(""" '%s' """ %value)

        insert_sql = """insert into %s (%s) values (%s);""" % (
        self.table_name, ",".join(insert_keys), ",".join(insert_values))

        self.cur.execute(insert_sql)

        self.connect.commit()


    def select_database(self):
        sql = "select * from %s" % self.table_name
        self.cur.execute(sql)
        data = self.cur.fetchall()
        for value in data :
            print(value)


    def delete(self,**kwargs):


        delete_key = []
        delete_value = []

        for key,value in kwargs.items():

            delete_key.append(key)

            if isinstance(value ,int ):
                delete_value.append(str(value))

            else:
                delete_value.append(""" '%s' """ %value)



        delete_sql = """delete from %s where %s = %s """ %(self.table_name,delete_key[0],delete_value[0])
        print(delete_sql)

        self.cur.execute(delete_sql)

        self.connect.commit()






    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cur.close()
        self.connect.close()


def main():
    usql = YuQiong()

    usql.create_table()
    # usql.insert(name='HANFEI',UID='1',password='123')

    usql.insert(name='ting2',UID='4',password='456')
    usql.insert(name='yaya',UID='3',password='789')

    usql.select_database()

    usql.delete(name='yaya')


if __name__ == '__main__':
    main()