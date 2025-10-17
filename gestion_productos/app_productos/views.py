from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import permission_required
from django.views.generic import TemplateView
from .models import CustomUser, Producto
from .forms import ProductoForm, CustomUserCreationForm
from .mixins import CustomLoginRequiredMixin, CustomPermissionRequiredMixin, ProtectedTemplateView, PermissionProtectedTemplateView

class IndexView(TemplateView):
    template_name = 'index.html'

def RegisterView(request):
    from django.contrib.auth.models import Group
    
    # Creamos una clase inline que use CustomUser
    class CustomUserCreationForm(UserCreationForm):
        class Meta:
            model = CustomUser
            fields = ('username', 'email', 'first_name', 'last_name')

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            # Asignar grupo según la selección del usuario
            group_name = request.POST.get('group')
            if group_name:
                try:
                    group = Group.objects.get(name=group_name)
                    user.groups.add(group)
                except Group.DoesNotExist:
                    # Si el grupo no existe, asignar permisos básicos
                    pass
            
            login(request, user)
            return redirect('index')
    else:
        form = CustomUserCreationForm()
    
    # Obtener grupos disponibles para mostrar en el template
    groups = Group.objects.all()
    
    return render(request, 'register.html', {'form': form, 'groups': groups})

class LoginView(TemplateView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        return render(request, self.template_name, {
            'error': 'Usuario o contraseña incorrectos.',
            'username': username  # opcional, para mantenerlo en el form
        })

def LogoutView(request):
    logout(request)
    return render(request, 'logout.html')

class ProductoListView(PermissionProtectedTemplateView):
    template_name = 'producto_list.html'
    permission_required = 'app_productos.view_producto'
    

    def get(self, request, *args, **kwargs):
        productos = Producto.objects.all()
        return render(request, self.template_name, {'productos': productos})

class ProductoAddView(PermissionProtectedTemplateView):
    template_name = 'producto_add.html'
    permission_required = 'app_productos.add_producto'

    def get(self, request, *args, **kwargs):
        form = ProductoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
        return render(request, self.template_name, {'form': form})

class ProductoUpdateView(PermissionProtectedTemplateView):
    template_name = 'producto_update.html'
    permission_required = 'app_productos.change_producto'

    def get(self, request, pk, *args, **kwargs):
        producto = Producto.objects.get(pk=pk)
        form = ProductoForm(instance=producto)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk, *args, **kwargs):
        producto = Producto.objects.get(pk=pk)
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('producto_list')
        return render(request, self.template_name, {'form': form})

class ProductoDeleteView(PermissionProtectedTemplateView):
    template_name = 'producto_delete.html'
    permission_required = 'app_productos.delete_producto'

    def get(self, request, pk, *args, **kwargs):
        producto = Producto.objects.get(pk=pk)
        return render(request, self.template_name, {'producto': producto})

    def post(self, request, pk, *args, **kwargs):
        producto = Producto.objects.get(pk=pk)
        producto.delete()
        return redirect('producto_list')

def handler403(request, exception=None):
    """Manejador personalizado para errores 403 (Permiso denegado)"""
    return render(request, '403.html', status=403)


def handler404(request, exception=None):
    """Manejador personalizado para errores 404 (Página no encontrada)"""
    return render(request, '404.html', status=404)