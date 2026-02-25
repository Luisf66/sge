from django.urls import path

from . import views

urlpatterns = [
    path('brand/create/', views.BrandCreateView.as_view(), name='brand_create'),
    path('brand/list/', views.BrandListView.as_view(), name='brand_list'),
    path('brand/<int:pk>/detail/', views.BrandDetailView.as_view(), name='brand_detail'),
]
