# Generated by Django 2.0.2 on 2018-02-20 02:45

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import separatedvaluesfield.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DesignDocumentImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(max_length=256)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='DesignDocumentPackage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_url', models.URLField(max_length=256)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='designdocument',
            name='baseline_grid',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(40)]),
        ),
        migrations.AddField(
            model_name='designdocument',
            name='binding_method',
            field=models.CharField(blank=True, choices=[('perfect_binding', 'Perfect Binding'), ('saddle_stitch', 'Saddle Stitch'), ('case_binding', 'Case Binding'), ('coptic_stitch', 'Coptic Stitch'), ('spiral_bound', 'Spiral Bound'), ('pamphlet_stitch', 'Pamphlet Stitch'), ('stab_binding', 'Stab Binding')], max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='designdocument',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='designdocument',
            name='document_grid_x',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='designdocument',
            name='document_grid_y',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='designdocument',
            name='gutter',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='designdocument',
            name='has_assets',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='designdocument',
            name='has_download',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='designdocument',
            name='margin_bottom',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='designdocument',
            name='margin_top',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='designdocument',
            name='page_dimension_x',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='designdocument',
            name='page_dimension_y',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='designdocument',
            name='typeface',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
        migrations.AddField(
            model_name='designdocument',
            name='weights',
            field=separatedvaluesfield.models.SeparatedValuesField(blank=True, choices=[('roman_regular', 'Roman/Regular'), ('italic_oblique', 'Italic/Oblique'), ('bold', 'Bold'), ('light', 'Light'), ('condensed', 'Condensed'), ('extended', 'Extended'), ('bold_italic', 'Bold Italic'), ('bold_condensed', 'Bold Condensed'), ('bold_extended', 'Bold Extended'), ('light_condensed', 'Light Condensed'), ('light_extended', 'Light Extended'), ('bold_condensed_italic', 'Bold Condensed Italic'), ('light_condensed_italic', 'Light Condensed Italic'), ('semibold', 'Semibold'), ('semibold_condensed', 'Semibold Condensed'), ('semibold_condensed_italic', 'Semibold Condensed Italic'), ('semibold_extended', 'Semibold Extended'), ('semibold_italic', 'Semibold Italic'), ('light_italic', 'Light Italic'), ('semibold_extended_italic', 'Semibold Extended Italic'), ('black_condensed', 'Black'), ('black_condensed', 'Black Condensed'), ('black_extended', 'Black Extended'), ('black_italic', 'Black Italic'), ('black_condensed_italic', 'Black Condensed Italic'), ('black_extended_italic', 'Black Extended Italic'), ('mono', 'Mono')], max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='designdocumentpackage',
            name='design_document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.DesignDocument'),
        ),
        migrations.AddField(
            model_name='designdocumentimage',
            name='design_document',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.DesignDocument'),
        ),
    ]
