from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . import models
from . import forms


# Create your views here.
class CategoryCreateView(CreateView):
    model = models.Categories
    template_name = 'category_create.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('category_list')

class CategoryListView(ListView):
    model = models.Categories
    template_name = 'category_list.html'
    context_object_name = 'categories'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get('name')

        if name:
            queryset = queryset.filter(name__icontains=name)

        return queryset
    
class CategoryDetailView(DetailView):
    model = models.Categories
    template_name = 'category_detail.html'

class CategoryUpdateView(UpdateView):
    model = models.Categories
    template_name = 'category_update.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = models.Categories
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category_list')