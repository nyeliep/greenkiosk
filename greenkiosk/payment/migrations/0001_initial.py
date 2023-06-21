# Generated by Django 4.2.1 on 2023-06-21 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.IntegerField(primary_key=True, serialize=False)),
                ('customer_id', models.IntegerField()),
                ('payment_method', models.CharField(max_length=50)),
                ('payment_status', models.CharField(max_length=50)),
                ('payment_date', models.IntegerField()),
                ('payment_amount', models.IntegerField()),
                ('currency_used', models.CharField(max_length=50)),
            ],
        ),
    ]