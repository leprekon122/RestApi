from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='main'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('registration/', views.Registration.as_view(), name='register'),
    path('comments/', views.Comment.as_view(), name="comments"),
    path('UpdatePosts/<int:pk>', views.NewsUpdateView.as_view(), name='news_update'),
]
