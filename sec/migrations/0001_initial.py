# Generated by Django 2.1 on 2018-08-29 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('email', models.CharField(max_length=140)),
                ('phone', models.CharField(max_length=140)),
                ('age', models.CharField(max_length=3)),
                ('gender', models.CharField(max_length=140)),
                ('comment', models.TextField(max_length=1400)),
            ],
        ),
    ]
