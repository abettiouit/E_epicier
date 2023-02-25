from django.shortcuts import render, redirect  
from products.forms import ProductForm
from products.models import Product


def products(request):  
    #check if admin conected
    if request.session['user_id']==None:
         return redirect('/admin/login')
    # get id of admin
    admin=request.session['user_id']
    #if methdod post should insert product in database
    if request.method == "POST":  
        form = ProductForm(request.POST)  
        formcopy = ProductForm(request.POST.copy())
        formcopy.data['admin']=admin
        if formcopy.is_valid():  
            try:  
                formcopy.save()  
                return redirect('/product/show')  
            except:  
                pass  
    else: 
    # if method get show form add product 
        form = ProductForm()  
    return render(request,'product_index.html',{'form':form,"pageProduct":"sideBarItemActive"})  
def show(request): 
    if request.session['user_id']==None:
         return redirect('/admin/login')
    admin=request.session['user_id'] 
    products = Product.objects.filter(admin_id=admin)  
    return render(request,"product_show.html",{'products':products,"pageProduct":"sideBarItemActive","showProduct":"sideBarItemActive"})  

def search(request):
    if request.session['user_id']==None:
         return redirect('/admin/login')
    admin=request.session['user_id']
    name=request.GET.get('name')
    products = Product.objects.filter(name__contains=name,admin_id=admin)
    return render(request,"product_show.html",{'products':products,"pageProduct":"sideBarItemActive","showProduct":"sideBarItemActive","search":name})  
def edit(request, id):  
    if request.session['user_id']==None:
          return redirect('/admin/login')
    admin=request.session['user_id']
    product = Product.objects.get(id=id,admin_id=admin)  
    return render(request,'product_edit.html', {'product':product,"pageProduct":"sideBarItemActive"})  
def update(request, id):  
    if request.session['user_id']==None:
         return redirect('/admin/login')
    admin=request.session['user_id']
    product = Product.objects.get(id=id,admin_id=admin)  
    form = ProductForm(request.POST.copy(), instance = product)  
    form.data['admin']=admin
    if form.is_valid():  
        form.save()  
        return redirect("/product/show")  
    return render(request, 'product_edit.html', {'product': product,"pageProduct":"sideBarItemActive"})  
def destroy(request, id):  
    if request.session['user_id']==None:
          return redirect('/admin/login')
    product = Product.objects.get(id=id)  
    product.delete()  
    return redirect("/product/show")