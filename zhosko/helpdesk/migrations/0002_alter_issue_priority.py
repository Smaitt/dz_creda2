# Generated by Django 4.1.5 on 2023-09-19 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='priority',
            field=models.CharField(choices=[('Низкий', 'Низкий'), ('Средний', 'Средний'), ('Высокий', 'Высокий')], max_length=10),
        ),
    ]
