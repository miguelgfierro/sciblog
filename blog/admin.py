from django.contrib import admin
from blog.models import Post
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from django import forms
from libs.ckeditor.widgets import CKEditorWidget

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               	    {'fields': ['title']}),
        ('Description',			    {'fields':['meta_description']}),
        ('Keywords (lowercase)',    {'fields':['keywords']}),
        ('Author(s)', 			    {'fields':['authors']}),
        ('Date information', 	    {'fields': ['pub_date']}),
        ('Abstract',			    {'fields': ['abstract']}),
        ('Site', 				    {'fields': ['site']}),
        ('Post with formulas',	    {'fields': ['has_latex_formula']}),#if true, mathjax.js is included in template (better for SEO)
        ('Content',     		    {'fields': ['content']}),
    ]
    list_display = ('title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['title']
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


class ExtendedFlatPageForm(FlatpageForm):
    locals()['content'] = forms.CharField(widget=CKEditorWidget(), required=False, label=(u'Content'))
    class Meta:
        model = FlatPage
        fields = "__all__"

class ExtendedFlatPageAdmin(FlatPageAdmin):
    form = ExtendedFlatPageForm
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites', )}),
    )

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, ExtendedFlatPageAdmin)
admin.site.register(Post,PostAdmin)
