from django.db import models


class Todo(models.Model):
   text = models.CharField(max_length=200)
   status = models.BooleanField(default=False)

   def __str__(self):
      return f"{self.text} - {self.status}"