# Generated by Django 4.1 on 2022-11-01 16:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campaign', '0003_remove_campaign_user'),
        ('donate', '0002_donasi_campaign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donasi',
            name='campaign',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='campaign.campaign', to_field='title'),
        ),
    ]
