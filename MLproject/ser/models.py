from django.db import models

# Create your models here.
class Audio(models.Model):
	record=models.FileField(upload_to='Sound recordings/')
	
	class Meta:
		db_table='Audio'

