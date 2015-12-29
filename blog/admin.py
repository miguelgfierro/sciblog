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
        ('Image', 				{'fields': ['image']}),
        ('Image caption',		{'fields': ['image_caption']}),
        ('Image second', 		{'fields': ['image_second']}),
        ('Image caption second',{'fields': ['image_caption_second']}),
        ('Youtube link',        {'fields': ['youtube_link']}),
        ('Post with formulas',	{'fields': ['has_latex_formula']}),
        ('Page 1 column 1', 	{'fields': ['body_page1_col1']}),
        ('Page 1 column 2',		{'fields': ['body_page1_col2']}),
        ('Page 2 column 1',		{'fields': ['body_page2_col1']}),
        ('Page 2 column 2',		{'fields': ['body_page2_col2']}),

    ]
    list_display = ('title', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['title']
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


admin.site.register(Post,PostAdmin)
