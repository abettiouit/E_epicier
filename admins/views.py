from django.shortcuts import redirect, render
from admins.forms import AdminsForm
from admins.models import Admin

def register(request):
    if request.method == "POST":  
        form = AdminsForm(request.POST) 
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/admin/login')  
            except:  
                pass   
    return render(request,'register.html',)

def show(request):
      
      if request.session['user_id']==None:
         return redirect('/admin/login')
      admin=request.session['user_id']


      return redirect('/clients')
                  
    
def login(request):
     if request.method == "POST": 
      form = AdminsForm(request.POST)  
      email=form.data['email']
      password=form.data['password']
      admin=Admin.objects.filter(email=email)
      if len(admin)==0:
          return render(request,"login.html",{"err":"email ou password incorrect"})
      if admin[0].password==password:
          request.session['user_id']=admin[0].id
          request.session['user_name']=admin[0].name
          request.session['user_email']=admin[0].email
          return redirect('/clients')
      else:
          return render(request,"login.html",{"err":"email ou password incorrect"})
        
     else:
         return render(request,"login.html")
def logout(request):
    request.session['user_id']=None
    request.session['user_name']=None
    request.session['user_email']=None
    return redirect('/admin/login')
         
    