from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Rubric

# Register your models here.
# admin.site.register(Rubric)

class MyDraggableMPTTAdmin(DraggableMPTTAdmin):
    mptt_level_indent = 20

admin.site.register(
    Rubric,
    MyDraggableMPTTAdmin,
    list_display=(
        'tree_actions',
        'indented_title',
        # ...more fields if you feel like it...
    ),
    list_display_links=(
        'indented_title',
    ),
)