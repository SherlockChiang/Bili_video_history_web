from django.urls import path
from . import views
urlpatterns = [
    path('/', views.index),   # views.index 对应 index目录下的views.py里面的index视图函数
]