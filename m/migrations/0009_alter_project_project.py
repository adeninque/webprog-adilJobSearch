# Generated by Django 4.1.5 on 2023-02-09 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m', '0008_remove_tag_project_project_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project',
            field=models.ManyToManyField(related_name='projects', to='m.project'),
        ),
    ]
