from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import views


urlpatterns = [
    path('', views.MainPage.as_view(), name='main'),
    path('accounts/', include('allauth.urls')),
    path('posts_api/', views.PostViewSets.as_view()),
    path('posts_api/<int:pk>', views.PostDeleteUpdateSets.as_view()),
    path('comments_api/', views.CommentsViewSet.as_view()),
    path('comments_api/<int:pk>', views.CommentsUpdateDeleteSet.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('registration/', views.registration, name='register'),
    path('comments/', views.Comment.as_view(), name="comments"),
    path('UpdatePosts/<int:pk>', views.NewsUpdateView.as_view(), name='news_update')
]
