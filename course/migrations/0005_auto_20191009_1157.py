# Generated by Django 2.2.5 on 2019-10-09 11:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_auto_20191009_1143'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': '课程', 'verbose_name_plural': '课程'},
        ),
        migrations.AlterModelOptions(
            name='course_pakage',
            options={'verbose_name': '课程包', 'verbose_name_plural': '课程包'},
        ),
        migrations.AlterField(
            model_name='content',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='发布者'),
        ),
        migrations.AlterField(
            model_name='course',
            name='end_time',
            field=models.TimeField(verbose_name='结束时间'),
        ),
        migrations.AlterField(
            model_name='course',
            name='owner',
            field=models.ForeignKey(default=False, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='发布者'),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_time',
            field=models.TimeField(verbose_name='开始时间'),
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