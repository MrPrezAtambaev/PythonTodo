# Generated by Django 4.2.1 on 2023-05-24 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todos', '0005_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='author',
            field=models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]