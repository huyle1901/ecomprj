from django.urls import path
from core.views import index  # Import trực tiếp hàm index

app_name = "core"

urlpatterns = [
    path('', index),  # Sử dụng index trực tiếp
]