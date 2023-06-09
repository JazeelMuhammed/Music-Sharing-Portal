# Generated by Django 4.2.1 on 2023-05-29 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=20)),
                ('album', models.CharField(max_length=100)),
                ('file', models.FileField(upload_to='musics/')),
                ('is_private', models.BooleanField(default=False)),
                ('is_public', models.BooleanField(default=False)),
                ('is_protected', models.BooleanField(default=False)),
            ],
        ),
    ]
