from django.urls import path
from upload import views

urlpattenrs = [
    path('', views.FileUploadView),
]