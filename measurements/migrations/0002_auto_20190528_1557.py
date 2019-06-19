# Generated by Django 2.2.1 on 2019-05-28 15:57

from django.db import migrations

def load_sources(apps, schema_editor):
    SourceType = apps.get_model('measurements', 'SourceType')
    SourceType.objects.create(code="pessl")
    SourceType.objects.create(code="mtt")
    SourceType.objects.create(code="elmed")
    SourceType.objects.create(code="davis")

class Migration(migrations.Migration):

    dependencies = [
        ('measurements', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_sources)
    ]
