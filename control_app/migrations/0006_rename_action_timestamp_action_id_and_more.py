# Generated by Django 4.1.5 on 2023-03-23 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("control_app", "0005_rename_action_id_timestamp_action_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="timestamp",
            old_name="action",
            new_name="action_id",
        ),
        migrations.RenameField(
            model_name="timestamp",
            old_name="user",
            new_name="user_id",
        ),
        migrations.AlterField(
            model_name="timestamp",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
