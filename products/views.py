from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . import models
from . import forms

# Create your views here.
class ProductCreateView(CreateView):
    model = models.Product
    template_name = 'product_create.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')

class ProductListView(ListView):
    model = models.Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        title = self.request.GET.get('title')

        if title:
            queryset = queryset.filter(title__icontains=title)

        return queryset
    
class ProductDetailView(DetailView):
    model = models.Product
    template_name = 'product_detail.html'

class ProductUpdateView(UpdateView):
    model = models.Product
    template_name = 'product_update.html'
    form_class = forms.ProductForm
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = models.Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')