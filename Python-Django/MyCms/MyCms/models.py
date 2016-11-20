from django.db import models

class Student(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	#school = models.CahrField(max_length=40)
	def __str__(self):
		return self.first_name + ' ' + self.last_name