from Login.models import Login
from django.db import connection


class Dao:  
	def Login(self, emailid, password):
		cursor = connection.cursor()
		query = ("select * from Login where Email_id=%s and Password=%s")
		values = (emailid, password)
		cursor.execute(query,values) 
		a = cursor.fetchall()
		b = list(a) 
		return b