from django.urls import path
from .views import PostsList, PostDetail, PostCreate, PostSearch, PostUpdate, PostDelete

urlpatterns = [
    path("", PostsList.as_view(), name='post_list'),
    path("<int:pk>", PostDetail.as_view()),
    path('create/', PostCreate.as_view()),
    path('search/', PostSearch.as_view()),
    path("<int:pk>/update/", PostUpdate.as_view()),
    path("<int:pk>/delete/", PostDelete.as_view()),
]