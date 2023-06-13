# Generated by Django 4.2.1 on 2023-06-13 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('active', models.BooleanField(default=True, verbose_name='Is Active')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Product Name')),
                ('price', models.IntegerField(default=0, verbose_name='Price')),
                ('quantity', models.IntegerField(default=0, verbose_name='Quantity')),
                ('image', models.ImageField(upload_to='uploads/%Y/%m/%d/')),
                ('description', models.TextField(verbose_name='Description')),
                ('type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.type')),
            ],
        ),
    ]
