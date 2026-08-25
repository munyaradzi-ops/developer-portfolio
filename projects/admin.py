from django.contrib import admin

from .models import (
    Project,
    Technology,
    Feature,
    ProjectScreenshot,
)


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "website",
    )

    search_fields = (
        "name",
    )


class FeatureInline(admin.TabularInline):

    model = Feature

    extra = 1

    fields = (
        "title",
        "description",
        "order",
    )


class ScreenshotInline(admin.TabularInline):

    model = ProjectScreenshot

    extra = 1

    fields = (
        "image",
        "caption",
        "order",
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "category",
        "status",
        "featured",
        "start_date",
        "completion_date",
    )

    list_filter = (
        "category",
        "status",
        "featured",
    )

    search_fields = (
        "title",
        "short_description",
        "description",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    filter_horizontal = (
        "technologies",
    )

    inlines = [
        FeatureInline,
        ScreenshotInline,
    ]