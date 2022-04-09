from django.shortcuts import render, redirect
from rest_framework import generics, mixins, permissions, viewsets
from .models import *
from .serializers import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.views.generic import UpdateView


# Create your views here.
class MainPage(generics.GenericAPIView,
               mixins.CreateModelMixin):
    serializer_class = CreateNewsSerializer

    @staticmethod
    def get(request):
        if request.GET.get('login'):
            username = request.GET.get('username')
            password = request.GET.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main')
        model = Posts.objects.all()
        form = CreateNewsForm
        users = request.user
        data = {"model": model,
                'form': form,
                'user': users
                }

        return render(request, 'main/main.html', data)

    def post(self, request, *args, **kwargs):
        self.create(request, *args, **kwargs)
        return redirect('main')


"""API for Posts"""


class PostViewSets(generics.GenericAPIView,
                   mixins.CreateModelMixin,
                   mixins.ListModelMixin):
    queryset = Posts.objects.all()
    serializer_class = CreateNewsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PostDeleteUpdateSets(generics.GenericAPIView,
                           mixins.RetrieveModelMixin,
                           mixins.DestroyModelMixin,
                           mixins.UpdateModelMixin,
                           ):
    queryset = Posts.objects.all()
    serializer_class = CreateNewsSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, kwargs)


"""Api for comments"""


class CommentsViewSet(generics.GenericAPIView,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin):
    queryset = Comments.objects.all()
    serializer_class = CreateCommentSerializer
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CommentsUpdateDeleteSet(generics.GenericAPIView,
                              mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin,
                              mixins.RetrieveModelMixin):
    queryset = Comments.objects.values('id', 'username', 'comments', 'name__title')
    serializer_class = CreateCommentSerializer
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class NewsUpdateView(UpdateView):
    model = Posts
    fields = ['title', 'link', 'author_name']
    template_name = 'main/main.html'


"""registration user"""


class Registration(generics.GenericAPIView,
                   mixins.CreateModelMixin):
    serializer_class = CreateUserSerialize

    @staticmethod
    def get(request):
        form = RegistrForm
        data = {'form': form}
        return render(request, 'main/register.html', data)

    def post(self, request, *args, **kwargs):
        self.create(request, *args, **kwargs)
        return redirect('main')


"""Comment page"""


class Comment(generics.GenericAPIView,
              mixins.CreateModelMixin):
    serializer_class = CreateCommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    @staticmethod
    def get(request):
        form = CreateCommentForm
        model = Comments.objects.values('username', 'comments', 'name__title').order_by('-id')
        data = {'form': form,
                'model': model}
        return render(request, 'main/comments.html', data)

    def post(self, request, *args, **kwargs):
        self.create(request, *args, **kwargs)
        return redirect('comments')
