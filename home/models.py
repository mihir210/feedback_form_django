from django.db import models

# Create your models here.

class Contact(models.Model):
   name = models.CharField(max_length=122)
   email =models.CharField(max_length=120)
   department = models.CharField(max_length=20)
   roll_no = models.CharField(max_length=20)
   feedback_text = models.TextField()
   date = models.DateField()

   def __str__(self):
      return self.name
