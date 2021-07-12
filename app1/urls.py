from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page.as_view(), name="starting-page"),
    path("posts/", views.posts, name="all-posts"),
    path("posts/favorite", views.AddFavorite.as_view(), name="favorite"),
    path("posts/<slug:post_slug>", views.post_detail, name="selected-post"),
    path("addpost/", views.AddPost.as_view() , name='addpost'),
    path("comment/",views.CommentView.as_view(), name="comment"),
    path("posts/favoritepost/",views.FavoritePost.as_view(), name="favoriteposts"),
]