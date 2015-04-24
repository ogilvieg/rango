# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20150422_1216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.CharField(max_length=128)),
                ('votes', models.IntegerField()),
                ('question', models.ForeignKey(to='polls.Question')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
