# Generated by Django 4.1 on 2025-04-22 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_remove_complaint_sender_id_complaint_login'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.student'),
        ),
    ]
