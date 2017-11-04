# encoding = utf-8
import string,random
import pymysql

field = string.ascii_letters+string.digits #指定字符范围为数字+字母

# 随机生成4个由数字或字母组成的字符串
def getrandom():
    return "".join(random.sample(field,4))


# 将4组长度为4的字符串用‘-’拼接，即生成一组激活码
def concatenate():
    return '-'.join([getrandom() for i in range(4)])

#生成指定数量的激活码
def generate(n):
    return [concatenate() for i in range(n)]

#将数据存入mysql数据库
def save_to_db(codes):
    conn = pymysql.connect(host='localhost',port=3306,user='root',passwd='xxxxxxxx',db='test')    # 创建连接
    cursor = conn.cursor()                                              #创建一个游标
    sql="insert into tb1(id,code) values(%s,%s)"                        # sql语句
    for i in range(len(codes)):
        cursor.execute(sql,(i,codes[i]))                                #执行sql语句
    conn.commit()
    conn.close()


if __name__ == '__main__':
    save_to_db(generate(200))

