# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('Share', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='upload',
            options={'verbose_name': 'download', 'verbose_name_plural': 'download'},
        ),
        migrations.AlterField(
            model_name='upload',
            name='Datatime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='upload',
            name='DownloadDocount',
            field=models.IntegerField(verbose_name='下载次数', default=0),
        ),
    ]
