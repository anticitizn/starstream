
from django.contrib import admin
from django.urls import path, include
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.FileUploadView.as_view()),
    path('download/', views.FileDownloadView.as_view()),
    path('getmetadata/', views.GetMetadataView.as_view()),
    path('setmetadata/', views.SetMetadataView.as_view()),
    path('search/', views.SearchView.as_view()),
    path('getimage/', views.GetImageView.as_view())
]
