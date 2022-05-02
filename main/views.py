from django.shortcuts import render, redirect
from rest_framework import generics, mixins, permissions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from .models import *
from .serializers import *
from .forms import *
from django.contrib.auth import authenticate, login
from django.views.generic import UpdateView
from captcha.fields import CaptchaField

from rest_framework.response import Response


# Create your views here.
class MainPage(generics.GenericAPIView,
               mixins.CreateModelMixin):
    serializer_class = CreateNewsSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication]

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
                'user': users,
                }

        if request.GET.get('req'):
            comment_data = Comments.objects.filter(name__title=f"{request.GET.get('req')}").values('id', 'username',
                                                                                                   'comments',
                                                                                                   'name__title',
                                                                                                   'name__link',
                                                                                                   'create_date')
            form = CreateCommentForm
            data = {'model': comment_data,
                    'form': form}

            return render(request, 'main/detail_posts.html', data)

        return render(request, 'main/main.html', data)

    def post(self, request, *args, **kwargs):
        self.create(request, *args, **kwargs)
        return redirect('main')


class DetailComment(generics.GenericAPIView,
                    mixins.CreateModelMixin):
    serializer_class = CreateCommentSerializer

    @staticmethod
    def get(request):
        form = CreateCommentForm
        data = {'form': form,
                }
        return render(request, 'main/detail_posts.html', data)


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


def registration(request):
    if request.method == "POST":
        form = RegistrForm(request.POST)
        if form.is_valid():
            form.save()
    form = RegistrForm
    data = {'form': form}

    return render(request, 'main/register.html', data)


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
        return redirect('main')
