from django.contrib import admin
from .models import Articles,biji,jsbooks
# Register your models here.
class ArticlesAdmin(admin.ModelAdmin):
    # ...
    list_display = ('id','title', 'content', 'create_time')
admin.site.register(Articles,ArticlesAdmin)
admin.site.register(biji)
admin.site.register(jsbooks)