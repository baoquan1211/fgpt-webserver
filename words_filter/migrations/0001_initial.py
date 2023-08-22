# Generated by Django 4.2.4 on 2023-08-21 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WordsFilter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_words', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'app_words_filter',
            },
        ),
    ]
