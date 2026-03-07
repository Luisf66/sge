from django.urls import path

from . import views

urlpatterns = [
    path('brand/create/', views.BrandCreateView.as_view(), name='brand_create'),
    path('brand/list/', views.BrandListView.as_view(), name='brand_list'),
    path('brand/<int:pk>/detail/', views.BrandDetailView.as_view(), name='brand_detail'),
    path('brand/<int:pk>/update/', views.BrandUpdateView.as_view(), name='brand_update'),
    path('brand/<int:pk>/delete/', views.BrandDeleteView.as_view(), name='brand_delete'),

    path('api/v1/brands/', views.BrandListCreateApiView.as_view(), name='brand-list-create-api-view'),
    path('api/v1/brands/<int:pk>/', views.BrandRetrieveUpdateDestroyApiView.as_view(), name='brand-detail-api-view'),
]
