# Generated by Django 3.1.2 on 2020-11-16 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_auto_20201116_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='best_bidder',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gets', to=settings.AUTH_USER_MODEL),
        ),
    ]
