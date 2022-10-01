"""HospitalHome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from HospitalHomeBE import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', views.UsuarioListView.as_view()),  
    path('user/<int:pk>/', views.UsuarioRetrieveUpdateDeleteView.as_view()),  
    path('medico/', views.MedicoListCreateView.as_view()),  
    path('medico/<int:pk>/', views.MedicoRetrieveUpdateView.as_view()),
    path('paciente/', views.createpaciente),
    path('paciente/<int:pk>/', views.detailpaciente),
    path('userlogin/', views.usercreateview.as_view()),
    path ('familiar/', views.FamiliarListCreateView.as_view()),
    path('familiar/<int:pk>/', views.FamiliarRetrieveUpdateView.as_view()),
    path ('enfermero/', views.EnfermeroListCreateView.as_view()),
    path('enfermero/<int:pk>/', views.EnfermeroRetrieveUpdateView.as_view()),
    path('historia/<int:pk>/', views.HistoriaRetrieveUpdateView.as_view()),
    path ('rol/', views.RolListCreateView.as_view()),
    path('rol/<int:pk>/', views.RolRetrieveDestroyView.as_view()),
]