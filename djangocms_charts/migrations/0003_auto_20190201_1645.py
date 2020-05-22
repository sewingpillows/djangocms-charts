
# Generated by Django 1.11.18 on 2019-02-01 16:45


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djangocms_charts', '0002_add_chart_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chartjsbarmodel',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_charts_chartjsbarmodel', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='chartjsbarmodel',
            name='data_series_format',
            field=models.CharField(default='rows', max_length=10, verbose_name='Data series in Rows or Cols)'),
        ),
        migrations.AlterField(
            model_name='chartjsbarmodel',
            name='labels_top',
            field=models.BooleanField(default=True, help_text='here is some help', verbose_name='Labels top row'),
        ),
        migrations.AlterField(
            model_name='chartjsbarmodel',
            name='option_legendTemplate',
            field=models.CharField(blank=True, default='<ul class="<%=name.toLowerCase()%>-legend"><% for (var i=0; i<datasets.length; i++){%><li><span style="background-color:<%=datasets[i].fillColor%>"></span><%if(datasets[i].label){%><%=datasets[i].label%><%}%></li><%}%></ul>', max_length=300, verbose_name='Legend template'),
        ),
        migrations.AlterField(
            model_name='chartjsbarmodel',
            name='option_scaleGridLineColor',
            field=models.CharField(blank=True, default='rgba(0,0,0,.05)', max_length=300, verbose_name='Colour of the grid lines'),
        ),
        migrations.AlterField(
            model_name='chartjsdoughnutmodel',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_charts_chartjsdoughnutmodel', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='chartjsdoughnutmodel',
            name='data_series_format',
            field=models.CharField(default='rows', max_length=10, verbose_name='Data series in Rows or Cols)'),
        ),
        migrations.AlterField(
            model_name='chartjsdoughnutmodel',
            name='labels_top',
            field=models.BooleanField(default=True, help_text='here is some help', verbose_name='Labels top row'),
        ),
        migrations.AlterField(
            model_name='chartjsdoughnutmodel',
            name='option_animationEasing',
            field=models.CharField(blank=True, default='easeOutBounce', max_length=300, verbose_name='Animation easing effect'),
        ),
        migrations.AlterField(
            model_name='chartjsdoughnutmodel',
            name='option_legendTemplate',
            field=models.CharField(blank=True, default='<ul class="<%=name.toLowerCase()%>-legend"><% for (var i=0; i<segments.length; i++){%><li><span style="background-color:<%=segments[i].fillColor%>"></span><%if(segments[i].label){%><%=segments[i].label%><%}%></li><%}%></ul>', max_length=300, verbose_name='Legend template'),
        ),
        migrations.AlterField(
            model_name='chartjsdoughnutmodel',
            name='option_segmentStrokeColor',
            field=models.CharField(blank=True, default='#fff', max_length=300, verbose_name='The colour of each segment stroke'),
        ),
        migrations.AlterField(
            model_name='chartjslinemodel',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_charts_chartjslinemodel', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='chartjslinemodel',
            name='data_series_format',
            field=models.CharField(default='rows', max_length=10, verbose_name='Data series in Rows or Cols)'),
        ),
        migrations.AlterField(
            model_name='chartjslinemodel',
            name='labels_top',
            field=models.BooleanField(default=True, help_text='here is some help', verbose_name='Labels top row'),
        ),
        migrations.AlterField(
            model_name='chartjslinemodel',
            name='option_legendTemplate',
            field=models.CharField(blank=True, default='<ul class="<%=name.toLowerCase()%>-legend"><% for (var i=0; i<datasets.length; i++){%><li><span style="background-color:<%=datasets[i].strokeColor%>"></span><%if(datasets[i].label){%><%=datasets[i].label%><%}%></li><%}%></ul>', max_length=300, verbose_name='A legend template'),
        ),
        migrations.AlterField(
            model_name='chartjslinemodel',
            name='option_scaleGridLineColor',
            field=models.CharField(blank=True, default='rgba(0,0,0,.05)', max_length=300, verbose_name='Colour of the grid lines'),
        ),
        migrations.AlterField(
            model_name='chartjspiemodel',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_charts_chartjspiemodel', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='chartjspiemodel',
            name='data_series_format',
            field=models.CharField(default='rows', max_length=10, verbose_name='Data series in Rows or Cols)'),
        ),
        migrations.AlterField(
            model_name='chartjspiemodel',
            name='labels_top',
            field=models.BooleanField(default=True, help_text='here is some help', verbose_name='Labels top row'),
        ),
        migrations.AlterField(
            model_name='chartjspiemodel',
            name='option_animationEasing',
            field=models.CharField(blank=True, default='easeOutBounce', max_length=300, verbose_name='Animation easing effect'),
        ),
        migrations.AlterField(
            model_name='chartjspiemodel',
            name='option_legendTemplate',
            field=models.CharField(blank=True, default='<ul class="<%=name.toLowerCase()%>-legend"><% for (var i=0; i<segments.length; i++){%><li><span style="background-color:<%=segments[i].fillColor%>"></span><%if(segments[i].label){%><%=segments[i].label%><%}%></li><%}%></ul>', max_length=300, verbose_name='Legend template'),
        ),
        migrations.AlterField(
            model_name='chartjspiemodel',
            name='option_segmentStrokeColor',
            field=models.CharField(blank=True, default='#fff', max_length=300, verbose_name='The colour of each segment stroke'),
        ),
        migrations.AlterField(
            model_name='chartjspolarmodel',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_charts_chartjspolarmodel', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='chartjspolarmodel',
            name='data_series_format',
            field=models.CharField(default='rows', max_length=10, verbose_name='Data series in Rows or Cols)'),
        ),
        migrations.AlterField(
            model_name='chartjspolarmodel',
            name='labels_top',
            field=models.BooleanField(default=True, help_text='here is some help', verbose_name='Labels top row'),
        ),
        migrations.AlterField(
            model_name='chartjspolarmodel',
            name='option_animationEasing',
            field=models.CharField(blank=True, default='easeOutBounce', max_length=300, verbose_name='Animation easing effect.'),
        ),
        migrations.AlterField(
            model_name='chartjspolarmodel',
            name='option_legendTemplate',
            field=models.CharField(blank=True, default='<ul class="<%=name.toLowerCase()%>-legend"><% for (var i=0; i<segments.length; i++){%><li><span style="background-color:<%=segments[i].fillColor%>"></span><%if(segments[i].label){%><%=segments[i].label%><%}%></li><%}%></ul>', max_length=300, verbose_name='A legend template'),
        ),
        migrations.AlterField(
            model_name='chartjspolarmodel',
            name='option_scaleBackdropColor',
            field=models.CharField(blank=True, default='rgba(255,255,255,0.75)', max_length=300, verbose_name='The colour of the label backdrop'),
        ),
        migrations.AlterField(
            model_name='chartjspolarmodel',
            name='option_segmentStrokeColor',
            field=models.CharField(blank=True, default='#fff', max_length=300, verbose_name='The colour of the stroke on each segement.'),
        ),
        migrations.AlterField(
            model_name='chartjsradarmodel',
            name='cmsplugin_ptr',
            field=models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='djangocms_charts_chartjsradarmodel', serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='chartjsradarmodel',
            name='data_series_format',
            field=models.CharField(default='rows', max_length=10, verbose_name='Data series in Rows or Cols)'),
        ),
        migrations.AlterField(
            model_name='chartjsradarmodel',
            name='labels_top',
            field=models.BooleanField(default=True, help_text='here is some help', verbose_name='Labels top row'),
        ),
        migrations.AlterField(
            model_name='chartjsradarmodel',
            name='option_angleLineColor',
            field=models.CharField(blank=True, default='rgba(0,0,0,.1)', max_length=300, verbose_name='Colour of the angle line'),
        ),
        migrations.AlterField(
            model_name='chartjsradarmodel',
            name='option_legendTemplate',
            field=models.CharField(blank=True, default='<ul class="<%=name.toLowerCase()%>-legend"><% for (var i=0; i<datasets.length; i++){%><li><span style="background-color:<%=datasets[i].strokeColor%>"></span><%if(datasets[i].label){%><%=datasets[i].label%><%}%></li><%}%></ul>', max_length=300, verbose_name='Legend template'),
        ),
        migrations.AlterField(
            model_name='chartjsradarmodel',
            name='option_pointLabelFontColor',
            field=models.CharField(blank=True, default='#666', max_length=300, verbose_name='Point label font colour'),
        ),
        migrations.AlterField(
            model_name='chartjsradarmodel',
            name='option_pointLabelFontFamily',
            field=models.CharField(blank=True, default="'Arial'", max_length=300, verbose_name='Point label font declaration'),
        ),
        migrations.AlterField(
            model_name='chartjsradarmodel',
            name='option_pointLabelFontStyle',
            field=models.CharField(blank=True, default='normal', max_length=300, verbose_name='Point label font weight'),
        ),
    ]
