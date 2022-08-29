# Generated by Django 3.2.12 on 2022-07-13 06:17

import common.db.fields
import django.core.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0051_sessionsharing_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='endpoint',
            name='oracle_11g_port',
            field=common.db.fields.PortField(default=15211, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(65535)], verbose_name='Oracle 11g Port'),
        ),
        migrations.AddField(
            model_name='endpoint',
            name='oracle_12c_port',
            field=common.db.fields.PortField(default=15212, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(65535)], verbose_name='Oracle 12c Port'),
        ),
    ]
