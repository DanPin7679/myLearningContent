# Generated by Django 3.2.5 on 2021-07-22 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learningcontent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='subject',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
