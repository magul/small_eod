# Generated by Django 3.0.6 on 2020-05-28 09:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0003_Plural_form_features'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='featureoption',
            name='features',
        ),
        migrations.AddField(
            model_name='featureoption',
            name='feature',
            field=models.ForeignKey(default='', help_text='Related feature.', on_delete=django.db.models.deletion.CASCADE, related_name='featureoptions', to='features.Feature', verbose_name='Feature'),
            preserve_default=False,
        ),
    ]
