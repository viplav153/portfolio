from django.db import models

# Create your models here.
class job(models.Model):
    image =models.ImageField(upload_to="images/")
    summary= models.CharField(max_length=200)
   # http://localhost:8000/media/images/fifa_ybaMeJZ.png