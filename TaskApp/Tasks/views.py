from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import generics
from .models import Tache
from .serializers import TacheSerializer

# Web Views
class TacheListView(ListView):
    model = Tache
    template_name = 'Tasks/tache_list.html'

class TacheDetailView(DetailView):
    model = Tache
    template_name = 'Tasks/tache_detail.html'

class TacheCreateView(CreateView):
    model = Tache
    template_name = 'Tasks/tache_form.html'
    fields = ['titre', 'description', 'statut']

class TacheUpdateView(UpdateView):
    model = Tache
    template_name = 'Tasks/tache_form.html'
    fields = ['titre', 'description', 'statut']

class TacheDeleteView(DeleteView):
    model = Tache
    template_name = 'Tasks/tache_confirm_delete.html'
    success_url = reverse_lazy('tache_list')

# API Views
class TacheListCreateAPIView(generics.ListCreateAPIView):
    queryset = Tache.objects.all()
    serializer_class = TacheSerializer

class TacheRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tache.objects.all()
    serializer_class = TacheSerializer
