# Generated by Django 2.2 on 2019-06-02 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='user_name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='name'),
        ),
    ]
