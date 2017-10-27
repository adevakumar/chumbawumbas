from django.contrib import admin

# Register your models here.

from .models import Weather, User, Clothing, Outfit, Comment

# Register the Admin classes for Weather using the decorator

@admin.register(Weather)
class WeatherAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for User using the decorator

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for Clothing using the decorator

@admin.register(Clothing)
class ClothingAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for Outfit using the decorator

@admin.register(Outfit)
class OutfitAdmin(admin.ModelAdmin):
    pass

# Register the Admin classes for Comment using the decorator

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass