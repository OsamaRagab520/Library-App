# Generated by Django 3.2.7 on 2021-09-19 14:47

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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('img', models.URLField()),
                ('description', models.TextField()),
                ('added_at', models.DateField(auto_now_add=True)),
                ('return_date', models.DateField(null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='library.category')),
                ('student', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
