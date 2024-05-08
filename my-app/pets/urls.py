from django.urls import path

from . import views


urlpatterns = [
    path("", views.pet_list),
    path("<int:id>/", views.pet_detail)
]