# Generated by Django 4.2.4 on 2023-08-18 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0006_alter_conversation_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='questions',
            field=models.TextField(blank=True, default=''),
        ),
    ]
