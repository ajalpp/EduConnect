# Generated by Django 4.1 on 2025-03-26 03:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_teacher_course_attendance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='complaint',
            name='sender_id',
        ),
        migrations.AddField(
            model_name='complaint',
            name='login',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.login'),
        ),
    ]
