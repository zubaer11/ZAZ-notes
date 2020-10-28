from django.db import models

# Create your models here.
class Contact(models.Model):
    serial_no = models.AutoField(primary_key = True)
    user_name = models.CharField(max_length=100)
    contact_mail = models.CharField(max_length=150)
    contact_number = models.CharField(max_length=15)
    subject_of_issue = models.CharField(max_length=200)
    issue = models.CharField(max_length=1000)
    sent_date = models.DateTimeField(auto_now_add=True, blank = True)

    def __str__(self):
        return self.user_name + '->' + self.subject_of_issue

class Subscribe(models.Model):
    email = models.CharField(max_length= 100)

    def __str__(self):
        return self.email