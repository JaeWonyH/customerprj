from django.shortcuts import render, get_object_or_404, redirect

from .forms import CustomerModelForm
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

#글 등록(modelform 사용)
def customer_new_modelform(request):
    if request.method == "POST":
        # 등록을 요청하는 경우
        customer_form = CustomerModelForm(request.POST)
        if customer_form.is_valid():
            post = customer_form.save() #model 객체 생성 및 db 저장
            return redirect('customer_detail', pk = post.pk) #등록 후 글 상세 url로 이동(리다이렉션 처리)
    else:
        # 글 등록을 위한 form을 출력
        customer_form = CustomerModelForm()
    return render(request, 'customer/customer_edit.html', {'customerform': customer_form})


