# Generated by Django 3.0.2 on 2024-02-17 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoginModel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login_user',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]