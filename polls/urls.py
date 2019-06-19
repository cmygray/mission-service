from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:poll_id>/', views.detail, name='detail'),
    path('<int:poll_id>/actions/vote/', views.vote, name='actions.vote')
]
