from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import CustomerDetails



def customer_details(request):
    if request.method == 'POST':

        customer_name = request.POST['name']
        customer_email = request.POST['email']
        customer_address = request.POST['address']
        customer_pno = request.POST['pno']
        customer_age = request.POST['age']

        customer_obj = CustomerDetails(name=customer_name, email=customer_email, age=customer_age,
                                       address=customer_address, pno=customer_pno)
        customer_obj.save()
        return redirect('/search/')

    return render(request,'customerDetails.html')

def customer_search(request):
    database_obj = CustomerDetails.objects.all()
    context = {'data': database_obj}

    return render(request,'customerSearch.html',context)