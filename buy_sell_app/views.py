from django.shortcuts import render, HttpResponse
from multiprocessing import AuthenticationError
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db import IntegrityError
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

from .forms import *
# Create your views here.

# def home(request):
#     html = "<html><body>Hello World..!!</body></html>"
#     return HttpResponse(html)

# def home(request):
#     return render(request, 'index.html')


def signnewuser(request):
    if request.method == "POST":
        if request.POST.get('password1')==request.POST.get('password2'):
            try:
                if request.POST.get('checkbox') == "on":
                    saveuser=User.objects.create_user(request.POST.get('username'), password=request.POST.get('password1'),email=request.POST.get('email'),is_staff=True )
                    saveuser.save() 
                else:    
                    saveuser=User.objects.create_user(request.POST.get('username'), password=request.POST.get('password1'),email=request.POST.get('email') )
                    saveuser.save()      
                return render(request, 'authentication-register1.html', { 'info': 'The User ' + request.POST['username'] + ' is saved Successfully..!!'})
        
            except IntegrityError:
                return render(request, 'authentication-register1.html', { 'exist': 'The User '+ request.POST['username'] + ' is already Exist..!!!',})

        else:
            return render(request, 'authentication-register1.html', {'error': 'The Password are not Matching..!'})

    else:
        return render(request, 'authentication-register1.html',)

def loginuser(request):
    if request.method=="POST":
        loginsuccess=authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if loginsuccess is None:
            return render(request, 'authentication-login1.html', {'form':AuthenticationError(), 'error': 'The username or Password are Wrong..!'})
        else:
            if loginsuccess.is_staff == True:
                login(request,loginsuccess)
                return redirect('welcomepage1')  
            else: 
                login(request,loginsuccess)
                return redirect('welcomepage')
    else:
       return render(request, 'authentication-login1.html', {'form':AuthenticationForm()}) 
                
def welcomepage1(request):
    return render(request, 'seller/welcome1.html', {'info': 'Go to the Home List..!!'})

def welcomepage(request):
    return render(request, 'welcome.html', {'info': 'Go to the Home List..!!'})

def logoutpage(request):
    if request.method=="POST":
        logout(request)
        return redirect(loginuser)

#=======================================Product====================================

def add_product(request):
    context = {'submitted' : False}
    id = request.GET.get('id')
    if request.method == 'POST': 
        submitted_form = ProductsForm(request.POST, request.FILES)

        if submitted_form.is_valid():
            submitted_form.cleaned_data['seller'] = id
            submitted_form.save()
            return redirect(welcomepage1)
        
    form = ProductsForm
    if 'submitted' in request.GET:
            submitted = True

    return render(request, 'seller/add_product.html', {'form': form, 'context':context})

def see_products(request):
    item_id = request.GET.get('id')
    id = User.objects.get(id=item_id)
    temp_obj = Products.objects.filter(is_active=True,is_deleted=False, seller = id)
    context = {'products' : temp_obj}
    return render(request, 'seller/see_products.html', context)

def product_list(request):
    # id = request.GET.get('id')
    if request.method == 'POST': 
        # print(request.POST['product_id'],request.POST['buyer'],request.POST['seller'],'------request.POST----')
        submitted_form = CartForm(request.POST)

        if submitted_form.is_valid():
            submitted_form.save()

    temp_obj = Products.objects.filter(is_active=True,is_deleted=False).order_by('-id')
    context = {'products' : temp_obj}
    return render(request, 's_list.html', context)

def product_cart(request):
    item_id = request.GET.get('id')
    id = User.objects.get(id=item_id)
    if request.method == 'POST': 
        cart_id = int(request.POST['cart_id'])
        Cart.objects.filter(buyer=id, id= cart_id).update(is_active=False,is_deleted=True)
        temp_obj = Cart.objects.filter(is_active=True,is_deleted=False, buyer = id)
        context = {'cart' : temp_obj}
        return render(request, 's_cart.html', context)
    else:
        pass
    temp_obj = Cart.objects.filter(is_active=True,is_deleted=False, buyer = id)
    context = {'cart' : temp_obj}
    return render(request, 's_cart.html', context)