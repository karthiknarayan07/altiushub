from django.db import models
import uuid
# Create your models here.

class InvoiceMaster(models.Model):
    id = models.UUIDField(default=uuid.uuid4, null=False, blank=False,primary_key=True)
    
    date = models.CharField(max_length=30, null=False, blank=False)
    invoice_number = models.IntegerField(null=False, blank=False, unique=True)
    customer_name = models.CharField(max_length=150, null=False, blank=False)
    
    shipping_address = models.CharField(max_length=150, null=False, blank=False)
    billing_address = models.CharField(max_length=150, null=False, blank=False)
    gstin = models.CharField(max_length=30, null=False, blank=False)
    total_amount = models.DecimalField(max_digits=16, decimal_places=2, default=0, null=False, blank=False)
    


class InvoiceItems(models.Model):
    id = models.UUIDField(default=uuid.uuid4, null=False, blank=False, primary_key=True)
    
    invoice_master = models.ForeignKey('InvoiceMaster', on_delete=models.CASCADE, null=False, blank=False)
    
    item_name = models.CharField(max_length=150, null=False, blank=False)
    quantity = models.DecimalField(max_digits=16, decimal_places=2, default=0, null=False, blank=False)
    price = models.DecimalField(max_digits=16, decimal_places=2, default=0, null=False, blank=False)
    amount = models.DecimalField(max_digits=16, decimal_places=2, default=0, null=False, blank=False)
    

class InvoiceBillSundry(models.Model):
    id = models.UUIDField(default=uuid.uuid4, null=False, blank=False, primary_key=True)
    
    invoice_master = models.ForeignKey('InvoiceMaster', on_delete=models.CASCADE, null=False, blank=False)
    
    bill_sundry_name = models.CharField(max_length=150, null=False, blank=False)
    amount = models.DecimalField(max_digits=16, decimal_places=2, default=0, null=False, blank=False)