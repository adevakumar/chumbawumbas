from django.contrib import admin

# Register your models here.

from .models import Weather, User, Clothing, ClothingType, Outfit, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    
# Register the Admin classes for Weather using the decorator
@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    list_display = ('weather_type', 'date')


# Register the Admin classes for User using the decorator
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'profile_picture', 'residence', 'phone', 'email', 'gender')
    
    fieldsets = (
        (None, {
            'fields': ('user_name', 'profile_picture', 'gender', 'residence')
        }),
        ('Contact Information', {
            'fields': ('phone', 'email')
        }),
    )


# Register the Admin classes for Clothing using the decorator
@admin.register(Clothing)
class ClothingAdmin(admin.ModelAdmin):
    list_display = ('clothing_name', 'clothing_type', 'clothing_picture', 'weather', 'id')
    list_filter = ('clothing_type', 'weather')


# Register the Admin classes for ClothingType using the decorator
@admin.register(ClothingType)
class ClothingTypeAdmin(admin.ModelAdmin):
	pass


# Register the Admin classes for Outfit using the decorator
@admin.register(Outfit)
class OutfitAdmin(admin.ModelAdmin):
    list_display = ('outfit_name', 'user', 'favorite', 'display_clothing', 'date', 'id')
    inlines = [CommentInline]


# Register the Admin classes for Comment using the decorator
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'outfit', 'text', 'date')
    list_filter = ('outfit', 'user', 'date')