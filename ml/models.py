from django.db import models

# Create your models here.
class paymentDetails(models.Model):
    step = models.IntegerField()
    payment_type = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    nameOrig = models.CharField(max_length=200)
    oldbalanceOrg = models.DecimalField(max_digits=100, decimal_places=2)
    newbalanceOrig = models.DecimalField(max_digits=100, decimal_places=2)
    nameDest = models.CharField(max_length=200)
    oldbalanceDest = models.DecimalField(max_digits=100, decimal_places=2)
    newbalanceDest = models.DecimalField(max_digits=100, decimal_places=2)
    isFraud = models.BooleanField()
    isFlaggedFraud = models.BooleanField()
    
    def __str__(self):
        return self.payment_type