from .models import Clients, Trainers, Directions
from django import forms


class ClientsForms(forms.ModelForm):
    class Meta:
        model = Clients
        fields = '__all__'

    def __str__(self):
        return self.name


class DirectionsForms(forms.ModelForm):
    class Meta:
        model = Directions
        fields = '__all__'

    def __str__(self):
        return self.name


class TrainerForms(forms.ModelForm):
    class Meta:
        model = Trainers
        fields = '__all__'

    def __str__(self):
        return self.name