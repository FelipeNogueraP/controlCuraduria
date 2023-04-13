# Generated by Django 4.1.5 on 2023-04-12 22:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "control_app",
            "0004_licenceholderresponsible_electronic_notification_and_more",
        ),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="bordersdimensionareas",
            options={"verbose_name_plural": "Borders Dimension Areas"},
        ),
        migrations.AlterModelOptions(
            name="generaldata",
            options={"verbose_name_plural": "General Data"},
        ),
        migrations.AlterModelOptions(
            name="materiality",
            options={"verbose_name_plural": "Materialities"},
        ),
        migrations.AlterModelOptions(
            name="modality",
            options={"verbose_name_plural": "Modalities"},
        ),
        migrations.AlterModelOptions(
            name="planimetry",
            options={"verbose_name_plural": "Planimetries"},
        ),
        migrations.AlterModelOptions(
            name="property",
            options={"verbose_name": "Property", "verbose_name_plural": "Properties"},
        ),
        migrations.AlterModelOptions(
            name="uses",
            options={"verbose_name_plural": "Uses"},
        ),
        migrations.AddField(
            model_name="document",
            name="mandatory",
            field=models.BooleanField(default=True, verbose_name="¿Obligatorio?"),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="BrUniqueNationalFormNeighbor",
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
                    "neighbor_id",
                    models.ManyToManyField(
                        related_name="Neighbor Id+", to="control_app.neighbor"
                    ),
                ),
                (
                    "unique_national_form_id",
                    models.ManyToManyField(
                        related_name="Unique National Form Id+",
                        to="control_app.uniquenationalform",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BrTypeProcedureModality",
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
                    "modality_id",
                    models.ManyToManyField(
                        related_name="Modality Id+", to="control_app.modality"
                    ),
                ),
                (
                    "type_procedure_id",
                    models.ManyToManyField(
                        related_name="Type Procedure Id+",
                        to="control_app.typeprocedure",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BrSustainableDeclarationMeasure",
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
                    "measure_id",
                    models.ManyToManyField(
                        related_name="Measure Id+", to="control_app.measure"
                    ),
                ),
                (
                    "sustainable_declaration_id",
                    models.ManyToManyField(
                        related_name="Sustainable Declaration Id+",
                        to="control_app.sustainabledeclaration",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BrSustainableDeclarationMateriality",
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
                    "materiality_id",
                    models.ManyToManyField(
                        related_name="Materiality Id+", to="control_app.materiality"
                    ),
                ),
                (
                    "sustainable_declaration_id",
                    models.ManyToManyField(
                        related_name="Sustainable Declaration Id+",
                        to="control_app.sustainabledeclaration",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BrRequestUses",
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
                    "other_detail_id",
                    models.ManyToManyField(
                        related_name="Other detail+", to="control_app.otherdetail"
                    ),
                ),
                (
                    "request_id",
                    models.ManyToManyField(
                        related_name="Request Id+", to="control_app.request"
                    ),
                ),
                (
                    "type_uses_id",
                    models.ManyToManyField(
                        related_name="Type Uses Id+", to="control_app.request"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BrRequestTypeProcedure",
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
                    "request_id",
                    models.ManyToManyField(
                        related_name="Request Id+", to="control_app.request"
                    ),
                ),
                (
                    "type_procedure_id",
                    models.ManyToManyField(
                        related_name="Type Procedure Id+", to="control_app.request"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BrRequestProcedureObjective",
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
                    "other_detail_id",
                    models.ManyToManyField(
                        related_name="Other Detail Id+", to="control_app.otherdetail"
                    ),
                ),
                (
                    "procedure_objective_id",
                    models.ManyToManyField(
                        related_name="Procedure Objective Id+", to="control_app.request"
                    ),
                ),
                (
                    "request_id",
                    models.ManyToManyField(
                        related_name="Request Id+", to="control_app.request"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BrRequestInstitutionalType",
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
                    "institutional_type_id",
                    models.ManyToManyField(
                        related_name="Institutional Type Id+",
                        to="control_app.institutionaltype",
                    ),
                ),
                (
                    "other_detail_id",
                    models.ManyToManyField(
                        related_name="Other Detail+", to="control_app.otherdetail"
                    ),
                ),
                (
                    "request_id",
                    models.ManyToManyField(
                        related_name="Request Id+", to="control_app.request"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BrRequestHousingType",
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
                    "housing_type_id",
                    models.ManyToManyField(
                        related_name="Housing Type Id+", to="control_app.request"
                    ),
                ),
                (
                    "request_id",
                    models.ManyToManyField(
                        related_name="Request Id+", to="control_app.request"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BrRequestCommercialType",
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
                    "commercial_type_id",
                    models.ManyToManyField(
                        related_name="Commercial Type Id+",
                        to="control_app.commercialtype",
                    ),
                ),
                (
                    "other_detail_id",
                    models.ManyToManyField(
                        related_name="Other Detail Id+", to="control_app.otherdetail"
                    ),
                ),
                (
                    "request_id",
                    models.ManyToManyField(
                        related_name="Request Id+", to="control_app.request"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BrRequestBuildArea",
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
                    "build_area_id",
                    models.ManyToManyField(
                        related_name="Build Area Id+", to="control_app.buildarea"
                    ),
                ),
                (
                    "request_id",
                    models.ManyToManyField(
                        related_name="Request Id+", to="control_app.request"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BrPropertySoilClasification",
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
                    "property_id",
                    models.ManyToManyField(
                        related_name="Property Id+", to="control_app.property"
                    ),
                ),
                (
                    "soil_clasification_id",
                    models.ManyToManyField(
                        related_name="Soil Clasification Id+",
                        to="control_app.soilclasification",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BrPropertyPlanimetry",
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
                    "planimetry_id",
                    models.ManyToManyField(
                        related_name="Planimetry Id+", to="control_app.planimetry"
                    ),
                ),
                (
                    "property_id",
                    models.ManyToManyField(
                        related_name="Property Id+", to="control_app.property"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="BrDocumentTypeProcedureModality",
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
                    "document_id",
                    models.ManyToManyField(
                        related_name="Document Id+", to="control_app.document"
                    ),
                ),
                (
                    "modality_id",
                    models.ManyToManyField(
                        related_name="Modality Id+", to="control_app.modality"
                    ),
                ),
                (
                    "type_procedure_id",
                    models.ManyToManyField(
                        related_name="TypeProcedure Id+", to="control_app.typeprocedure"
                    ),
                ),
            ],
        ),
    ]