from django.contrib import admin
from .models import Post, Tag

class PostAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags', 'rel_products',)
    list_display = ('title', 'pub_date', 'active',)
    list_editable = ('active',)
    list_filter = ('active', 'tags',)
    class Meta:
        model = Post

admin.site.register(Post, PostAdmin)

admin.site.register(Tag)