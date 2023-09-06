from django.contrib import admin

from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "created_by", "created_at", "updated_at")
    prepopulated_fields = {"slug": ("title",)}
    exclude = ("created_by",)

    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Post, PostAdmin)
