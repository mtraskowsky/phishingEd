# Generated by Django 2.1.5 on 2021-03-12 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listView', '0003_post_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='reciever',
            new_name='receiver',
        ),
        migrations.AddField(
            model_name='post',
            name='subject',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
