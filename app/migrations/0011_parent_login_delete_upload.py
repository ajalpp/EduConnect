# Generated by Django 4.1 on 2025-02-13 05:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_rename_student_id_upload_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='parent',
            name='login',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.login'),
        ),
        migrations.DeleteModel(
            name='upload',
        ),
    ]
