# Generated by Django 2.2.5 on 2019-09-20 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='姓名')),
                ('sex', models.IntegerField(choices=[(1, '男'), (2, '女'), (0, '未知')], verbose_name='性别')),
                ('grades', models.IntegerField(choices=[(0, '小学'), (1, '初中'), (2, '高中')], verbose_name='年级')),
                ('classes', models.IntegerField(choices=[(1, '一年级'), (2, '二年级'), (3, '三年级'), (4, '四年级'), (5, '五年级'), (6, '六年级')], verbose_name='班级')),
                ('birth', models.DateField(verbose_name='出生日期')),
                ('status', models.IntegerField(choices=[(0, '申请'), (1, '通过'), (2, '拒绝')], default=0, verbose_name='审核状态')),
                ('created_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='USER',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='姓名')),
                ('cellphone', models.CharField(max_length=128, verbose_name='手机号')),
                ('email', models.CharField(max_length=128, verbose_name='邮箱')),
                ('status', models.IntegerField(choices=[(0, '申请'), (1, '通过'), (2, '拒绝')], default=1, verbose_name='审核状态')),
                ('created_time', models.DateTimeField(auto_now=True, verbose_name='创建时间')),
                ('sex', models.SmallIntegerField(choices=[(1, '男'), (2, '女'), (0, '未知')], default=0, verbose_name='性别')),
                ('avatar', models.CharField(blank=True, default='', max_length=50, null=True, verbose_name='头像')),
                ('openid', models.CharField(db_index=True, max_length=64, verbose_name='openid')),
                ('admin_type', models.IntegerField(choices=[(0, '超级管理员'), (1, '公司管理员'), (2, '一般用户')], default=2, verbose_name='账户类型')),
            ],
        ),
        migrations.CreateModel(
            name='Student_USER',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_type', models.IntegerField(choices=[(0, '创建者'), (1, '被邀请者')], verbose_name='关系类型')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ttable.Student')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ttable.USER')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='user',
            field=models.ManyToManyField(through='ttable.Student_USER', to='ttable.USER'),
        ),
    ]
