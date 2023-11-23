from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.main),
    path('list/', views.list, name="list"),
    path('detail/<int:id>/', views.detail, name="detail")   
]

