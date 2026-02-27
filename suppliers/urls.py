from django.urls import path

from . import views

urlpatterns = [
    path('suppliers/create/', views.SupplierCreateView.as_view(), name='supplier_create'),
    path('suppliers/list/', views.SupplierListView.as_view(), name='supplier_list'),
    path('suppliers/<int:pk>/detail/', views.SupplierDetailView.as_view(), name='supplier_detail'),
    path('supplier/<int:pk>/update/', views.SupplierUpdateView.as_view(), name='supplier_update'),
    path('supplier/<int:pk>/delete/', views.SupplierDeleteView.as_view(), name='supplier_delete'),
]
