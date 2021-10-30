# Generated by Django 3.2.8 on 2021-10-24 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(auto_now_add=True, verbose_name='date created')),
                ('name', models.CharField(max_length=500, verbose_name='name')),
            ],
        ),
        migrations.CreateModel(
            name='TimeWindow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(verbose_name='period begins on date')),
            ],
        ),
        migrations.DeleteModel(
            name='Greeting',
        ),
        migrations.AddField(
            model_name='food',
            name='consumed_in_period',
            field=models.ManyToManyField(to='mainapp.TimeWindow'),
        ),
    ]