# Generated by Django 4.2.1 on 2023-06-21 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('delivery_address', models.CharField(max_length=200)),
                ('delivery_status', models.CharField(max_length=50)),
                ('delivery_date', models.IntegerField()),
                ('delivery_method', models.CharField(max_length=50)),
                ('order_id', models.CharField(max_length=50)),
                ('delivery_cost', models.IntegerField()),
            ],
        ),
    ]