# Generated by Django 4.2.17 on 2025-03-15 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_contactsubmission'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platform', models.CharField(choices=[('whatsapp', 'WhatsApp'), ('telegram', 'Telegram'), ('linkedin', 'LinkedIn'), ('twitter', 'Twitter'), ('instagram', 'Instagram'), ('github', 'GitHub')], max_length=20)),
                ('url', models.URLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('slug', models.SlugField(blank=True, max_length=100, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='contactsubmission',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
