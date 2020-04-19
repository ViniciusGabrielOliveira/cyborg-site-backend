import datetime
from django.db import models
from django.utils import timezone

class Noticia(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    reference_date = models.DateField(default=datetime.date.today)
    text = models.TextField()
    tags = models.CharField(max_length=500, default='')
    image = models.CharField(max_length=1000)
    classification = models.IntegerField(default=0)

    def __str__(self):
        return self.noticia_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
