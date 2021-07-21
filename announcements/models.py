from django.db import models

# Create your models here.
class Announcements(models.Model):
    title = models.TextField()
    poster = models.URLField()
    date = models.DateField()
    content = models.TextField()
    url = models.URLField()


    def __str__(self):
        return self.title