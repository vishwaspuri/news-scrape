from django.db import models

# Create your models here.


class Article(models.Model):
    title=models.CharField(max_length=150)
    description=models.TextField()
    article_link = models.CharField(max_length=150)
    image_link = models.CharField(max_length=150)
    def __str__(self):
        return self.title



