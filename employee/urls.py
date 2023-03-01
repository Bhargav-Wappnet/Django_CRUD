from django.contrib import admin  
from django.urls import path  
from employee import views 


urlpatterns = [
        path('', views.emply),  
        path('display', views.display),  
        path('edit/<int:id>', views.edit),  
        path('update/<int:id>', views.update),  
        path('delete/<int:id>', views.destroy),  
    ]
