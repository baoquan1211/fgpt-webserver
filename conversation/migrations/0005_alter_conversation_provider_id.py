# Generated by Django 4.2.4 on 2023-08-18 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conversation', '0004_alter_conversation_messages'),
    ]

    operations = [
        migrations.AlterField(
            model_name='conversation',
            name='provider_id',
            field=models.IntegerField(null=True),
        ),
    ]
