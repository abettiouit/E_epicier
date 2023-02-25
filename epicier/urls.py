
from django.contrib import admin
from django.urls import include, path
from products import views as productView
from clients import views as clientView
from credits import views as creditView
from admins import views as adminView
urlpatterns = [
    path('admin/login/', adminView.login),  
    path('admin/logout/', adminView.logout),  
    path('admin/register/', adminView.register),  


    path('product/', productView.products),  
    path('product/show',productView.show),  
    path('product/search',productView.search),  
    path('product/edit/<int:id>', productView.edit),  
    path('product/update/<int:id>', productView.update),  
    path('product/delete/<int:id>', productView.destroy), 

    path('clients/', clientView.clients),  
    path('clients/show',clientView.show),  
    path('clients/search',clientView.search),  
    path('clients/edit/<int:id>', clientView.edit),  
    path('clients/update/<int:id>', clientView.update),  
    path('clients/delete/<int:id>', clientView.destroy), 

    path('accounts/profile/',adminView.show),
    path('',adminView.show),
    
    path('credits/', creditView.credits),  
    path('credits/show',creditView.show),  
    path('credits/edit/<int:id>', creditView.edit),  
    path('credits/update/<int:id>', creditView.update),  
    path('credits/delete/<int:id>', creditView.destroy),
    path('credits/paye/<int:id>', creditView.paye),
    path('credits/search', creditView.searchClient),
    

]
