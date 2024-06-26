# Generated by Django 5.0.6 on 2024-05-17 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='twitter',
            field=models.CharField(blank=True, max_length=255, verbose_name='Twitter'),
        ),
        migrations.AddField(
            model_name='user',
            name='web_site',
            field=models.CharField(blank=True, max_length=255, verbose_name='Web site'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email'),
        ),
    ]
