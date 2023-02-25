from django.shortcuts import render, redirect
from clients.models import Client  
from credits.forms import CreditForm
from credits.models import Credit
from products.models import Product

# Create your views here.
def credits(request): 
    if request.session['user_id']==None:
         
          return redirect('/admin/login')
    admin=request.session['user_id'] 
    if request.method == "POST":  
        form = CreditForm(request.POST)  
        formcopy = CreditForm(request.POST.copy())
        product=Product.objects.get(id=formcopy.data["product"])
        formcopy.data["price"]=product.price
        formcopy.data["total"]=formcopy.data["price"]*float(formcopy.data["quantite"])
        formcopy.data["admin"]=admin
        
        product.quantite=product.quantite-float(formcopy.data["quantite"])
        
        if formcopy.is_valid():
            try:  
                formcopy.save()  
                product.save()
                return redirect('/credits/show')  
            except Exception as e:  
                print(e)
        else:
            print(form.errors)      

    else:  
        form = CreditForm() 
    products=Product.objects.filter(admin_id=admin)
    clients=Client.objects.filter(admin_id=admin)
    return render(request,'credit_index.html',{'form':form,'products':products,'clients':clients,"pageCredit":"sideBarItemActive"})  
def show(request):  
    if request.session['user_id']==None:
          return redirect('/admin/login')
    admin=request.session['user_id'] 
    credits = Credit.objects.filter(admin_id=admin)  
    clients=Client.objects.filter(admin_id=admin) 
    return render(request,"credit_show.html",{'credits':credits,"pageCredit":"sideBarItemActive","showCredit":"sideBarItemActive","clients":clients})  

def searchClient(request):  
    if request.session['user_id']==None:
          return redirect('/admin/login')
    admin=request.session['user_id'] 
    clients=Client.objects.filter(admin_id=admin)
    name=request.GET.get('name')
    credits = Credit.objects.filter(admin_id=admin,client__name__contains=name)
    return render(request,"credit_show.html",{'credits':credits,"pageCredit":"sideBarItemActive","showCredit":"sideBarItemActive","clients":clients,"search":name})
def edit(request, id):  
    if request.session['user_id']==None:
          return redirect('/admin/login')
    admin=request.session['user_id'] 
    products=Product.objects.filter(admin_id=admin)
    clients=Client.objects.filter(admin_id=admin) 
    credit = Credit.objects.get(id=id,)  
    return render(request,'credit_edit.html', {'credit':credit,'products':products,'clients':clients,"pageCredit":"sideBarItemActive"})  
def update(request, id):  
    if request.session['user_id']==None:
          return redirect('/admin/login')
    admin=request.session['user_id'] 
    credit = Credit.objects.get(id=id)   
    formcopy = CreditForm(request.POST.copy(),instance = credit)
    formcopy.data["price"]=Product.objects.get(id=formcopy.data["product"]).price
    formcopy.data["total"]=formcopy.data["price"]*float(formcopy.data["quantite"])
    formcopy.data["admin"]=admin
    if formcopy.is_valid():  
        formcopy.save()  
        return redirect("/credits/show")  
    return render(request, 'credit_edit.html', {'credit': credit,"pageCredit":"sideBarItemActive"})  
def destroy(request, id):  
    if request.session['user_id']==None:
         return  redirect('/admin/login')
    
    credit = Credit.objects.get(id=id)  
    credit.delete()  
    return redirect("/credits/show")
def paye(request, id):  
    if request.session['user_id']==None:
         return  redirect('/admin/login')
    
    credit = Credit.objects.get(id=id)  
    credit.etat=True
    credit.save()
    return redirect("/credits/show")