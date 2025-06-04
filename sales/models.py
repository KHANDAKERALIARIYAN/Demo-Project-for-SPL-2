from django.db import models
from django.utils import timezone
from inventory.models import Product
from customers.models import Customer

class Sale(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(
        max_length=20,
        choices=[
            ('cash', 'Cash'),
            ('credit', 'Credit'),
            ('card', 'Card'),
            ('mobile', 'Mobile Payment')
        ],
        default='cash'
    )
    invoice_number = models.CharField(max_length=20, unique=True)
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Sale #{self.invoice_number}"

    class Meta:
        ordering = ['-date']

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('sales:sale_detail', args=[str(self.id)])

class SaleItem(models.Model):
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} x {self.quantity}"

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.unit_price
        super().save(*args, **kwargs)
        # Update product quantity
        self.product.quantity -= self.quantity
        self.product.save()
