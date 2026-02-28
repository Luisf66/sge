from django.views.generic import CreateView, ListView, DetailView
from django.urls import reverse_lazy

from . import models
from . import forms
# Create your views here.


class OutflowCreateView(CreateView):
    model = models.Outflow
    template_name = 'outflow_create.html'
    form_class = forms.OutflowForm
    success_url = reverse_lazy('outflow_list')

class OutflowListView(ListView):
    model = models.Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset
    
class OutflowDetailView(DetailView):
    model = models.Outflow
    template_name = 'outflow_detail.html'