from django.urls import path

from . import views

urlpatterns = [
    path("user/<int:user_id>/", views.UserFollowListView.as_view(), name='user-follow-list'),
    path("add/", views.FollowCreateView.as_view(), name='follow-create'),
    path("delete/", views.FollowDeleteView.as_view(), name='follow-delete'),
]