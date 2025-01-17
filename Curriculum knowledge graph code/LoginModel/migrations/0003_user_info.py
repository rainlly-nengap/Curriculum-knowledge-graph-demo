# Generated by Django 3.0.2 on 2024-02-28 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginModel', '0002_auto_20240217_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('user_grade', models.CharField(max_length=255)),
                ('user_classes', models.CharField(max_length=255)),
                ('user_birthday', models.CharField(max_length=255)),
                ('user_home', models.CharField(max_length=255)),
                ('user_hobby', models.CharField(max_length=255)),
                ('user_province', models.CharField(max_length=255)),
                ('user_city', models.CharField(max_length=255)),
                ('user_region', models.CharField(max_length=255)),
                ('user_gender', models.CharField(max_length=3)),
                ('user_sign', models.CharField(max_length=3)),
            ],
        ),
    ]
