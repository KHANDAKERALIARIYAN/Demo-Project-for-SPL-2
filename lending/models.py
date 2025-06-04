from django.db import models
from django.utils import timezone
from inventory.models import Product
from customers.models import Customer

class LendingRecord(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    lend_date = models.DateField(default=timezone.now)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('active', 'Active'),
            ('returned', 'Returned'),
            ('overdue', 'Overdue')
        ],
        default='active'
    )
    notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.name} - {self.product.name}"

    def save(self, *args, **kwargs):
        if self.return_date:
            self.status = 'returned'
        elif self.due_date < timezone.now().date() and not self.return_date:
            self.status = 'overdue'
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-lend_date']

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('lending:lending_detail', args=[str(self.id)])
