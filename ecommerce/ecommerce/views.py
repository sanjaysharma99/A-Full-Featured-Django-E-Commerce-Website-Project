from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from mydata.models import Products, Categories, Carts
from django.http import HttpResponse


def home(request):
    products=Products.objects.all()
    categories=Categories.objects.all()
    return render(request,'home.html',{'products':products,'categories':categories})

def signup_page(request):
    categories=Categories.objects.all()
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            email=request.POST.get('email')
            password=request.POST.get('password')

            user=User.objects.filter(username=username)

            if user.exists():
                messages.info(request,'Username Already Exists')
                return redirect('/signup/')
            
            user=User.objects.create(username=username,email=email)
            user.set_password(password)
            user.save()

            messages.info(request,'Account Created Successfully')
            return redirect('/signup/')
        
        return render(request,'signup.html',{'categories':categories})
    

def login_page(request):
    categories=Categories.objects.all()
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method=='POST':
            username=request.POST.get('username')
            password=request.POST.get('password')

            if not User.objects.filter(username=username).exists():
                messages.info(request,'Account Not Found')
                return redirect('/login/')
            
            user=authenticate(username=username,password=password)

            if user is None:
                messages.info(request,'Invalid Information')
                return redirect('/login/')
            else:
                login(request,user)
                return redirect('/')
        
        return render(request,'login.html',{'categories':categories})

def logout_page(request):
    logout(request)
    return redirect('/login/')

def category(request,category_url):
    category_name=Categories.objects.get(category_slug=category_url)
    category_product=Products.objects.filter(product_category=category_url)

    categories=Categories.objects.all()
    return render(request,'category.html',{'category':category_product,'categories':categories})

def product(request,product_url):
    categories=Categories.objects.all()
    data=Products.objects.get(product_slug=product_url)
    data={'data':data,'categories':categories}

    if request.method=='POST':
        product_name=request.POST.get('product_name')
        qty=request.POST.get('qty')
        username=request.user.username

        r1=Carts.objects.filter(cart_username=username)
        if r1.exists():
            for product in r1:
                if product.cart_product_name==product_name:
                    product.cart_product_qty=qty
                    product.save()
                    return redirect(f'/product/{product_url}')
            
            new_product=Carts(cart_username=username,cart_product_name=product_name,cart_product_qty=qty)

            new_product.save()
            
            return redirect(f'/product/{product_url}')
        
        else:   
            new_product=Carts(cart_username=username,cart_product_name=product_name,cart_product_qty=qty)
            new_product.save()
            
            return redirect(f'/product/{product_url}')
        
    return render(request,'product.html',data)

@login_required(login_url='/login/')
def cart(request):
    categories=Categories.objects.all()
    username=request.user.username
    data=Carts.objects.filter(cart_username=username)
    
    mydata={}

    for cart_product in data:
         mydata[cart_product]=Products.objects.get(product_name=cart_product.cart_product_name)

        
    return render(request,'cart.html',{'mydict':mydata,'categories':categories})

@login_required(login_url='/login/')
def update_cart_product(request):
    if request.method=='POST':
        username=request.user.username
        product_name=request.POST.get('update_cart_product')
        product_qty=request.POST.get('qty')

        cart_data=Carts.objects.filter(cart_username=username,cart_product_name=product_name)
        for product in cart_data:
            if product.cart_product_name==product_name:
                product.cart_product_qty=product_qty
                product.save()

        return redirect('/cart/')

@login_required(login_url='/login/')    
def delete_cart_product(request):
    if request.method=='POST':
        username=request.user.username
        product_name=request.POST.get('delete_cart_product')

        cart_data=Carts.objects.filter(cart_username=username,cart_product_name=product_name)
        for product in cart_data:
            if product.cart_product_name==product_name:
                product.delete()

        return redirect('/cart/')

@login_required(login_url='/login/') 
def checkout(request):
    categories=Categories.objects.all()
    total_price=0
    username=request.user.username

    cart_products=Carts.objects.filter(cart_username=username)
    for product in cart_products:
        product_main_data=Products.objects.get(product_name=product.cart_product_name)
        sub_total=product.cart_product_qty*product_main_data.product_pric
        total_price=total_price+sub_total

    return render(request,'checkout.html',{'categories':categories,'total_price':total_price})

@login_required(login_url='/login/')
def order(request):
    categories=Categories.objects.all()
    return render(request,'order_placed.html',{'categories':categories})

@login_required(login_url='/login')
def delete_account(request):
    username=request.user.username
    User.objects.get(username=username).delete()
    return redirect('/signup')