# Generated by Django 4.0.3 on 2022-06-22 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.CharField(max_length=150, verbose_name='Логотип')),
                ('fio', models.CharField(max_length=150, verbose_name='ФИО')),
                ('school', models.CharField(max_length=150, verbose_name='Школа')),
                ('objects_school', models.CharField(max_length=150, verbose_name='Предмет')),
                ('date', models.DateField(verbose_name='Дата')),
                ('biograf', models.TextField(verbose_name='Биография')),
                ('diploma1', models.CharField(blank=True, max_length=150, verbose_name='Дипломы1')),
                ('diploma2', models.CharField(blank=True, max_length=150, verbose_name='Дипломы2')),
                ('diploma3', models.CharField(blank=True, max_length=150, verbose_name='Дипломы3')),
                ('diploma4', models.CharField(blank=True, max_length=150, verbose_name='Дипломы4')),
                ('diploma5', models.CharField(blank=True, max_length=150, verbose_name='Дипломы5')),
                ('diploma6', models.CharField(blank=True, max_length=150, verbose_name='Дипломы6')),
                ('diploma7', models.CharField(blank=True, max_length=150, verbose_name='Дипломы7')),
                ('diploma8', models.CharField(blank=True, max_length=150, verbose_name='Дипломы8')),
                ('education', models.CharField(max_length=150, verbose_name='Образование')),
                ('experience', models.CharField(max_length=150, verbose_name='Стаж работы')),
                ('qualif', models.CharField(max_length=150, verbose_name='Повышение квалификации')),
                ('author', models.CharField(max_length=150, verbose_name='Логин учителя')),
            ],
            options={
                'verbose_name': 'Портволио',
                'verbose_name_plural': 'Портволио',
            },
        ),
    ]
