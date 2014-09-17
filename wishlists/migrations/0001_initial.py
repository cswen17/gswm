# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('list_name', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WishlistItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('item_name', models.CharField(max_length=200)),
                ('item_description', models.CharField(max_length=1024)),
                ('item_price', models.DecimalField(max_digits=32, decimal_places=2)),
                ('item_url', models.URLField()),
                ('item_image', models.ImageField(upload_to=None)),
                ('wish_list', models.ForeignKey(to='wishlists.Wishlist')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
