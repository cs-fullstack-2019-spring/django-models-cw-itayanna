#importing path and veiws functions

from django.urls import path
from . import views

#linking routes for server

urlpatterns = [
    path("", views.index, name="index"),
]