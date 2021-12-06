from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from .mixins import ValidarPermisosMixin

#Para respaldar y restaurar
import os
from .models import *
from .forms import *

# Create your views here.
'''
    1- dispatch(): valida la peticion y elige que metodo HTTP se utilizo para la solicitud
    2- http_method_not:allowed(): retorna un error cuando se utiliza un metodo HTTP no soportado o definido
    3- options(): para utilizar opciones del view
'''

class Ingreso(LoginView):
    template_name = 'Cremeria_ToscanoApp/login.html'

class Inicio(LoginRequiredMixin, TemplateView):
    template_name = 'Cremeria_ToscanoApp/index.html'

class MostrarProducto(LoginRequiredMixin, ValidarPermisosMixin, ListView):
    permission_required = 'Cremeria_Toscano_1.view_productos'

    model = Productos
    template_name = 'Cremeria_ToscanoApp/mostrar_productos.html'
    context_object_name = 'productos'
    queryset = Productos.objects.all()

    def post(self, request, *args, **kwargs):
        buscar = request.POST['consulta']
        productos = Productos.objects.filter(nombreproducto__contains=buscar)
        return render(request,self.template_name,{"productos":productos})
#Productos
class AgregarProducto(LoginRequiredMixin, ValidarPermisosMixin, CreateView):
    permission_required = 'Cremeria_Toscano_1.add_productos'

    model = Productos
    form_class = ProductosForm
    template_name = 'Cremeria_ToscanoApp/formularios/agregar_producto.html'
    success_url = reverse_lazy('Cremeria_Toscano_1:productos')

class ModificarProducto(LoginRequiredMixin, ValidarPermisosMixin, UpdateView):
    permission_required = 'Cremeria_ToscanoApp.change_productos'

    model = Productos
    form_class = ProductosForm
    template_name = 'Cremeria_ToscanoApp/formularios/modificar_producto.html'
    success_url = reverse_lazy('Cremeria_Toscano_1:productos')

class EliminarProducto(LoginRequiredMixin, ValidarPermisosMixin, DeleteView):
    permission_required = 'Cremeria_Toscano_1.delete_productos'

    model = Productos
    success_url = reverse_lazy('Cremeria_Toscano_1:productos')

#Ventas
class MostrarVenta(LoginRequiredMixin, ValidarPermisosMixin, ListView):
    permission_required = 'Cremeria_Toscano_1.view_ventas'

    model = Ventas
    template_name = 'Cremeria_ToscanoApp/mostrar_ventas.html'
    context_object_name = 'ventas'
    queryset = Ventas.objects.all()

    def post(self, request, *args, **kwargs):
        buscar = request.POST['consulta']
        ventas = Ventas.objects.filter(idventa__contains=buscar)
        return render(request,self.template_name,{"ventas":ventas})

class AgregarVenta(LoginRequiredMixin, ValidarPermisosMixin, CreateView):
    permission_required = 'Cremeria_Toscano_1.add_ventas'

    model = Ventas
    form_class = VentasForm
    template_name = 'Cremeria_ToscanoApp/formularios/agregar_ventas.html'
    success_url = reverse_lazy('Cremeria_Toscano_1:ventas')

class ModificarVenta(LoginRequiredMixin, ValidarPermisosMixin, UpdateView):
    permission_required = 'Cremeria_Toscano_1.change_ventas'

    model = Ventas
    form_class = VentasForm
    template_name = 'Cremeria_ToscanoApp/formularios/modificar_ventas.html'
    success_url = reverse_lazy('Cremeria_Toscano_1:ventas')

class EliminarVenta(LoginRequiredMixin, ValidarPermisosMixin, DeleteView):
    permission_required = 'Cremeria_Toscano_1.delete_ventas'

    model = Ventas
    success_url = reverse_lazy('Cremeria_Toscano_1:ventas')

#Detalle Ventas
class MostrarDetallesVenta(LoginRequiredMixin, ValidarPermisosMixin, ListView):
    permission_required = 'Cremeria_Toscano_1.view_detallesventas'

    model = Detallesventas
    template_name = 'Cremeria_ToscanoApp/mostrar_detallesventas.html'
    context_object_name = 'detallesventas'
    queryset = Detallesventas.objects.all()

    def post(self, request, *args, **kwargs):
        buscar = request.POST['consulta']
        detallesventas = Detallesventas.objects.filter(idventa__idventa__icontains=buscar)
        return render(request,self.template_name,{"detallesventas":detallesventas})

class AgregarDetallesVenta(LoginRequiredMixin, ValidarPermisosMixin, CreateView):
    permission_required = 'Cremeria_Toscano_1.add_detallesventas'

    model = Detallesventas
    form_class = DetallesVentasForm
    template_name = 'Cremeria_ToscanoApp/formularios/agregar_detallesventa.html'
    success_url = reverse_lazy('Cremeria_Toscano_1:detallesventas')

class ModificarDetallesVenta(LoginRequiredMixin, ValidarPermisosMixin, UpdateView):
    permission_required = 'Cremeria_Toscano_1.change_detallesventas'

    model = Detallesventas
    form_class = DetallesVentasForm
    template_name = 'Cremeria_ToscanoApp/formularios/modificar_detallesventa.html'
    success_url = reverse_lazy('Cremeria_Toscano_1:detallesventas')

class EliminarDetallesVenta(LoginRequiredMixin, ValidarPermisosMixin, DeleteView):
    permission_required = 'Cremeria_Toscano_1.delete_detallesventas'

    model = Detallesventas
    success_url = reverse_lazy('Cremeria_Toscano_1:detallesventas')

class RespaldarRestaurar(LoginRequiredMixin, TemplateView):
    template_name = 'Cremeria_ToscanoApp/respaldar_restaurar.html'
    
    def post(self, request, *args, **kwargs):
        accion = request.POST['accion']
        print(accion)
        if accion == "Respaldar":
            os.system('Python manage.py dumpdata --format=json --indent=4 > backup/respaldo_base.json')
        else:
            os.system('Python manage.py loaddata backup/respaldo_base.json')
        return redirect('Cremeria_Toscano_1:index')