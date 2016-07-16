# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-15 15:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Databases',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='TTP001', null=True, verbose_name='MDL001')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='TTP002', null=True, verbose_name='MDL002')),
                ('name', models.CharField(help_text='TTP003', max_length=100, verbose_name='MDL003')),
                ('description', models.TextField(blank=True, help_text='TTP004', null=True, verbose_name='MDL004')),
                ('site', models.URLField(blank=True, help_text='TTP009', null=True, verbose_name='MDL009')),
                ('proficiency', models.PositiveIntegerField(help_text='TTP010', verbose_name='MDL010')),
                ('sql', models.BooleanField(default=True, help_text='TTP013', verbose_name='MDL013')),
            ],
            options={
                'verbose_name': 'MTA007',
                'verbose_name_plural': 'MTA008',
            },
        ),
        migrations.CreateModel(
            name='Frameworks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='TTP001', null=True, verbose_name='MDL001')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='TTP002', null=True, verbose_name='MDL002')),
                ('name', models.CharField(help_text='TTP003', max_length=100, verbose_name='MDL003')),
                ('description', models.TextField(blank=True, help_text='TTP004', null=True, verbose_name='MDL004')),
                ('site', models.URLField(blank=True, help_text='TTP009', null=True, verbose_name='MDL009')),
                ('proficiency', models.PositiveIntegerField(help_text='TTP010', verbose_name='MDL010')),
            ],
            options={
                'verbose_name': 'MTA005',
                'verbose_name_plural': 'MTA006',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='TTP001', null=True, verbose_name='MDL001')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='TTP002', null=True, verbose_name='MDL002')),
                ('name', models.CharField(help_text='TTP003', max_length=100, verbose_name='MDL003')),
                ('description', models.TextField(blank=True, help_text='TTP004', null=True, verbose_name='MDL004')),
                ('title', models.TextField(blank=True, help_text='TTP005', null=True, verbose_name='MDL005')),
                ('image_string', models.TextField(help_text='TTP006', verbose_name='MDL006')),
                ('mimetype', models.TextField(help_text='TTP007', verbose_name='MDL007')),
                ('extension', models.TextField(help_text='TTP008', verbose_name='MDL008')),
            ],
            options={
                'verbose_name': 'MTA001',
                'verbose_name_plural': 'MTA002',
            },
        ),
        migrations.CreateModel(
            name='ProgrammingLanguages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='TTP001', null=True, verbose_name='MDL001')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='TTP002', null=True, verbose_name='MDL002')),
                ('name', models.CharField(help_text='TTP003', max_length=100, verbose_name='MDL003')),
                ('description', models.TextField(blank=True, help_text='TTP004', null=True, verbose_name='MDL004')),
                ('site', models.URLField(blank=True, help_text='TTP009', null=True, verbose_name='MDL009')),
                ('proficiency', models.PositiveIntegerField(help_text='TTP010', verbose_name='MDL010')),
                ('logo', models.OneToOneField(blank=True, help_text='TTP011', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='portfolio.Image', verbose_name='MDL011')),
            ],
            options={
                'verbose_name': 'MTA003',
                'verbose_name_plural': 'MTA004',
            },
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='TTP001', null=True, verbose_name='MDL001')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='TTP002', null=True, verbose_name='MDL002')),
                ('name', models.CharField(help_text='TTP003', max_length=100, verbose_name='MDL003')),
                ('description', models.TextField(blank=True, help_text='TTP004', null=True, verbose_name='MDL004')),
                ('database', models.ManyToManyField(blank=True, help_text='TTP018', to='portfolio.Databases', verbose_name='MDL018')),
                ('framework', models.ManyToManyField(blank=True, help_text='TTP017', to='portfolio.Frameworks', verbose_name='MDL017')),
                ('images', models.ManyToManyField(blank=True, help_text='TTP020', to='portfolio.Image', verbose_name='MDL020')),
                ('programming_language', models.ManyToManyField(help_text='TTP01', to='portfolio.ProgrammingLanguages', verbose_name='MDL01')),
            ],
            options={
                'verbose_name': 'MTA017',
                'verbose_name_plural': 'MTA018',
            },
        ),
        migrations.CreateModel(
            name='ProjectTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='TTP001', null=True, verbose_name='MDL001')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='TTP002', null=True, verbose_name='MDL002')),
                ('name', models.CharField(help_text='TTP003', max_length=100, verbose_name='MDL003')),
                ('description', models.TextField(blank=True, help_text='TTP004', null=True, verbose_name='MDL004')),
            ],
            options={
                'verbose_name': 'MTA015',
                'verbose_name_plural': 'MTA016',
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='TTP001', null=True, verbose_name='MDL001')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='TTP002', null=True, verbose_name='MDL002')),
                ('name', models.CharField(help_text='TTP003', max_length=100, verbose_name='MDL003')),
                ('description', models.TextField(blank=True, help_text='TTP004', null=True, verbose_name='MDL004')),
                ('type', models.CharField(choices=[('ED', 'MDL022'), ('XP', 'MDL023'), ('AW', 'MDL024')], default='ED', help_text='TTP025', max_length=2, verbose_name='MDL025')),
                ('start_year', models.PositiveIntegerField(choices=[(1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016)], default=2016, help_text='TTP027', verbose_name='MDL027')),
                ('end_year', models.PositiveIntegerField(choices=[(1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016)], default=2016, help_text='TTP029', verbose_name='MDL029')),
                ('title', models.CharField(help_text='MDL030', max_length=100, null=True, verbose_name='MDL030')),
                ('en_title', models.CharField(help_text='MDL031', max_length=100, null=True, verbose_name='MDL031')),
                ('where', models.TextField(help_text='MDL032', verbose_name='MDL032')),
            ],
            options={
                'verbose_name': 'MTA019',
            },
        ),
        migrations.CreateModel(
            name='Technologies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='TTP001', null=True, verbose_name='MDL001')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='TTP002', null=True, verbose_name='MDL002')),
                ('name', models.CharField(help_text='TTP003', max_length=100, verbose_name='MDL003')),
                ('description', models.TextField(blank=True, help_text='TTP004', null=True, verbose_name='MDL004')),
                ('site', models.URLField(blank=True, help_text='TTP009', null=True, verbose_name='MDL009')),
                ('proficiency', models.PositiveIntegerField(help_text='TTP010', verbose_name='MDL010')),
                ('logo', models.OneToOneField(blank=True, help_text='TTP011', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='portfolio.Image', verbose_name='MDL011')),
            ],
            options={
                'verbose_name': 'MTA013',
                'verbose_name_plural': 'MTA014',
            },
        ),
        migrations.CreateModel(
            name='TechnologyTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='TTP001', null=True, verbose_name='MDL001')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='TTP002', null=True, verbose_name='MDL002')),
                ('name', models.CharField(help_text='TTP003', max_length=100, verbose_name='MDL003')),
                ('description', models.TextField(blank=True, help_text='TTP004', null=True, verbose_name='MDL004')),
                ('site', models.URLField(blank=True, help_text='TTP009', null=True, verbose_name='MDL009')),
                ('proficiency', models.PositiveIntegerField(help_text='TTP010', verbose_name='MDL010')),
                ('logo', models.OneToOneField(blank=True, help_text='TTP011', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='portfolio.Image', verbose_name='MDL011')),
            ],
            options={
                'verbose_name': 'MTA011',
                'verbose_name_plural': 'MTA012',
            },
        ),
        migrations.CreateModel(
            name='WebServers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='TTP001', null=True, verbose_name='MDL001')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='TTP002', null=True, verbose_name='MDL002')),
                ('name', models.CharField(help_text='TTP003', max_length=100, verbose_name='MDL003')),
                ('description', models.TextField(blank=True, help_text='TTP004', null=True, verbose_name='MDL004')),
                ('site', models.URLField(blank=True, help_text='TTP009', null=True, verbose_name='MDL009')),
                ('proficiency', models.PositiveIntegerField(help_text='TTP010', verbose_name='MDL010')),
                ('logo', models.OneToOneField(blank=True, help_text='TTP011', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='portfolio.Image', verbose_name='MDL011')),
            ],
            options={
                'verbose_name': 'MTA009',
                'verbose_name_plural': 'MTA010',
            },
        ),
        migrations.AddField(
            model_name='technologies',
            name='type',
            field=models.ForeignKey(help_text='TTP014', on_delete=django.db.models.deletion.CASCADE, to='portfolio.TechnologyTypes', verbose_name='MDL014'),
        ),
        migrations.AddField(
            model_name='projects',
            name='technology',
            field=models.ManyToManyField(blank=True, help_text='TTP019', to='portfolio.Technologies', verbose_name='MDL019'),
        ),
        migrations.AddField(
            model_name='projects',
            name='type',
            field=models.ForeignKey(help_text='TTP015', on_delete=django.db.models.deletion.CASCADE, to='portfolio.ProjectTypes', verbose_name='MDL015'),
        ),
        migrations.AddField(
            model_name='projects',
            name='webserver',
            field=models.ManyToManyField(blank=True, help_text='TTP020', to='portfolio.WebServers', verbose_name='MDL020'),
        ),
        migrations.AddField(
            model_name='frameworks',
            name='language',
            field=models.ForeignKey(help_text='TTP012', on_delete=django.db.models.deletion.CASCADE, to='portfolio.ProgrammingLanguages', verbose_name='MDL012'),
        ),
        migrations.AddField(
            model_name='frameworks',
            name='logo',
            field=models.OneToOneField(blank=True, help_text='TTP011', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='portfolio.Image', verbose_name='MDL011'),
        ),
        migrations.AddField(
            model_name='databases',
            name='logo',
            field=models.OneToOneField(blank=True, help_text='TTP011', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='portfolio.Image', verbose_name='MDL011'),
        ),
    ]