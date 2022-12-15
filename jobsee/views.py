from django.views.generic import TemplateView, ListView, CreateView
from django.urls import reverse_lazy
import jobsee.models as models


class HomepageView(TemplateView):
    template_name = 'base.html'


class CompanyListView(ListView):
    model = models.Company
    template_name = 'company/list.html'


class CompanyCreateView(CreateView):
    model = models.Company
    template_name = 'company/create.html'
    fields = ['name', 'base_location', 'technologies', 'www']
    success_url = reverse_lazy('company_list')
