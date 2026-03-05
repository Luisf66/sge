from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from . import models
from . import forms

# Create your views here.
class InflowCreateView(LoginRequiredMixin ,CreateView):
    model = models.Inflow
    template_name = 'inflow_create.html'
    form_class = forms.InflowForm
    success_url = reverse_lazy('inflow_list')

class InflowListView(LoginRequiredMixin ,ListView):
    model = models.Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset

class InflowDetailView(LoginRequiredMixin ,DetailView):
    model = models.Inflow
    template_name = 'inflow_detail.html'