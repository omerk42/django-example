# Generated by Django 4.1 on 2022-08-25 15:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('djangoApp', '0002_contact_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Email',
            new_name='email',
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]
