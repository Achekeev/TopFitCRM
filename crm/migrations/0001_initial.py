# Generated by Django 3.0.7 on 2020-07-17 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Directions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.CharField(max_length=255, verbose_name='Направление')),
            ],
        ),
        migrations.CreateModel(
            name='Trainers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ФИО Тренера')),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='crm.Directions')),
            ],
        ),
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Имя')),
                ('age', models.TextField(max_length=5)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('social_contacts', models.TextField(blank=True)),
                ('whatsapp', models.TextField(max_length=255)),
                ('visits', models.DateField()),
                ('payment', models.CharField(max_length=255)),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='crm.Directions')),
            ],
        ),
    ]
