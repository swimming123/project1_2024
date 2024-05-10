#config/models.py
import cx_Oracle as ora
class MyModel:
    def myconn(self):
        conn = ora.connect("semiproject/semiproject@192.168.0.131/xe")
        return conn