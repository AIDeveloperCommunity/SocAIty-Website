# Generated by Django 2.1.2 on 2018-10-18 21:55

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0016_auto_20181018_2134'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('voter', 'blog')},
        ),
    ]
