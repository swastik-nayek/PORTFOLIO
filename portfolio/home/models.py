from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length = 122)
    email = models.CharField(max_length = 122)
    phone = models.CharField(max_length = 12)
    catagory = models.CharField(max_length = 12)
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=13)
    slug = models.CharField(max_length=130)
    

    def __str__(self):
        return self.title + ' Massege from ' + self.author