# Generated by Django 4.2.4 on 2023-11-17 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("arches_for_science", "0002_view_plugin_permission"),
    ]

    operations = [
        migrations.CreateModel(
            name="CanvasXDigitalResource",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("canvas", models.TextField(unique=True)),
                ("digitalresource", models.TextField(unique=True)),
            ],
            options={
                "db_table": "canvas_x_digitalresource",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="ManifestXCanvas",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("manifest", models.TextField()),
                ("canvas", models.TextField()),
            ],
            options={
                "db_table": "manifest_x_canvas",
                "managed": True,
            },
        ),
        migrations.CreateModel(
            name="ManifestXDigitalResource",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("manifest", models.TextField(unique=True)),
                ("digitalresource", models.TextField(unique=True)),
            ],
            options={
                "db_table": "manifest_x_digitalresource",
                "managed": True,
            },
        ),
    ]
