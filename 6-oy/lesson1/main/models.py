from django.db import models

class Banner(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(default='')
    img = models.ImageField(upload_to='banner/',null=True)

    def __str__(self):
        return self.title
    

class Media(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(null=True)
    image = models.ImageField(upload_to='media/',null=True)
    # image = models.ImageField(auto_now_add=True)

class Contact(models.Model):
    fname = models.CharField(max_length=255)
    lname = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=13)
    body = models.TextField()
    is_checked = models.BooleanField()

class SocialSites(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=255)

