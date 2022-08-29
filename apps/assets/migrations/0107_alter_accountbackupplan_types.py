# Generated by Django 3.2.13 on 2022-08-29 11:46
from django.db import migrations, models

from assets.const import Category
from assets.models import Type


def update_account_backup_type(apps, schema_editor):
    backup_model = apps.get_model('assets', 'AccountBackupPlan')
    all_number = 4294967295
    asset_number = Type.choices_to_value([Category.HOST])
    app_number = Type.choices_to_value([
        Category.NETWORKING, Category.DATABASE, Category.CLOUD, Category.WEB]
    )

    backup_model.objects.filter(types=255).update(types=all_number)
    backup_model.objects.filter(types=1).update(types=asset_number)
    backup_model.objects.filter(types=2).update(types=app_number)

    backup_execution_model = apps.get_model('assets', 'AccountBackupPlanExecution')
    choices_dict = {
        'all': Type.get_types(value=all_number),
        'asset': Type.get_types(value=asset_number),
        'app': Type.get_types(value=app_number)
    }
    qs_dict = {
        'all': backup_execution_model.objects.filter(plan__types=255),
        'asset': backup_execution_model.objects.filter(plan__types=1),
        'app': backup_execution_model.objects.filter(plan__types=2)
    }

    backup_executions = []
    for k, qs in qs_dict.items():
        type_choices = choices_dict[k]
        for i in qs:
            i.plan_snapshot['types'] = type_choices
            backup_executions.append(i)
    backup_execution_model.objects.bulk_update(backup_executions, fields=['plan_snapshot'])


class Migration(migrations.Migration):
    dependencies = [
        ('assets', '0106_auto_20220819_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountbackupplan',
            name='types',
            field=models.BigIntegerField(
                choices=[(4294967295, 'All'), (1, 'Linux'), (2, 'Windows'), (4, 'Unix'), (8, 'BSD'), (16, 'MacOS'),
                         (32, 'Mainframe'), (64, 'Other host'), (127, 'Host'), (128, 'Switch'), (256, 'Router'),
                         (512, 'Firewall'), (1024, 'Other device'), (1920, 'NetworkDevice'), (2048, 'MySQL'),
                         (4096, 'MariaDB'), (8192, 'PostgreSQL'), (16384, 'Oracle'), (32768, 'SQLServer'),
                         (65536, 'MongoDB'), (131072, 'Redis'), (260096, 'Database'), (262144, 'Clouding'),
                         (524288, 'Web')], default=4294967295, verbose_name='Type'),
        ),
        migrations.RunPython(update_account_backup_type),
    ]
