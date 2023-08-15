from django.db import models

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=200,verbose_name='Title')
    complete=models.BooleanField(default=False,verbose_name='Completed')
    created=models.DateTimeField(auto_now_add=True, verbose_name='Created')
    def __str__(self):
        return self.title
