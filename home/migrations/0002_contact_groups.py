# Generated by Django 3.0.6 on 2020-08-20 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='groups',
            field=models.ManyToManyField(to='auth.Group', verbose_name='test'),
        ),
    ]
