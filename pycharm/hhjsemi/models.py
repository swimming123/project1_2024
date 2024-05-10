from django.db import models

# Create your models here.

from config.models import MyModel

class ProjectModel(MyModel):
    def ProjectList(self,Project_list):
        conn = self.myconn()
        cursor = conn.cursor()
        sql = "SELECT title FROM NEWSDATA WHERE SCATEGORY =:1 AND NEWSDATE BETWEEN :2 AND :3 ORDER BY NEWSDATE"
        cursor.execute(sql, Project_list)
        res = cursor.fetchall()
        cursor.close()
        conn.close()
        return res

    def projectTitle(self,Project_title):
        conn = self.myconn()
        cursor = conn.cursor()
        sql = "SELECT title FROM (SELECT title FROM NEWSDATA WHERE SCATEGORY = :1 AND NEWSDATE BETWEEN :2 AND :3 AND title LIKE '%' || :4 || '%' ORDER BY NEWSDATE DESC) WHERE ROWNUM <= 5"
        cursor.execute(sql, Project_title)
        res = cursor.fetchall()
        cursor.close()
        conn.close()
        return res