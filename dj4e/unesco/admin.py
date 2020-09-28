from django.contrib import admin

# Register your models here.
from .models import Category, States, Region, Iso, Site
# Register your models here.
admin.site.register(Category)
admin.site.register(States)
admin.site.register(Region)
admin.site.register(Iso)
admin.site.register(Site)