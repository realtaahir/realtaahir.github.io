# Generated by Django 5.0.6 on 2024-07-08 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_alter_headquiz_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='headquiz',
            options={'permissions': [('can_view_1_headquiz', 'Can view the 1 headquizzes'), ('can_view_all_headquiz', 'Can view all headquizzes')]},
        ),
    ]