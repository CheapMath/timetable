# Generated by Django 2.2.5 on 2019-09-30 04:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ttable', '0003_auto_20190930_1205'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_user',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
