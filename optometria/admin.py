from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Role, TipoDocumento, Paciente, Turno, HistorialMedico, Producto, Pedido

# Register your models here.

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class RoleInline(admin.StackedInline):
    model = Role
    can_delete = False
    verbose_name_plural = 'Rol'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (RoleInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(TipoDocumento)
admin.site.register(Paciente)
admin.site.register(Turno)
admin.site.register(HistorialMedico)
admin.site.register(Producto)
admin.site.register(Pedido)
