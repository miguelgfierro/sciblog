from django.contrib import admin
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django import forms
from libs.ckeditor.widgets import CKEditorWidget
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    """Post administrator. It manages the Post model."""

    fieldsets = [
        (None, {"fields": ["title"]}),
        ("Description", {"fields": ["meta_description"]}),
        ("Keywords (lowercase)", {"fields": ["keywords"]}),
        ("Author(s)", {"fields": ["authors"]}),
        ("Date information", {"fields": ["pub_date"]}),
        ("Abstract", {"fields": ["abstract"]}),
        ("Site", {"fields": ["site"]}),
        # Activate the formulas, if true mathjax.js is included in template (better for SEO)
        ("Post with formulas", {"fields": ["has_latex_formula"]},),
        ("Content", {"fields": ["content"]}),
    ]
    list_display = ("title", "pub_date", "was_published_recently")
    list_filter = ["pub_date"]
    search_fields = ["title"]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


class ExtendedFlatPageForm(FlatpageForm):
    """Extended FlatPageForm. It adds the CKEditor widget."""

    locals()["content"] = forms.CharField(
        widget=CKEditorWidget(), required=False, label=(u"Content")
    )

    class Meta:
        model = FlatPage
        fields = "__all__"


class ExtendedFlatPageAdmin(FlatPageAdmin):
    """ExtendedFlatPageAdmin class. It manages the ExtendedFlatPageForm."""

    form = ExtendedFlatPageForm
    fieldsets = (
        (None, {"fields": ("url", "title", "content", "sites", "template_name",)}),
    )


admin.site.unregister(FlatPage)
admin.site.register(FlatPage, ExtendedFlatPageAdmin)
admin.site.register(Post, PostAdmin)
