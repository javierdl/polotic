from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Role, TipoDocumento, Paciente, Turno, HistorialMedico, Producto, Pedido

# Register your models here.
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('username', 'email', 'first_name', 'last_name', 'role')
# UserAdmin.list_display = ('email', 'first_name', 'last_name', 'is_active', 'date_joined', 'is_staff', 'role')

    
# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class RoleInline(admin.StackedInline):
    model = Role
    can_delete = False
    verbose_name_plural = 'Rol'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (RoleInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'rol', 'is_active', 'is_staff')
    
    def rol(self, obj):
        return Role.ROLE_CHOICES[obj.role.role-1][1]


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Role)
admin.site.register(TipoDocumento)
admin.site.register(Paciente)
admin.site.register(Turno)
admin.site.register(HistorialMedico)
admin.site.register(Producto)
admin.site.register(Pedido)

