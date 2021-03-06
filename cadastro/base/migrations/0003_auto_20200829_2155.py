# Generated by Django 3.1 on 2020-08-30 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_pessoa'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pessoa',
            options={'ordering': ('nome',), 'verbose_name_plural': 'pessoas'},
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='apelido',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='obs',
            field=models.TextField(blank=True, max_length=400),
        ),
    ]
