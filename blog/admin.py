from django.contrib import admin
from blog.models import Post, RichTextFlatPage
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               	{'fields': ['title']}),
        ('Description',			{'fields':['meta_description']}),
        ('Keywords', 			{'fields':['keywords']}),
        ('Author(s)', 			{'fields':['authors']}),
        ('Date information', 	{'fields': ['pub_date']}),
        ('Abstract',			{'fields': ['abstract']}),
        ('Site', 				{'fields': ['site']}),
        ('Post with formulas',	{'fields': ['has_latex_formula']}),#if true, mathjax.js is included in template (better for SEO)
        ('Content',     		{'fields': ['content']}),
    ]
    list_display = ('title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['title']
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


class ExtendedFlatPageForm(FlatpageForm):
    class Meta:
        model = RichTextFlatPage

class ExtendedFlatPageAdmin(FlatPageAdmin):
    form = ExtendedFlatPageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content_rich', 'sites', )}),
    )

admin.site.unregister(FlatPage)
admin.site.register(RichTextFlatPage, ExtendedFlatPageAdmin)
admin.site.register(Post,PostAdmin)
