from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    bio = models.TextField()
    profile_image = models.ImageField(
        upload_to="profile/",
        blank=True,
        null=True
    )
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=30, blank=True)
    location = models.CharField(max_length=100, blank=True)

    github_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Skill(models.Model):
    CATEGORY_CHOICES = [
        ("backend", "Backend"),
        ("frontend", "Frontend"),
        ("database", "Database"),
        ("ai", "AI & Machine Learning"),
        ("tools", "Tools & Technologies"),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )
    level = models.PositiveIntegerField(
        default=80,
        help_text="Skill level from 0 to 100"
    )

    def __str__(self):
        return self.name