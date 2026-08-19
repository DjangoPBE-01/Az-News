from django.urls import path
from apps.news.views import HomeView

app_name = 'news'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
]