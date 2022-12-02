from django.db import models

class Job(models.Model):
    image = models.ImageField(upload_to='images/')
    jobtitle = models.CharField(max_length=200, default='Title')
    summary = models.CharField(max_length=200)

    def __str__(self):
        return self.jobtitle

class MainSlider(models.Model):
    sliderimage = models.ImageField(upload_to='images/')
    headline = models.CharField(max_length=200)
    subtext = models.TextField(max_length=400)

    def __str__(self):
        return self.headline