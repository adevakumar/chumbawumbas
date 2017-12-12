from django.contrib import admin

# Register your models here.

from .models import UserProfile, Clothing, ClothingType, WeatherSuggestion, Outfit, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0

# admin.site.register(UserProfile)
# Register the Admin classes for UserProfile using the decorator
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    readonly_fields=('display_user_name', 'display_email', 'display_clothing', 'display_friends')
    list_display = ('display_user_name', 'profile_picture', 'description', 'display_clothing', 'display_friends','residence', 'display_email','phone', 'gender', 'maximum_cold_temperature', 'maximum_cool_temperature', 'maximum_warm_temperature')
    
    fieldsets = (
        (None, {
            'fields': ('display_user_name', 'profile_picture', 'description', 'display_clothing', 'display_friends', 'gender', 'residence', 'maximum_cold_temperature', 'maximum_cool_temperature', 'maximum_warm_temperature')
        }),
        ('Contact Information', {
            'fields': ('phone', 'display_email')
        }),
    )


# Register the Admin classes for Clothing using the decorator
@admin.register(Clothing)
class ClothingAdmin(admin.ModelAdmin):
    list_display = ('clothing_name', 'clothing_type', 'clothing_picture',  'id')
    list_filter = ('clothing_type',)


# Register the Admin classes for ClothingType using the decorator
@admin.register(ClothingType)
class ClothingTypeAdmin(admin.ModelAdmin):
	pass


# Register the Admin class for WeatherSuggestion using the decorator
@admin.register(WeatherSuggestion)
class WeatherSuggestionAdmin(admin.ModelAdmin):
    pass


# Register the Admin classes for Outfit using the decorator
@admin.register(Outfit)
class OutfitAdmin(admin.ModelAdmin):
    list_display = ('outfit_name', 'user', 'favorite', 'display_clothing', 'date', 'id')
    inlines = [CommentInline]


# Register the Admin classes for Comment using the decorator
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'outfit', 'text', 'date')
    list_filter = ('outfit', 'user_profile', 'date')