from django.db import models

# Create your models here.

class Post(models.Model):
    post_image = models.CharField(max_length=450)
    post_title = models.CharField(max_length=150)
    post_content = models.TextField()

    def __str__(self):
        return self.post_title

class ContactMessage(models.Model):
    message_id = models.IntegerField(primary_key=True)
    email = models.CharField(max_length=150)
    subject = models.CharField(max_length=150)
    message = models.TextField()

    def __str__(self):
        return self.email + ": " + self.subject