# Generated by Django 2.1.2 on 2018-10-19 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20181019_0827'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='views',
            field=models.PositiveIntegerField(default=0, editable=False, verbose_name='Views'),
        ),
    ]