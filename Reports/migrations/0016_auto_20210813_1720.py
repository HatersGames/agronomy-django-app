# Generated by Django 3.2.6 on 2021-08-13 12:20

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reports', '0015_auto_20210813_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='glazing_throughput',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)], verbose_name='Пропускная способность остекления (в процентах)'),
        ),
        migrations.AlterField(
            model_name='report',
            name='light_intensity',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Интенсивность естественного света'),
        ),
        migrations.AlterField(
            model_name='report',
            name='light_intensity_per_day',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Интенсивность естественного света (за световой день)'),
        ),
        migrations.AlterField(
            model_name='report',
            name='lighting_system_operating_time',
            field=models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)], verbose_name='Количество часов работы системы досвечивания (50% вкл и откл берутся как 0,5 за 1 полный час)'),
        ),
        migrations.AlterField(
            model_name='report',
            name='lighting_system_power',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Мощность системы досвечивания'),
        ),
        migrations.AlterField(
            model_name='report',
            name='lighting_system_turn_off_time',
            field=models.TimeField(verbose_name='Время отключения досвечивания'),
        ),
        migrations.AlterField(
            model_name='report',
            name='lighting_system_turn_on_time',
            field=models.TimeField(verbose_name='Время включения досвечивания'),
        ),
        migrations.AlterField(
            model_name='report',
            name='solar_radiation_per_day',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0.0)], verbose_name='Приход естественной солнечной радиации за сутки'),
        ),
        migrations.AlterField(
            model_name='report',
            name='sunrise_time',
            field=models.TimeField(verbose_name='Время естественного восхода Солнца'),
        ),
        migrations.AlterField(
            model_name='report',
            name='sunset_time',
            field=models.TimeField(verbose_name='Время естественного захода Солнца'),
        ),
        migrations.AlterField(
            model_name='report',
            name='temp_day',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Т дневная'),
        ),
        migrations.AlterField(
            model_name='report',
            name='temp_day_avr',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Т среднесуточная'),
        ),
        migrations.AlterField(
            model_name='report',
            name='temp_day_max',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Т макс дневная'),
        ),
        migrations.AlterField(
            model_name='report',
            name='temp_night',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Т ночная'),
        ),
        migrations.AlterField(
            model_name='report',
            name='unlit_light_points',
            field=models.PositiveIntegerField(verbose_name='Количество негорящих светоточек'),
        ),
    ]
