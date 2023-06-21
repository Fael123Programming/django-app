from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)
    

class AboutUs(models.Model):
    textLeft = models.CharField(max_length=500)
    textRight = models.CharField(max_length=500)
    

class AboutUsListItem(models.Model):
    text = models.CharField(max_length=100)
    