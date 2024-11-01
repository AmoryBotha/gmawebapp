from django.db import models
from django.contrib.auth.models import User
# Create your models here.


#model for notes
#foreign keys link users to data that belongs to that user ex. each collection of notes 1*M User*notes
class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")

    def __str__(self):
        return self.title