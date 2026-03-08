from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView

from rest_framework import generics
from . import serializers, models, forms
from app.metrics import get_sales_metrics


class OutflowListCreateApiView(generics.ListCreateAPIView):
    queryset = models.Outflow.objects.all() 
    serializer_class = serializers.OutflowSerializer

class OutflowRetrieveApiView(generics.RetrieveAPIView):
    queryset = models.Outflow.objects.all()
    serializer_class = serializers.OutflowSerializer

# Create your views here.
class OutflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Outflow
    template_name = 'outflow_create.html'
    form_class = forms.OutflowForm
    success_url = reverse_lazy('outflow_list')
    permission_required = 'outflows.add_outflow'

class OutflowListView(LoginRequiredMixin ,ListView):
    model = models.Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    paginate_by = 10
    permission_required = 'outflows.view_outflow'

    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')

        if product:
            queryset = queryset.filter(product__title__icontains=product)

        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales_metrics'] = get_sales_metrics()
        return context
    
class OutflowDetailView(LoginRequiredMixin ,DetailView):
    model = models.Outflow
    template_name = 'outflow_detail.html'
    permission_required = 'outflows.view_outflow'