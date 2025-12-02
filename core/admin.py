from django.contrib import admin
from .models import Service, Role, TeamMember


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("name", "created", "modified", "active")
    search_fields = ("name",)
    list_filter = ("active", "created", "modified")


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("title", "icon", "created", "modified", "active")
    search_fields = ("title", "description")
    list_filter = ("active", "created", "modified")


@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("name", "role", "created", "modified", "active")
    search_fields = ("name", "bio", "email")
    list_filter = ("active", "created", "modified")
