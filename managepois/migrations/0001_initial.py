# Generated by Django 2.2 on 2021-02-01 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MapboxPOIs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('latitude', models.CharField(max_length=50)),
                ('longitude', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('geometry', models.CharField(max_length=200)),
                ('status', models.BooleanField(max_length=50)),
            ],
            options={
                'db_table': 'tbl_mapbox_pois',
            },
        ),
    ]