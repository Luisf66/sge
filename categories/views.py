from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from rest_framework import generics
from . import serializers, models, forms


class CategoryListCreateApiView(generics.ListCreateAPIView):
    queryset = models.Categories.objects.all()
    serializer_class = serializers.CategorySerializer

# Create your views here.
class CategoryCreateView(LoginRequiredMixin ,CreateView):
    model = models.Categories
    template_name = 'category_create.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('category_list')

class CategoryListView(LoginRequiredMixin ,ListView):
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
    
class CategoryDetailView(LoginRequiredMixin ,DetailView):
    model = models.Categories
    template_name = 'category_detail.html'

class CategoryUpdateView(LoginRequiredMixin ,UpdateView):
    model = models.Categories
    template_name = 'category_update.html'
    form_class = forms.CategoryForm
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(LoginRequiredMixin ,DeleteView):
    model = models.Categories
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category_list')