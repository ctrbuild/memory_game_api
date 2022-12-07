from django.db import models

# Create your models here.
    #  {id:0, name: 'Bryan Canstron', status: '', img:'/images/01.jpg'},
class Card(models.Model):
    match = models.IntegerField()
    name = models.CharField(max_length=200, default="")
    status = models.CharField(default="", max_length=200)
    img = models.CharField(max_length=200)


class Score(models.Model):
    val = models.FloatField()
    user_name = models.CharField(max_length=200, null=False)

