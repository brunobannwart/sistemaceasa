from django.contrib import admin
from .models import Usuario

# Register your models here.
admin.site.site_header = 'Administrativo'
admin.site.site_title = 'CEASA'
admin.site.index_title = 'Gerenciamento do CEASA'

admin.site.register(Usuario)