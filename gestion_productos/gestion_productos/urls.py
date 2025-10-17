"""
URL configuration for gestion_productos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from app_productos.views import IndexView, RegisterView, LoginView, LogoutView, ProductoListView, ProductoAddView, ProductoUpdateView, ProductoDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView, name='logout'),
    path('register/', RegisterView, name='register'),
    path('productos/', ProductoListView.as_view(), name='productos'),
    path('crear_producto/', ProductoAddView.as_view(), name='crear_producto'),
    path('editar_producto/<int:pk>', ProductoUpdateView.as_view(), name='editar_producto'),
    path('borrar_producto/<int:pk>', ProductoDeleteView.as_view(), name='borrar_producto'),
]
