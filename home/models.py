from django.db import models

# Create your models here.
class snippet_table(models.Model):
    name = models.CharField(max_length=122)
    value = models.TextField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    firstname = models.CharField(max_length=122)
    lastname = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=122)
    message = models.TextField()
    date = models.DateTimeField(null = True , blank = True)

    def __str__(self):
        return self.firstname