# Generated by Django 4.1.5 on 2023-02-09 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('m', '0003_alter_review_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('project', models.ManyToManyField(related_name='tags', to='m.project')),
            ],
        ),
    ]
