# Generated by Django 3.2.4 on 2021-06-29 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CBVM_APP', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='username',
            field=models.CharField(max_length=20),
        ),
    ]