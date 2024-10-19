from django.urls import path

from . import views

app_name = "robot"

urlpatterns = [
    path("", views.index, name="index"),
    path("client", views.client, name="client"),
    path("create", views.create, name="create"),
    # path("result/<int:id>", views.result, name="result"),
]
