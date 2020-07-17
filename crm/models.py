from django.db import models


class Clients(models.Model):
    name = models.CharField('Имя', max_length=255)
    age = models.TextField(max_length=5)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    social_contacts = models.TextField(blank=True)
    whatsapp = models.TextField(max_length=255)
    direction = models.ForeignKey('Directions', on_delete=models.DO_NOTHING)
    visits = models.DateField()
    payment = models.CharField(max_length=255)


class Trainers(models.Model):
    name = models.CharField('ФИО Тренера', max_length=255)
    direction = models.ForeignKey('Directions', on_delete=models.DO_NOTHING)


class Directions(models.Model):
    direction = models.CharField('Направление', max_length=255)
# Create your models here.
