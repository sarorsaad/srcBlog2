from django.db import models

# Create your models here.
class Post(models.Model):

    # Fields
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    content = models.TextField(max_length=5000)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)