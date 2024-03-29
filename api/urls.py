from django.urls import path

from .views import * 

urlpatterns = [
    path('invoice',InvoiceMasterListView.as_view(),),
]
