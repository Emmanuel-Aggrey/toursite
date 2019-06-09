# Generated by Django 2.2 on 2019-06-04 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0012_auto_20190604_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='request_guiid',
            field=models.OneToOneField(blank=True, help_text='optional select a tour guid', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ticket.Tour_Guid', verbose_name='Request Guide'),
        ),
    ]