from django.urls import path

from . import views

urlpatterns = [
    path("", views.PetListCreateView.as_view(), name='pet-list'),
    path("<int:pk>/", views.PetRetrieveUpdateDeleteView.as_view(), name='pet-detail')
]
