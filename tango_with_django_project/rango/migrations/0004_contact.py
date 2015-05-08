# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0003_category_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=75)),
                ('subject', models.CharField(max_length=128)),
                ('message', models.CharField(max_length=256)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
