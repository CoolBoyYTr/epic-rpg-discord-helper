# Generated by Django 3.1.3 on 2020-11-24 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('epic', '0006_timeformat'),
    ]

    operations = [
        migrations.CreateModel(
            name='Guild',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('after', models.DateTimeField(blank=True, null=True)),
                ('raid_dibbs', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='has_raid_dibbs_for', to='epic.profile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='player_guild',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='epic.guild'),
        ),
    ]
