# Generated by Django 4.2.4 on 2023-10-17 19:09
from django.db import migrations
from guardian.ctypes import get_content_type


def assign_view_plugin(apps, schema_editor):
    Group = apps.get_model("auth", "Group")
    Plugin = apps.get_model("models", "Plugin")
    Permission = apps.get_model("auth", "Permission")
    GroupObjectPermission = apps.get_model("guardian", "GroupObjectPermission")

    view_plugin = Permission.objects.get(codename="view_plugin")
    resource_reviewers = Group.objects.get(name="Resource Reviewer")
    plugins = Plugin.objects.all()

    # Cannot use django_guardian shortcuts or object managers
    # https://github.com/django-guardian/django-guardian/issues/751
    GroupObjectPermission.objects.bulk_create(
        [
            GroupObjectPermission(
                permission=view_plugin,
                group=resource_reviewers,
                content_type_id=get_content_type(plugin).pk,
                object_pk=plugin.pk,
            )
            for plugin in plugins
        ],
        ignore_conflicts=True,
    )


class Migration(migrations.Migration):
    dependencies = [
        ("arches_for_science", "0001_initial"),
        ("guardian", "0002_generic_permissions_index"),
    ]

    operations = [
        migrations.RunPython(assign_view_plugin, migrations.RunPython.noop),
    ]
