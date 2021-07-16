# Generated by Django 3.2.4 on 2021-07-16 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publication_date', models.DateTimeField(verbose_name='Дата создания отчета')),
                ('production_department', models.BigIntegerField(default=0, verbose_name='Номер производственного отделения')),
                ('greenhouse', models.BigIntegerField(default=0, verbose_name='Номер теплицы')),
                ('report_comment', models.CharField(max_length=255, verbose_name='Комментарий к отчету')),
            ],
        ),
    ]
