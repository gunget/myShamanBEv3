# Generated by Django 3.1.5 on 2021-03-23 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieDrtr', '0007_auto_20210319_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='ficwriterinfo',
            name='job',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
    ]