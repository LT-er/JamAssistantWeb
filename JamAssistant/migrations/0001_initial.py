# Generated by Django 2.0.2 on 2018-05-12 13:19

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stu_name', models.CharField(max_length=32)),
            ],
        ),
    ]
