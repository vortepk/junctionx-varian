# Generated by Django 4.1 on 2023-11-25 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("doctor", "0002_bed_floor_room_timeslot_remove_machine_family_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="patient",
            name="priority",
            field=models.BooleanField(blank=True, max_length=1024, null=True),
        ),
    ]
