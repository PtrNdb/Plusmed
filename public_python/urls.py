from django.contrib import admin
from django.urls import path, include
from public_python import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('kontakt/', views.kontakt),
    path('', views.glowna),
    path('wozki/', views.wozki),
    path('balkoniki/', views.balkoniki),
    path('sanitarny/', views.sanitarny),
    path('sportowo/', views.sportowo),
    path('szyja/', views.szyja),
    path('kregoslup/', views.kregoslup),
    path('konczynagorna/', views.konczynagorna),
    path('wypozyczalnia/', views.wypozyczalnia),
    path('konczynadolna/', views.konczynadolna),
    path('kompresoterapia/', views.kompresoterapia),
    path('pieluchomajtki/', views.pieluchomajtki),
    path('sprzetmedyczny/', views.sprzetmedyczny),
    path('obuwiemedyczne/', views.obuwiemedyczne),
    
    path('wpisy/', include('wpisy.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

