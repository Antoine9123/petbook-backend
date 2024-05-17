from django.urls import path

from . import views

urlpatterns = [
    path("", views.PostListCreateView.as_view(), name='post-list'),
    path("<int:pk>/", views.PostRetrieveUpdateDeleteView.as_view(), name='post-detail'),
    path("get-post-from/<int:pet_id>/", views.ListPostForPet.as_view(), name='get-pet-posts'),
    path("get-post-by/<str:category>/", views.ListPostForCategory.as_view(), name='get-category-posts')

]
