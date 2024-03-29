from rest_framework.views import APIView

from rest_framework import status

from rest_framework.response import Response

from rest_framework.permissions import AllowAny


from .models import *

from .serializers import * 

from django.db.models import Sum


class InvoiceMasterListView(APIView):
    permission_classes = (AllowAny,)
    
    def get(self,request):
        try:
            
            
            invoice = InvoiceMaster.objects.filter(id=request.GET.get('id')).first()
            
            serializer = InvoiceMasterSerializer(invoice)
            
            items = InvoiceItems.objects.filter(invoice_master = invoice)
            
            item_serializer = InvoiceItemsSerializer(items, many=True)
            
            bill_sundrys = InvoiceBillSundry.objects.filter(invoice_master = invoice)
            sundry_serializer = InvoiceBillSundrySerializer(bill_sundrys,many=True)
            
            response = {
                **serializer.data,
                'items': item_serializer.data,
                'bill_sundrys':sundry_serializer.data
            }
            
            return Response(
                response,status=status.HTTP_200_OK
            )
        
        except Exception as error:
            return Response('Exception in List View:- '+str(error))
        
    
    def post(self,request):
        
        try:
            
            data = request.data.copy()
            
            serializer = InvoiceMasterSerializer(data=data)
            
            if serializer.is_valid():
                master_invoice_obj = serializer.save()
                
                # creating product items
                total_amount = 0
                for item in data['items']:
                    item['invoice_master'] = master_invoice_obj.pk
                    item['amount'] = float(item['price']) * int(item['quantity'])
                    item_serializer = InvoiceItemsSerializer(data=item)
                    if item_serializer.is_valid():
                        item_serializer.save()
                        total_amount += item['amount']
                    else:
                        return Response(serializer.errors,status=status.HTTP_201_CREATED)
                    
                # creating bill sundrys
                for item in data['bill_sundrys']:
                    item['invoice_master'] = master_invoice_obj.pk
                    sundry_serializer = InvoiceBillSundrySerializer(data=item)
                    if sundry_serializer.is_valid():
                        sundry_serializer.save()
                        total_amount += item['amount']
                    else:
                        return Response(serializer.errors,status=status.HTTP_201_CREATED)
                    
                master_invoice_obj.total_amount = total_amount
                master_invoice_obj.save()
                
                
                return Response(serializer.data,status=status.HTTP_400_BAD_REQUEST)
            
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
        except Exception as error:
            return Response('Exception in Invoice Create View:- '+str(error))