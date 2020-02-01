# Generated by Django 3.0.2 on 2020-02-01 07:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200126_1652'),
    ]

    operations = [
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='', max_length=64)),
                ('social_page', models.CharField(blank=True, default='', max_length=64)),
                ('social_vk', models.CharField(blank=True, default='', max_length=64)),
                ('social_fb', models.CharField(blank=True, default='', max_length=64)),
                ('social_ok', models.CharField(blank=True, default='', max_length=64)),
                ('social_inst', models.CharField(blank=True, default='', max_length=64)),
                ('social_youtube', models.CharField(blank=True, default='', max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='minister',
            name='social',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Social'),
        ),
        migrations.AddField(
            model_name='setting',
            name='social',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Social'),
        ),
    ]
