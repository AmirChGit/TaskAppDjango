# Tasks/models.py

from django.db import models
from django.urls import reverse

class Tache(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    date_de_creation = models.DateTimeField(auto_now_add=True)
    statut = models.BooleanField(default=False)

    def __str__(self):
        return self.titre

    def get_absolute_url(self):
        return reverse('tache_detail', kwargs={'pk': self.pk})
