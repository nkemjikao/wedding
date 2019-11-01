from django.contrib import admin
from django.urls import path
from wedding import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('trad',views.trad,name='trad'),
    path('media',views.media,name='media'),
    
    path('trad_gallery',views.trad_gallery,name='tradgallery'),
    path('white_gallery',views.white_gallery,name='whitegallery'),
]
