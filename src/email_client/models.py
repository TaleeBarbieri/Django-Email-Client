from django.db import models


class Email(models.Model):
    subject = models.CharField(max_length=500)
    message = models.TextField(max_length=500)
    email = models.EmailField()

    def __str__(self):
        return self.id
