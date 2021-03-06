# Generated by Django 3.0.2 on 2020-02-01 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_subscriber'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendedForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(blank=True, default='', max_length=64)),
                ('email', models.EmailField(blank=True, default='', max_length=254)),
                ('name', models.CharField(blank=True, default='', max_length=64)),
                ('tel', models.CharField(blank=True, default='', max_length=64)),
                ('message', models.TextField(blank=True, default='')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='subscriber',
            options={'ordering': ('email', 'method')},
        ),
        migrations.AddField(
            model_name='subscriber',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='method',
            field=models.CharField(default='', max_length=64),
        ),
        migrations.AlterField(
            model_name='subscriber',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
        migrations.AlterUniqueTogether(
            name='subscriber',
            unique_together={('email', 'method')},
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='desc',
        ),
    ]
