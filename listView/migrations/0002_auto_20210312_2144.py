# Generated by Django 2.1.5 on 2021-03-12 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listView', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='scamType',
            field=models.CharField(choices=[('Link', 'Phishing with a link'), ('Reply', 'Reply to')], max_length=255),
        ),
    ]