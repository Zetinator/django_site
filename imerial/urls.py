from django.urls import path

from . import views

app_name = 'imerial'
urlpatterns = [
    path('', views.index, name='index'),
    path('servicios', views.servicios, name='servicios'),
    path('productos', views.productos, name='productos'),
    path('detail_coccion', views.detail_coccion, name='detail_coccion'),
    path('detail_refrigeracion', views.detail_refrigeracion, name='detail_refrigeracion'),
    path('detail_aceros', views.detail_aceros, name='detail_aceros'),
    path('detail_electricos', views.detail_electricos, name='detail_electricos'),
]
