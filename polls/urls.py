from django.urls import path
from . import views

# for the namespace
app_name = 'ds_polls'

urlpatterns = [
    # route, view, kwargs, name
    path('', views.index, name='index'),
    path('<int:poll_id>/', views.detail, name='detail'),
    path('<int:poll_id>/results/', views.results, name='results'),
    path('<int:poll_id>/vote/', views.vote, name='vote'),
]