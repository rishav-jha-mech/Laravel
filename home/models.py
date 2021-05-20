from django.db import models
from django.conf.urls.static import static
from django.conf import settings
# Create your models here.

class Contact(models.Model):
    name= models.CharField(max_length=40)
    email= models.CharField(max_length=50)
    phone= models.CharField(max_length=122)
    desc= models.TextField()
    date=models.DateField(null=True)

    def __str__(self):                 #to change the titles of contact
        return self.name

class Blog(models.Model):
    post_id= models.AutoField(primary_key=True)
    blogtitle= models.TextField(max_length=300, default="")
    name= models.TextField(max_length=50, default="Anonymous")
    blogsubtitle= models.TextField(max_length=200, default="")
    blogcontent= models.TextField(default="")
    pub_date=models.DateField(null=True)
    thumbnail= models.ImageField(null= True, blank=True,upload_to= "blog_thumbnails/%Y/%m/%d/")

    def __str__(self):                 #to change the titles of contact
        return self.blogtitle
