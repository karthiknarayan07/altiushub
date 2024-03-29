from rest_framework import serializers


from .models import InvoiceMaster, InvoiceItems, InvoiceBillSundry


class InvoiceMasterSerializer(serializers.ModelSerializer):
    
    
    
    class Meta:
        model = InvoiceMaster
        fields = '__all__'
        
        
class InvoiceItemsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = InvoiceItems
        fields = '__all__'

class InvoiceBillSundrySerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceBillSundry
        fields = '__all__'