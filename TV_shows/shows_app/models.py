from django.db import models

# Create your models here.
class Networks(models.Model):
    id = models.AutoField(primary_key=True)
    name= models.CharField(max_length=255)

class Show(models.Model):
    id = models.AutoField(primary_key=True)
    title= models.CharField(max_length=255)
    release_date = models.DateTimeField()
    description = models.TextField(default='')
    network = models.ForeignKey(Networks, related_name='shows', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

