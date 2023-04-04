from django.shortcuts import get_object_or_404
from django.views import View
from django.http import JsonResponse
import json
from rest_framework import permissions, generics
from rest_framework.response import Response
from .models import Users, Post, Comment, Movies
from .serializers import MovieSerializer, UserSerializer, PostSerializer, CommentSerializer
from django.views.decorators.csrf import csrf_exempt


class SignupView(View):
    @csrf_exempt
    def dispatch(self, request, args, **kwargs):
        return super().dispatch(request,args, kwargs)

    def post(self, request, *args, kwargs):
        data = json.loads(request.body)
        # process the sign-up data and save it to the database return a JSON response indicating success or failure
        return JsonResponse({'status': 'success'})

    def get(self, request, *args, **kwargs):
        return JsonResponse({'status': 'error'})


@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data['name']
        password = data['password']
        users = Users.objects.filter(name=name,password=password)
        print(users)
        if users.exists():
            user = users.first()
            print(user.password)
            return JsonResponse({'success': True,"user_id":user.id})
        else:
            return JsonResponse({'success': False, 'error': 'User not found'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})

# ============================= User ================================

class UserListView(generics.ListAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()

class UserUpdateView(generics.UpdateAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def perform_update(self, serializer):
        serializer.save()

class UserDeleteView(generics.DestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UserSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'User deleted successfully'})


# ============================= Post ================================
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostCreateView(generics.CreateAPIView):
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        user_id = self.kwargs['user_id']
        user = Users.objects.get(pk=user_id)

        post = Post.objects.create(
            user=user,
            title=serializer.validated_data.get('title'),
            content=serializer.validated_data.get('content')
        )
        serializer = PostSerializer(post)
        return Response(serializer.data)


class PostUpdateView(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_update(self, serializer):
        serializer.save()

class PostDeleteView(generics.DestroyAPIView):
    queryset = Post.objects.all()

    def delete(self, request, *args, **kwargs):
        post = self.get_object()
        if post.user != request.user:
            return Response({'error': 'You are not authorized to delete this post'})
        post.delete()
        return Response({'message': 'Post deleted successfully'})


# ============================= Comment ================================

class CommentListView(generics.ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentUpdateView(generics.UpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_update(self, serializer):
        serializer.save()

class CommentDeleteView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def delete(self, request, *args, **kwargs):
        comment = self.get_object()
        if comment.user != request.user:
            return Response({'error': 'You are not authorized to delete this comment'})
        comment.delete()
        return Response({'message': 'Comment deleted successfully'})

class CommentdetailView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['post']
        return Comment.objects.filter(post=post_id)
    
# ============================= Movie ================================

class MovieListGet(generics.ListAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer


class MovieListCreate(generics.CreateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class MovieDetailGet(generics.RetrieveAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer


class MovieDetailUpdate(generics.UpdateAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

    def get_object(self):
        return get_object_or_404(Movies, pk=self.kwargs['pk'], user=self.request.user)


class MovieDetailDelete(generics.DestroyAPIView):
    queryset = Movies.objects.all()
    serializer_class = MovieSerializer

    def get_object(self):
        return get_object_or_404(Movies, pk=self.kwargs['pk'], user=self.request.user)
    
    
class UserCommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    
    def perform_create(self, serializer):
        user_id = self.kwargs['userid']
        user = Users.objects.get(pk=user_id)
        post_id = self.kwargs['postid']
        post= Post.objects.get(pk=post_id)
        print(user,post)
        comment = Comment.objects.create(
            user=user,
            post=post,
            content=serializer.validated_data.get('content')
        )
        serializer = CommentSerializer(comment)


# ============================= Admin ================================

class AdminMovieListGet(generics.ListAPIView):
    queryset = Movies.objects.filter(admin_post=True)
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAdminUser]


class AdminMovieListCreate(generics.CreateAPIView):
    queryset = Movies.objects.filter(admin_post=True)
    serializer_class = MovieSerializer
    permission_classes = [permissions.IsAdminUser]



