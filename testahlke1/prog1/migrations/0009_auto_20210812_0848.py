# Generated by Django 3.2.6 on 2021-08-12 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prog1', '0008_auto_20210811_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dokumentationmodel',
            old_name='admindokumation',
            new_name='admindokumentation',
        ),
        migrations.RenameField(
            model_name='dokumentationmodel',
            old_name='apidokumation',
            new_name='apidokumentation',
        ),
        migrations.RenameField(
            model_name='dokumentationmodel',
            old_name='appUrldokumation',
            new_name='appUrldokumentation',
        ),
        migrations.RenameField(
            model_name='dokumentationmodel',
            old_name='djangodokumation',
            new_name='djangodokumentation',
        ),
        migrations.RenameField(
            model_name='dokumentationmodel',
            old_name='formsdokumation',
            new_name='formsdokumentation',
        ),
        migrations.RenameField(
            model_name='dokumentationmodel',
            old_name='githubdokumation',
            new_name='githubdokumentation',
        ),
        migrations.RenameField(
            model_name='dokumentationmodel',
            old_name='hauptUrldokumation',
            new_name='hauptUrldokumentation',
        ),
        migrations.RenameField(
            model_name='dokumentationmodel',
            old_name='modelsdokumation',
            new_name='modelsdokumentation',
        ),
        migrations.RenameField(
            model_name='dokumentationmodel',
            old_name='settingsdokumation',
            new_name='settingsdokumentation',
        ),
        migrations.RenameField(
            model_name='dokumentationmodel',
            old_name='sonstigesdokumation',
            new_name='sonstigesdokumentation',
        ),
        migrations.RenameField(
            model_name='dokumentationmodel',
            old_name='templatesdokumation',
            new_name='templatesdokumentation',
        ),
        migrations.RenameField(
            model_name='dokumentationmodel',
            old_name='viewsdokumation',
            new_name='viewsdokumentation',
        ),
    ]