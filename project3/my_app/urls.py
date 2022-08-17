from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('dl/', views.deep_learning, name='deep_learning')
]
