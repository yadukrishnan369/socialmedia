# Generated by Django 3.2.8 on 2022-03-05 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adminsignup',
            old_name='adminName',
            new_name='name',
        ),
        migrations.AddField(
            model_name='adminsignup',
            name='username',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
