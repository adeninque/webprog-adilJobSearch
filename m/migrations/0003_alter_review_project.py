# Generated by Django 4.1.5 on 2023-02-09 03:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('m', '0002_review'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='m.project'),
        ),
    ]
