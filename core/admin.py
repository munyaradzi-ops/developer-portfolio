from django.contrib import admin
from .models import Profile, Skill


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "title",
        "email",
        "location",
        "updated_at",
    )


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "category",
        "level",
    )

    list_filter = (
        "category",
    )