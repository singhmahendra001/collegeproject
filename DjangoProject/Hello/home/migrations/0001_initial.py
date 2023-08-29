# Generated by Django 4.0.4 on 2022-04-22 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=12)),
                ('desc', models.TextField()),
            ],
        ),
    ]
