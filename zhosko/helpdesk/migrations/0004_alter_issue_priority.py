# Generated by Django 4.1.5 on 2023-09-27 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0003_issue_actions_issue_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.CharField(max_length=10),
        ),
    ]
