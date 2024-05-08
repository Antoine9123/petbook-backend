from django.urls import path

from . import views


urlpatterns = [
    path("", views.pet_list, name='pet-list'),
    path("<int:id>/", views.pet_detail, name='pet-detail')
]