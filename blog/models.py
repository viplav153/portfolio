from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title

    def summary(self):
        return self.text

    def pub_date_pretty(self):
        return self.date

    

    
    

