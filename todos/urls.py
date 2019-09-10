from django.urls import path
from todos import views

app_name = "toods"

urlpatterns = [
    path('', views.index, name="index"),
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('edit/<int:pk>/', views.edit, name="edit"),
    path('update/<int:pk>/', views.update, name="updates"),
]