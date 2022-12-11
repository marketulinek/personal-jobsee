from django.urls import path
import jobsee.views as views


urlpatterns = [
    path('', views.HomepageView.as_view(), name='homepage'),
]