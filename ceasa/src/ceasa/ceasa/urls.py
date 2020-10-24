"""ceasa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from ceasa.views import login_view, changepassword_view, logout_view
from escola.views import schoollist_view, schoolcreate_view, schooledit_view, schooldelete_view
from usuario.views import userlist_view, usercreate_view, useredit_view, userdelete_view

urlpatterns = [
    path('ceasa/', admin.site.urls),

    path('', login_view, name='login'),
    path('trocarsenha/', changepassword_view, name='changepassword'),
    path('sair/', logout_view, name='logout'),

    path('escolas/', schoollist_view, name='schoollist'),
    path('escolas/formulario/', schoolcreate_view, name='schoolcreate'),
    path('escolas/formulario/<int:id>/', schooledit_view, name='schooledit'),
    path('escolas/excluir/<int:id>/', schooldelete_view, name='schooldelete'),

    path('usuarios/', userlist_view, name='userlist'),
    path('usuarios/formulario/', usercreate_view, name='usercreate'),
    path('usuarios/formulario/<int:id>/', useredit_view, name='useredit'),
    path('usuarios/excluir/<int:id>/', userdelete_view, name='userdelete'),

    re_path(r'^media/(?P<path>.*)$', serve, { 'document_root': settings.MEDIA_ROOT }),
    re_path(r'^static/(?P<path>.*)$', serve, { 'document_root': settings.STATIC_ROOT }),
]

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
