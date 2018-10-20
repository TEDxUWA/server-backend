# Generated by Django 2.1.2 on 2018-10-20 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20180824_1618'),
    ]

    operations = [
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('profile_image', models.URLField(blank=True)),
                ('bio', models.TextField(blank=True, default='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('event', models.ManyToManyField(help_text='which event(s) this speaker is a part of', related_name='speakers', to='events.Event')),
            ],
        ),
    ]
