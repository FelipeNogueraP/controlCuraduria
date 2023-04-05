# Generated by Django 4.1.5 on 2023-04-03 21:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("control_app", "0006_rename_action_timestamp_action_id_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="BuildArea",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Cadastral",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("number", models.CharField(max_length=50)),
                ("neighborhood", models.CharField(max_length=50)),
                ("vereda", models.CharField(max_length=50)),
                ("comuna", models.CharField(max_length=30)),
                ("sector", models.CharField(max_length=30)),
                ("estrato", models.CharField(max_length=20)),
                ("corregimiento", models.CharField(max_length=50)),
                ("manzana_number", models.CharField(max_length=30)),
                ("lote_number", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="CommercialType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="GeneralData",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("responsible_office", models.CharField(max_length=50)),
                ("filing_number_location", models.IntegerField()),
                ("filing_number_curator", models.IntegerField()),
                ("filing_number_year", models.IntegerField()),
                ("filing_number_consecutive", models.IntegerField()),
                ("date", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="GeographicLocation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("department", models.CharField(max_length=50)),
                ("municipality", models.CharField(max_length=50)),
                ("vereda", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="HousingType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="InstitutionalType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="MaterialityType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="MeasureType",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Modality",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="OtherDetail",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("description", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Planimetry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="ProcedureObjective",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="Property",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("current_address", models.CharField(max_length=100)),
                ("previous_address", models.CharField(max_length=100)),
                ("real_state_reg_num", models.CharField(max_length=50)),
                (
                    "cadastral_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="control_app.cadastral",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="RatioWallCeiling",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("north", models.CharField(max_length=3)),
                ("south", models.CharField(max_length=3)),
                ("east", models.CharField(max_length=3)),
                ("west", models.CharField(max_length=3)),
                ("ceiling_height", models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name="Request",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("cultural_building", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="SoilClasification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="TypeProcedure",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name="entity_user",
            name="first_name",
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name="entity_user",
            name="last_name",
            field=models.CharField(max_length=20),
        ),
        migrations.CreateModel(
            name="Uses",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                (
                    "other_detail_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="control_app.otherdetail",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UniqueNationalForm",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "general_data_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="control_app.generaldata",
                    ),
                ),
                (
                    "property_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="control_app.property",
                    ),
                ),
                (
                    "request_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="control_app.request",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SustainableDeclaration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("water_saving_exp", models.CharField(max_length=20)),
                ("energy_saving_exp", models.CharField(max_length=20)),
                (
                    "ratio_wall_ceiling_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="control_app.ratiowallceiling",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="request",
            name="sustainable_declaration_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="control_app.sustainabledeclaration",
            ),
        ),
        migrations.CreateModel(
            name="Measure",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "measure_type_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="control_app.measuretype",
                    ),
                ),
                (
                    "other_detail_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="control_app.otherdetail",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Materiality",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "materiality_type_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="control_app.materialitytype",
                    ),
                ),
                (
                    "other_detail_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="control_app.otherdetail",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="generaldata",
            name="geographic_location_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING,
                to="control_app.geographiclocation",
            ),
        ),
    ]