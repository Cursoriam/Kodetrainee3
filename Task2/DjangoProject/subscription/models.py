from django.db import models

class Trader(models.Model):
    email=models.EmailField(primary_key=True)

    def __str__(self):
        return self.email

class Subscription(models.Model):
    ticker=models.CharField(max_length=10, null=True)
    email=models.ForeignKey(Trader, on_delete=models.CASCADE)
    max_price=models.FloatField(blank=True, null=True)
    min_price=models.FloatField(blank=True, null=True)
    

    def __str__(self):
        return self.ticker
