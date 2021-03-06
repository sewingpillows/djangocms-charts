# Generated by Django 2.2.16 on 2020-10-12 22:19

from django.db import migrations, models
import django.db.models.deletion
import djangocms_charts.models_datasets


class Migration(migrations.Migration):
    dependencies = [
        ('djangocms_charts', '0008_set_new_chart_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chartjsdoughnutmodel',
            name='cmsplugin_ptr',
        ),
        migrations.RemoveField(
            model_name='chartjsglobalsettingsmodel',
            name='site',
        ),
        migrations.RemoveField(
            model_name='chartjslinemodel',
            name='cmsplugin_ptr',
        ),
        migrations.RemoveField(
            model_name='chartjspiemodel',
            name='cmsplugin_ptr',
        ),
        migrations.RemoveField(
            model_name='chartjspolarmodel',
            name='cmsplugin_ptr',
        ),
        migrations.RemoveField(
            model_name='chartjsradarmodel',
            name='cmsplugin_ptr',
        ),
        migrations.DeleteModel(
            name='ChartJsBarModel',
        ),
        migrations.DeleteModel(
            name='ChartJsDoughnutModel',
        ),
        migrations.DeleteModel(
            name='ChartJsGlobalSettingsModel',
        ),
        migrations.DeleteModel(
            name='ChartJsLineModel',
        ),
        migrations.DeleteModel(
            name='ChartJsPieModel',
        ),
        migrations.DeleteModel(
            name='ChartJsPolarModel',
        ),
        migrations.DeleteModel(
            name='ChartJsRadarModel',
        ),
    ]
