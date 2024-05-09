from django.urls import path

from . import views

urlpatterns = [
    path("", views.PetListCreateView.as_view(), name='pet-list'),
    path("<int:pk>/", views.PetRetrieveUpdateDeleteView.as_view(), name='pet-detail'),
    path("current-user/",views.get_pets_for_current_user, name='current-user' )
]
