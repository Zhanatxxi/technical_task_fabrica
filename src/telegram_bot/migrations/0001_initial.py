# Generated by Django 4.2.5 on 2023-09-05 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=128, null=True)),
                ('first_name', models.CharField(blank=True, max_length=128, null=True)),
                ('telegram_id', models.CharField(db_index=True, max_length=128, unique=True)),
                ('token_api', models.UUIDField()),
            ],
        ),
    ]