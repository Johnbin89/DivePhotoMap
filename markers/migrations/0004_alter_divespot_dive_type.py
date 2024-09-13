# Generated by Django 5.0.6 on 2024-09-13 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markers', '0003_alter_marker_divespot'),
    ]

    operations = [
        migrations.AlterField(
            model_name='divespot',
            name='dive_type',
            field=models.CharField(choices=[('Reef', 'Reef'), ('Wall', 'Wall'), ('Wreck', 'Wreck'), ('Aircraft', 'Aircraft'), ('Cave', 'Cave'), ('Cavern', 'Cavern'), ('Open Water', 'Open Water')], default='Open Water', max_length=30),
        ),
    ]
