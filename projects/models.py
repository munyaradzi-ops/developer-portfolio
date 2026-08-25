from django.db import models


class Technology(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        help_text="Optional icon name or CSS class"
    )

    website = models.URLField(
        blank=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        
class Feature(models.Model):

    project = models.ForeignKey(
        "Project",
        on_delete=models.CASCADE,
        related_name="features"
    )

    title = models.CharField(
        max_length=200
    )

    description = models.TextField(
        blank=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    def __str__(self):
        return f"{self.project.title} - {self.title}"

    class Meta:
        ordering = ["order"]
        
class ProjectScreenshot(models.Model):

    project = models.ForeignKey(
        "Project",
        on_delete=models.CASCADE,
        related_name="screenshots"
    )

    image = models.ImageField(
        upload_to="projects/screenshots/"
    )

    caption = models.CharField(
        max_length=200,
        blank=True
    )

    order = models.PositiveIntegerField(
        default=0
    )

    def __str__(self):
        return f"{self.project.title} - Screenshot {self.id}"

    class Meta:
        ordering = ["order"]
    
class Project(models.Model):

    CATEGORY_CHOICES = [
        ("web", "Web Application"),
        ("ecommerce", "E-Commerce"),
        ("management", "Management System"),
        ("ai", "AI / Machine Learning"),
        ("other", "Other"),
    ]

    STATUS_CHOICES = [
        ("completed", "Completed"),
        ("development", "In Development"),
        ("maintenance", "Maintenance"),
    ]

    title = models.CharField(
        max_length=200
    )

    slug = models.SlugField(unique=True, null=True, blank=True,
        max_length=220,
        
    )

    short_description = models.CharField(
        max_length=300
    )

    description = models.TextField()

    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )

    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default="completed"
    )

    image = models.ImageField(
        upload_to="projects/",
        blank=True,
        null=True
    )

    technologies = models.ManyToManyField(
        Technology,
        related_name="projects",
        blank=True
    )

    github_url = models.URLField(
        blank=True
    )

    live_url = models.URLField(
        blank=True
    )

    featured = models.BooleanField(
        default=False
    )

    start_date = models.DateField(
        blank=True,
        null=True
    )

    completion_date = models.DateField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-featured", "-created_at"]