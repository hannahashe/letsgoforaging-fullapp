from django.urls import path
from . import views

urlpatterns = [

    path("", views.workshop_list, name="workshop_list"),

    path(
        "<slug:slug>/",
        views.workshop_detail,
        name="workshop_detail"
    ),
]
