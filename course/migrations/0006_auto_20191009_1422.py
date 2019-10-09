# Generated by Django 2.2.5 on 2019-10-09 14:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20191009_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='发布者'),
        ),
        migrations.AlterField(
            model_name='course',
            name='owner',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='发布者'),
        ),
        migrations.AlterField(
            model_name='course_pakage',
            name='owner',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='发布者'),
        ),
        migrations.AlterField(
            model_name='label_course',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='发布者'),
        ),
        migrations.AlterField(
            model_name='label_course_pakage',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='发布者'),
        ),
    ]