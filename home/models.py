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

class codeforce_submission(models.Model):
    problem_name = models.CharField(max_length=122)
    language = models.CharField(max_length=122)
    time = models.CharField(max_length=122)
    memory = models.CharField(max_length=122)
    solution =  models.TextField()
    date = models.DateTimeField(null = True , blank = True)

    def __str__(self):
        return self.problem_name
