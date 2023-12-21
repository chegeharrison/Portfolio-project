from django.db import models

# Create your models here.
class Course(models.Model):
    image = models.ImageField(upload_to ='static/media/')
    summary = models.CharField(max_length = 200)

    def __str__(self):
        return"%s %s" %(self.image,self.summary)
