from django.urls import path

from telugu.views import home
urlpatterns = [
    path('',home),
]
