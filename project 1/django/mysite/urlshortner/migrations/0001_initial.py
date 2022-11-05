# Generated by Django 4.1.3 on 2022-11-02 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ShortUrls',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('original_url', models.CharField(max_length=500)),
                ('short_id', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField()),
            ],
        ),
    ]
