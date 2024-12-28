from django.db import models

# Create your models here.
class CustomerDetails(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(help_text="Example:xyz_01@gmail.com")
    address = models.TextField()
    age = models.IntegerField()
    pno = models.CharField(max_length=10, null=True, blank=True)


    def __str__(self):
        return f" name :- {self.name}"

