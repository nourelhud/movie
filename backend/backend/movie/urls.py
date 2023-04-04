from django.urls import path
from .views import *

urlpatterns = [
    path('login/',login_view , name='login'),
    path('signup/', SignupView.as_view(), name='signup'),
    # User URLs
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/create/', UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user_delete'),

    # Post URLs
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/create/<int:user_id>', PostCreateView.as_view(), name='post_create'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

    # Comment URLs
    path('comments/', CommentListView.as_view(), name='comment_list'),
    path('comments/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('posts/<int:post>/comments/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
    path('users/<int:userid>/posts/<int:postid>/comments/create/', UserCommentCreateView.as_view(), name='user_comment_create'),
    path('posts/<int:post>/comments/', CommentdetailView.as_view(), name='post_comments'),

    # Movie URLs
    path('movies/', MovieListGet.as_view(), name='movie_list'),
    path('movies/create/', MovieListCreate.as_view(), name='movie_create'),
    path('movies/<int:pk>/', MovieDetailGet.as_view(), name='movie_detail'),
    path('movies/<int:pk>/update/', MovieDetailUpdate.as_view(), name='movie_update'),
    path('movies/<int:pk>/delete/', MovieDetailDelete.as_view(), name='movie_delete'),

    # Admin Movie URLs
    path('admin/movies/', AdminMovieListGet.as_view(), name='admin_movie_list'),
    path('admin/movies/create/', AdminMovieListCreate.as_view(), name='admin_movie_create'),
]