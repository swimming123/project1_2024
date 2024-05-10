from django.db import models

# Create your models here.
import cx_Oracle as ora

def myconn():
    conn = ora.connect("ictserver/ictserver@192.168.0.103/xe")
    return conn
def memberinsert(addr_list):
    conn = myconn()
    cursor = conn.cursor()
    print('con => ', cursor)
    #num, id, pwd, name, email, tel, addr, mdate
    sql = "insert into member values(member_seq.nextVal, :1, :2, :3, :4, :5, :6, sysdate)"
    cursor.execute(sql, addr_list)
    cursor.close()
    conn.commit()
    conn.close()
#http://192.168.0.103:9000/member/memIdchk?id=syyoon
def idcheck(idx):
    conn = myconn()
    cursor = conn.cursor()
    sql = "select count(*) from member where id=:id"
    cursor.execute(sql, id=idx)
    res = cursor.fetchone()
    cursor.close()
    conn.close()
    return res