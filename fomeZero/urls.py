from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.shortcuts import redirect
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls')),
    path('cliente/', include('cliente.urls')),
    path('voluntario/', include('voluntario.urls')),
    path('', lambda request: redirect('/cliente/home'))
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
