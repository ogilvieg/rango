# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_choice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='date_published',
            new_name='pub_date',
        ),
    ]
