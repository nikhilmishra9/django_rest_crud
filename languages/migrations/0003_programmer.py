# Generated by Django 2.0.6 on 2019-05-24 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0002_auto_20190524_0954'),
    ]

    operations = [
        migrations.CreateModel(
            name='Programmer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('languages', models.ManyToManyField(to='languages.Language')),
            ],
        ),
    ]