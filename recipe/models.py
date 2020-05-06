from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.Author model:
class Author(models.Model):
    name = models.CharField( max_length=50)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date = models.DateTimeField(default=timezone.now)
    description = models.TextField()
    time_required = models.CharField(max_length=50)
    instructions = models.TextField()

    def __str__(self):
        return self.title