from django.db import models
# import user class
from django.contrib.auth.models import User

# create title

class Title(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)
# creating user model

class Userform(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Title, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    order= models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    discription = models.TextField(null=True, blank=True)
    # for timestamp

    tile = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


