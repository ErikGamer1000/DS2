# Generated by Django 5.1 on 2024-12-15 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_alter_contact_response_alter_contact_responsed_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='response',
            field=models.CharField(max_length=20, verbose_name='response'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='responsed_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='respondido em'),
        ),
    ]