from django.db import models
from django.core.validators import EmailValidator

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True, validators=[EmailValidator()])
    notes = models.TextField(blank=True)
    credit_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('customers:customer_detail', args=[str(self.id)])
