# Generated by Django 3.2.19 on 2023-05-31 00:02

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hcs', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scamreport',
            name='user',
        ),
        migrations.AddField(
            model_name='scamreport',
            name='report_email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='scamreport',
            name='report_phone',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='scamreport',
            name='your_email',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='scamreport',
            name='your_full_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='scamreport',
            name='category',
            field=models.CharField(choices=[('scam', 'Scam'), ('hack', 'Hack'), ('crack', 'Crack')], max_length=10),
        ),
        migrations.AlterField(
            model_name='scamreport',
            name='location_city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='scamreport',
            name='location_country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='scamreport',
            name='location_state',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='scamreport',
            name='source',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.CreateModel(
            name='ReportVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('is_upvote', models.BooleanField()),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hcs.scamreport')),
            ],
            options={
                'unique_together': {('report', 'ip_address')},
            },
        ),
    ]
