# Generated by Django 2.2.3 on 2019-07-26 14:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Ruper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='password',
            field=models.CharField(max_length=255, validators=[django.core.validators.RegexValidator('^/W+/w+/d+{3}([$-/:-?{-~!"^_`\\[\\]]{2})', message='Password Must start with two(2)Capital Letters,Contain at least three(3) Numbers and contain at least two(2) Symbols')], verbose_name='Password'),
        ),
    ]