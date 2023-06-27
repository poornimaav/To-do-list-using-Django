from django.urls import path
from . import views
from .views import index
from .views import delete

urlpatterns = [

    path('', views.index, name="list"),
    path('create/', views.create, name="create"),
    path('view/<str:pk>', views.view, name="view"),
    path('update/<str:pk>/', views.update, name="update"),
    path('delete/<str:pk>/', views.delete, name="delete"),

]

