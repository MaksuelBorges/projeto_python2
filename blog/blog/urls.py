from django.contrib import admin
from django.urls import path
from myapp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('entrar/', views.entrar),
    path('cadastro/', views.cadastro),
    path('consulta/', views.consulta),
    path('login/', views.login),
    path('logout/', views.logout),
    path('userspace/', views.userspace),
    path('publicate/', views.publicate, name="publicate"),
    path('blogpost', views.blogpost_page),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)