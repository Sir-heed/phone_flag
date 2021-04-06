from django.db import models

# Create your models here.
class Device(models.Model):
    name = models.CharField(max_length=250)
    status = models.CharField(max_length=250)
    imei_1 = models.CharField(max_length=250)
    imei_2 = models.CharField(max_length=250, null=True, blank=True)
    details = models.CharField(max_length=250)
    model = models.CharField(max_length=250)
    color = models.CharField(max_length=250)
    phone_no = models.CharField(max_length=250)

    def __str__(self):
        self.name