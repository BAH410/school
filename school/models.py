from django.db import models


# Create your models here.


class Register_Student(models.Model):
    id = models.IntegerField(unique=True,
                             primary_key=True, editable=False)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField(max_length=8, blank=True, null=True)
    edu_level = models.CharField(max_length=200, blank=True, null=True)
    home_address = models.CharField(max_length=200, blank=True, null=True)
    next_of_kin = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'student'

    def __str__(self):
        return self.fname
