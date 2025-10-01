from django.contrib import admin
from blog.models import Post
# Register your models here.

# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('id','title','counted_view','status','created_date')
    list_filter = ('status',)
    # ordering = ['created_date']
    search_fields = ['title','content']
admin.site.register(Post,PostAdmin)


