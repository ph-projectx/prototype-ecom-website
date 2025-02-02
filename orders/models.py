from django.db import models
from shop .models import Product

# Create your models here.

class Order(models.Model):
    """Order Model for customer."""
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=250)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)
    braintree_id = models.CharField(max_length=150, blank=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        """String representation of order id """
        return f'Order {self.id}'

    def get_total_cost(self):
        """String representation of Total Cost"""
        return sum(item.get_cost() for item in self.items.all())

class OrderItem(models.Model):
    """Order Item Model"""
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        """Return String Representation of Orderitem id"""
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity
        """Return String Representation of total cost"""

