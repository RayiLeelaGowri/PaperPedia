
from django.db import models

class QuestionPaper(models.Model):
    year = models.IntegerField()
    branch = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    file = models.FileField(upload_to='papers/')

    def __str__(self):
        return f"{self.subject} - {self.year} - {self.branch}"
