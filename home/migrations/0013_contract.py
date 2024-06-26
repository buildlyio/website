# Generated by Django 3.2 on 2023-03-21 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_enterprise'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('party_one', models.CharField(blank=True, max_length=255, null=True)),
                ('party_two', models.CharField(blank=True, max_length=255, null=True)),
                ('hash', models.CharField(blank=True, max_length=255, null=True)),
                ('file', models.CharField(blank=True, max_length=255, null=True)),
                ('text', models.TextField(blank=True, null=True)),
                ('create_date', models.DateTimeField(blank=True, null=True)),
                ('edit_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
