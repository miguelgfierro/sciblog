from django.contrib import admin
from blog.models import Post

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


admin.site.register(Post,PostAdmin)
