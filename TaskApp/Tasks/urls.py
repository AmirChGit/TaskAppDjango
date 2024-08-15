from django.urls import path
from .views import (
    TacheListView, 
    TacheDetailView, 
    TacheCreateView, 
    TacheUpdateView, 
    TacheDeleteView,
    TacheListCreateAPIView,  # API views
    TacheRetrieveUpdateDestroyAPIView  # API views
)

urlpatterns = [
    # Web views
    path('', TacheListView.as_view(), name='tache_list'),
    path('tache/<int:pk>/', TacheDetailView.as_view(), name='tache_detail'),
    path('tache/new/', TacheCreateView.as_view(), name='tache_new'),
    path('tache/<int:pk>/edit/', TacheUpdateView.as_view(), name='tache_edit'),
    path('tache/<int:pk>/delete/', TacheDeleteView.as_view(), name='tache_delete'),

    # API views
    path('api/taches/', TacheListCreateAPIView.as_view(), name='tache_list_create_api'),
    path('api/taches/<int:pk>/', TacheRetrieveUpdateDestroyAPIView.as_view(), name='tache_detail_api'),
]
