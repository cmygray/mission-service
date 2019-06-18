from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:poll_id>/', views.detail, name='detail'),
    path('<int:poll_id>/choices/', views.choices, name='detail.choices'),
]
