from django.shortcuts import render
from .models import Clients, Trainers, Directions
from .forms import ClientsForms, TrainerForms, DirectionsForms
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, RedirectView
from django.shortcuts import get_object_or_404


class ClientsListView(ListView):
    model = Clients
    template_name = 'client_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = Clients.name
        return context

    def get_object(self):
        return self.request.user


class ClientDetailView(DetailView):
    model = Clients
    template_name = 'client-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class TrainersListView(ListView):
    model = Trainers
    template_name = 'trainer-list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = Trainers.name
        return context

    def get_object(self):
        return self.request.user


class TrainersDetailView(DetailView):
    model = Trainers
    template_name = 'trainer-detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context
# Create your views here.
