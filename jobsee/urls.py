from django.urls import path
import jobsee.views as views


urlpatterns = [
    path('', views.HomepageView.as_view(), name='homepage'),
    path('companies', views.CompanyListView.as_view(), name='company_list'),
    path('companies/create', views.CompanyCreateView.as_view(), name='company_create')
]