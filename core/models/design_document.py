from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

from separatedvaluesfield.models import SeparatedValuesField
from core.misc.fonts.formatted_fonts import fonts

weight_choices = (
    ('roman_regular', 'Roman/Regular'),
    ('italic_oblique', 'Italic/Oblique'),
    ('bold', 'Bold'),
    ('light', 'Light'),
    ('condensed', 'Condensed'),
    ('extended', 'Extended'),
    ('bold_italic', 'Bold Italic'),
    ('bold_condensed', 'Bold Condensed'),
    ('bold_extended', 'Bold Extended'),
    ('light_condensed', 'Light Condensed'),
    ('light_extended', 'Light Extended'),
    ('bold_condensed_italic', 'Bold Condensed Italic'),
    ('light_condensed_italic', 'Light Condensed Italic'),
    ('semibold', 'Semibold'),
    ('semibold_condensed', 'Semibold Condensed'),
    ('semibold_condensed_italic', 'Semibold Condensed Italic'),
    ('semibold_extended', 'Semibold Extended'),
    ('semibold_italic', 'Semibold Italic'),
    ('light_italic', 'Light Italic'),
    ('semibold_extended_italic', 'Semibold Extended Italic'),
    ('black_condensed', 'Black'),
    ('black_condensed', 'Black Condensed'),
    ('black_extended', 'Black Extended'),
    ('black_italic', 'Black Italic'),
    ('black_condensed_italic', 'Black Condensed Italic'),
    ('black_extended_italic', 'Black Extended Italic'),
    ('mono', 'Mono'),
)

binding_choices = (
    ('perfect_binding', 'Perfect Binding'),
    ('saddle_stitch', 'Saddle Stitch'),
    ('case_binding', 'Case Binding'),
    ('coptic_stitch', 'Coptic Stitch'),
    ('spiral_bound', 'Spiral Bound'),
    ('pamphlet_stitch', 'Pamphlet Stitch'),
    ('stab_binding', 'Stab Binding')
)

class DesignDocument(models.Model):
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    has_download = models.BooleanField(default=False)
    has_assets = models.BooleanField(default=False)
    baseline_grid = models.PositiveIntegerField(
        validators=[MaxValueValidator(40)],
        null=True,
        blank=True
    )
    document_grid_x = models.PositiveIntegerField(null=True, blank=True)
    document_grid_y = models.PositiveIntegerField(null=True, blank=True)
    gutter = models.PositiveIntegerField(null=True, blank=True)
    page_dimension_x = models.PositiveIntegerField(null=True, blank=True)
    page_dimension_y = models.PositiveIntegerField(null=True, blank=True)
    margin_top = models.PositiveIntegerField(null=True, blank=True)
    margin_bottom = models.PositiveIntegerField(null=True, blank=True)
    typefaces = SeparatedValuesField(choices=fonts, token=',', max_length=64, null=True, blank=True)
    weights = SeparatedValuesField(choices=weight_choices, token=',', max_length=150, null=True, blank=True)
    binding_method = models.CharField(choices=binding_choices, max_length=128, null=True, blank=True)

    def is_favorited(self, user):
        """Returns a boolean telling us if the relevant user has favorited this document"""
        from core.models import UserDocumentFavorite

        return UserDocumentFavorite.objects.filter(user=user, design_document=self).exists()

    @staticmethod
    def format_measurement(dimension1, dimension2, units=""):
        if dimension1 and dimension2:
            return "%s x %s %s" % (dimension1, dimension2, units)

        return 'NA'

    @property
    def baseline_grid_display(self):
        if not self.baseline_grid:
            return 'NA'

        return "%s pts." % (self.baseline_grid,)

    @property
    def margins_top_bottom(self):
        if not self.margin_top or not self.margin_bottom:
            return "NA"

        return "%s / %s in." % (self.margin_top, self.margin_bottom)

    @property
    def document_grid(self):
        return self.format_measurement(self.document_grid_x, self.document_grid_y)

    @property
    def page_dimensions(self):

        return self.format_measurement(self.page_dimension_x, self.page_dimension_y, "in.")
