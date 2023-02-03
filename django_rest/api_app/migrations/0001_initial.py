# Generated by Django 4.1.6 on 2023-02-03 16:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200)),
                ('date', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('status', models.CharField(choices=[('draft', 'Draft'), ('private', 'Private'), ('public', 'Public'), ('deleted', 'Deleted')], default='draft', max_length=200)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_events', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]