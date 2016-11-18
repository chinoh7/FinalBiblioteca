# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=40)),
                ('descripcion', models.CharField(max_length=40)),
                ('telefono', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='InfoLibro',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('autor', models.ForeignKey(to='biblioteca.Autor')),
                ('editoria', models.ForeignKey(to='biblioteca.Editorial')),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('titulo', models.CharField(max_length=30)),
                ('portada', models.CharField(max_length=15)),
                ('fecha_publicacion', models.DateField()),
                ('autor', models.ForeignKey(to='biblioteca.Autor')),
                ('editoria', models.ForeignKey(to='biblioteca.Editorial')),
            ],
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nombre', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamos',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('fecha_prestamo', models.DateField()),
                ('fecha_devolución', models.DateField()),
                ('libro', models.ForeignKey(to='biblioteca.Libro')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('nombres', models.CharField(max_length=40)),
                ('apellidos', models.CharField(max_length=40)),
                ('dpi', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='prestamos',
            name='usaurio',
            field=models.ForeignKey(to='biblioteca.Usuario'),
        ),
        migrations.AddField(
            model_name='libro',
            name='pais',
            field=models.ForeignKey(to='biblioteca.Pais'),
        ),
        migrations.AddField(
            model_name='infolibro',
            name='libro',
            field=models.ForeignKey(to='biblioteca.Libro'),
        ),
        migrations.AddField(
            model_name='infolibro',
            name='pais',
            field=models.ForeignKey(to='biblioteca.Pais'),
        ),
    ]
