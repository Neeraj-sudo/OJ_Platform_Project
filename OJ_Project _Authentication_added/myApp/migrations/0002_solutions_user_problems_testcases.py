# Generated by Django 4.0.3 on 2022-03-29 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solutions',
            fields=[
                ('problem', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='myApp.problem')),
                ('verdict', models.CharField(max_length=200)),
                ('submittedAt', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='problems',
            field=models.ManyToManyField(to='myApp.problem'),
        ),
        migrations.CreateModel(
            name='TestCases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', models.CharField(max_length=200)),
                ('output', models.CharField(max_length=200)),
                ('problem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.problem')),
            ],
        ),
    ]