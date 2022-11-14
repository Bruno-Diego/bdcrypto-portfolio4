# Generated by Django 3.2.15 on 2022-11-14 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_portfolio_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='asset',
            options={'ordering': ['-symbol']},
        ),
        migrations.RenameField(
            model_name='asset',
            old_name='ticker',
            new_name='symbol',
        ),
        migrations.AddField(
            model_name='asset',
            name='icon',
            field=models.URLField(blank=True, null=True),
        ),
    ]
