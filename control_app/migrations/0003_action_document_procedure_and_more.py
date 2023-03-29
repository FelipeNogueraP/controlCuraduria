# Generated by Django 4.1.5 on 2023-03-09 22:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("control_app", "0002_entity_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="Action",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Document",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=20)),
                ("description", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Procedure",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("procedure_type", models.CharField(max_length=50)),
                (
                    "document",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="control_app.document",
                    ),
                ),
            ],
        ),
        migrations.RenameField(
            model_name="entity_user",
            old_name="firs_name",
            new_name="first_name",
        ),
        migrations.CreateModel(
            name="TimeStamp",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "action_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="control_app.action",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="control_app.entity_user",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RolePermissions",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "action_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="control_app.action",
                    ),
                ),
                (
                    "procedure_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="control_app.procedure",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Role",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=20)),
                ("description", models.CharField(max_length=200)),
                (
                    "permissions",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="control_app.rolepermissions",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="procedure",
            name="user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="control_app.entity_user",
            ),
        ),
    ]
