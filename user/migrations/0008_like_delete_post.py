# Generated by Django 4.0.4 on 2022-05-16 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_post_delete_like'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like_user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.usersignup')),
                ('post_key', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='user.approvequotes')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
