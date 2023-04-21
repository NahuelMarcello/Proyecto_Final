# Generated by Django 4.2 on 2023-04-21 09:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Games', '0007_post_created_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='DM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=1000)),
                ('email', models.EmailField(max_length=254)),
                ('addressee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receptor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]