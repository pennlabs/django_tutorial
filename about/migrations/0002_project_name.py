# Generated by Django 2.1.1 on 2018-09-08 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
    ]