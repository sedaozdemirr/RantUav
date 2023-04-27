from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)

    def __str__(self):
        return self.name
class Uav(models.Model):
    img = models.ImageField(null=True,blank=True,upload_to='media/')
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255,null=True,blank=True)
    weight = models.IntegerField()
    category = models.CharField(max_length=255,null=True,blank=True)
    airtime = models.IntegerField()
    price = models.IntegerField()
    availability = models.BooleanField(null=True)

    def __str__(self):
        return self.model
class Reservation(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    uav = models.ForeignKey(Uav, on_delete=models.CASCADE)
    issue_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return str(self.customer) + "- " + str(self.car)