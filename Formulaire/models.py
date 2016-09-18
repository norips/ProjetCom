from django.db import models

# Create your models here.

class Form(models.Model) :
    title = models.CharField(max_length=200,default = 'Default title')
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class FieldForm(models.Model) :
    form = models.ForeignKey(Form, on_delete = models.CASCADE)
    question = models.CharField(max_length = 250)

    def __str__(self):
        return  self.question

class Answer(models.Model):
    field = models.ForeignKey(FieldForm, on_delete = models.CASCADE)
    answer = models.BooleanField()

    def __str__(self):
        return self.answer