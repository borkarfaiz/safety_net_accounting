from django.db import models


# Create your models here.
class TimeStampModel(models.Model):
    """An Abstract base class model that provides
        self update and self created fields.
    """
    created = models.DateTimeField(auto_created=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Customer(TimeStampModel):
    """This class is used to store the first and last name
        and the mobile number"""
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return (self.first_name + ' ' + self.last_name)
