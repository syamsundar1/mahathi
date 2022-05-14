from django.shortcuts import render
from .models import Amounts
from django.core.mail import send_mail
# Create your views here.

def index(request):
    amountobjects = Amounts.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phonenumber = request.POST.get('phonenumber')

        data = {
            'name':name,
            'email':email,
            'phonenumber':phonenumber,
        }
        message = '''
        New message from : {}
        Phone Number : {}
        
        From : {}
        '''.format(data['name'], data['phonenumber'] ,data['email'])
        send_mail(data['name'],message, '' , ['syamgopu2001@gmail.com'])
    return render(request,'shop/index.html',{'amountobjects':amountobjects})
