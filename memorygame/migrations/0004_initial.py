# Generated by Django 4.1.3 on 2022-12-07 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('memorygame', '0003_delete_card_delete_score'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match', models.IntegerField()),
                ('name', models.CharField(default='', max_length=200)),
                ('status', models.CharField(default='', max_length=200)),
                ('img', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('val', models.FloatField()),
                ('user_name', models.CharField(max_length=200)),
            ],
        ),
    ]
