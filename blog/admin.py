from django.contrib import admin
from blog.models import Post, Category

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               	{'fields': ['title']}),
        ('Category', 			{'fields':['category']}),
        ('Date information', 	{'fields': ['pub_date']}),
        ('Abstract',			{'fields': ['abstract']}),
        ('Site', 				{'fields': ['site']}),#TODO: remove this and take it automatically
        ('Image', 				{'fields': ['image']}),
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
admin.site.register(Category)
