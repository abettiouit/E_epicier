from django.shortcuts import render, redirect  
from clients.forms import ClientForm
from clients.models import Client
from credits.models import Credit
from django.db.models import Sum
# Create your views here.
def clients(request): 
    print("admin ")
    print(request.session['user_id'])
    if request.session['user_id']==None:
          return redirect('/admin/login')
    admin=request.session['user_id']

    if request.method == "POST":  
        form = ClientForm(request.POST)  
        formcopy = ClientForm(request.POST.copy())
        formcopy.data['admin']=admin
        if formcopy.is_valid():  
            try:  
                formcopy.save()  
                return redirect('/clients/show')  
            except:  
                pass  
    else:  
        form = ClientForm()  
   
    return render(request,'index.html',{'form':form,"pageClient":"sideBarItemActive"})  
def show(request):
    if request.session['user_id']==None:
         return  redirect('/admin/login')
    admin=request.session['user_id']  
    clients = Client.objects.filter(admin_id=admin) 
    return render(request,"show.html",{'clients':clients,"pageClient":"sideBarItemActive","showClient":"sideBarItemActive"})  
def search(request): 
    if request.session['user_id']==None:
         return redirect('/admin/login')
    admin=request.session['user_id']   
    name=request.GET.get('name')
    clients = Client.objects.filter(name__contains=name,admin_id=admin) 
    return render(request,"show.html",{'clients':clients,"pageClient":"sideBarItemActive","showClient":"sideBarItemActive","search":name})  
def edit(request, id):
    if request.session['user_id']==None:
         return redirect('/admin/login')   
    client = Client.objects.get(id=id)  
    return render(request,'edit.html', {'client':client,"pageClient":"sideBarItemActive"})  
def update(request, id):  
    if request.session['user_id']==None:
         return redirect('/admin/login')
    client = Client.objects.get(id=id)  
    admin=request.session['user_id']  
    formcopy = ClientForm(request.POST.copy(),instance = client)
    formcopy.data['admin']=admin
    if formcopy.is_valid():  
        formcopy.save()  
        return redirect("/clients/show")  
    return render(request, 'edit.html', {'client': client,"pageClient":"sideBarItemActive"})  
def destroy(request, id):  
    if request.session['user_id']==None:
          redirect('/admin/login')
    client = Client.objects.get(id=id)  
    client.delete()  
    return redirect("/clients/show")