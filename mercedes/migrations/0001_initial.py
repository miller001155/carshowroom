# Generated by Django 4.1.3 on 2022-11-17 17:27

from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название компании')),
                ('founder', models.CharField(max_length=50, verbose_name='Основатель')),
                ('email', models.EmailField(max_length=100, verbose_name='Электронный адрес')),
                ('company_information', models.TextField(blank=True, max_length=500, null=True, verbose_name='Информация о компании')),
            ],
            options={
                'verbose_name': 'Поставщик',
                'verbose_name_plural': 'Поставщики',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stamp', models.CharField(max_length=50, verbose_name='Марка авто')),
                ('brand', models.CharField(max_length=50, verbose_name='Бренд')),
                ('country_of_origin', django_countries.fields.CountryField(max_length=2)),
                ('price', models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Цена')),
                ('specifications', models.TextField(max_length=500, verbose_name='Характеристики авто')),
                ('time_create', models.DateTimeField(auto_now_add=True, verbose_name='время создания')),
                ('providers', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mercedes.provider', verbose_name='Поставщики')),
            ],
            options={
                'verbose_name': 'Сеть салонов',
                'verbose_name_plural': 'Сеть салонов',
                'ordering': ['time_create'],
            },
        ),
    ]
