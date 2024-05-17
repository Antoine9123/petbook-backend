from django.urls import path

from . import views

urlpatterns = [
    path("", views.PostListCreateView.as_view(), name='post-list'),
    path("<int:pk>/", views.PostRetrieveUpdateDeleteView.as_view(), name='post-detail'),
    # path("get-post-from/<id>/", views.ListPetForOwner.as_view(), name='get-user-pets'),

]
