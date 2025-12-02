from django.db import models
from stdimage.models import StdImageField
import uuid


def get_file_path(_instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return filename


class Base(models.Model):
    created = models.DateTimeField("Created at", auto_now_add=True)
    modified = models.DateTimeField("Modified at", auto_now=True)
    active = models.BooleanField("Active", default=True)

    class Meta:
        abstract = True


class Service(Base):
    ICONE_CHOICES = [
        ("lni-cog", "Cog"),
        ("lni-stats-up", "Stats Up"),
        ("lni-users", "Users"),
        ("lni-layers", "Layers"),
        ("lni-mobile", "Mobile"),
        ("lni-rocket", "Rocket"),
    ]
    title = models.CharField("Title", max_length=100)
    icon = models.CharField("Icon", max_length=20, choices=ICONE_CHOICES)
    description = models.TextField("Description", max_length=200)

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

    def __str__(self):
        return self.title


class Role(Base):
    name = models.CharField("Role Name", max_length=100)

    class Meta:
        verbose_name = "Role"
        verbose_name_plural = "Roles"

    def __str__(self):
        return self.name


class TeamMember(Base):
    name = models.CharField("Name", max_length=100)
    role = models.ForeignKey(
        Role,
        verbose_name="Role",
        on_delete=models.CASCADE,
        related_name="team_members",
    )
    photo = StdImageField(
        "Photo",
        upload_to=get_file_path,
        variations={"thumb": (480, 480)},
        blank=True,
        null=True,
    )
    bio = models.TextField("Bio", max_length=500, blank=True)
    email = models.EmailField("Email", max_length=254, blank=True)
    facebook = models.URLField("Facebook", max_length=200, blank=True)
    twitter = models.URLField("Twitter", max_length=200, blank=True)
    instagram = models.URLField("Instagram", max_length=200, blank=True)

    class Meta:
        verbose_name = "Team Member"
        verbose_name_plural = "Team Members"

    def __str__(self):
        return self.name
