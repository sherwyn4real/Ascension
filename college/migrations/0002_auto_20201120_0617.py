# Generated by Django 3.1.3 on 2020-11-20 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.CharField(help_text='info about course', max_length=50)),
                ('course_type', models.CharField(blank=True, choices=[('e', 'Engineering'), ('m', 'Medical')], default='e', max_length=1)),
                ('course_name', models.CharField(blank=True, choices=[('comp', 'Computer Engineering'), ('it', 'Information Technology'), ('mech', 'Mechanical Engineering'), ('etc', 'Electronic and Telecomunication'), ('mbbs', 'MBBS'), ('den', 'Bachelor Dental Science')], default='e', max_length=5)),
            ],
        ),
        migrations.DeleteModel(
            name='Courses',
        ),
        migrations.AlterField(
            model_name='usercollege',
            name='course',
            field=models.ManyToManyField(to='college.Course'),
        ),
    ]
