from django.shortcuts import render,get_object_or_404
from .models import Customer

# Create your views here.
#customer detail list
def customer_detail(request,pk):
    cust = get_object_or_404(Customer, pk = pk)
    return render(request,'customer/customer_detail.html',{'customer':cust})


#customer list
def customer_list(request):
    custs = Customer.objects.order_by('name')
    return render(request, 'customer/customer_list.html',{'customers':custs})


