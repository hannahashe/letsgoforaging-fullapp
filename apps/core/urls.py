from django.urls import path
from .views import home
from apps.core import views

urlpatterns = [
    path("", home, name="home"),
    path("tag/<slug:slug>/", views.tag_page, name="tag_page"),
]

