from django.contrib import admin
from .models import Departamentos

@admin.register(Departamentos)
class DepartamentosAdmin(admin.ModelAdmin):
	model = Departamentos

# Register your models here.
