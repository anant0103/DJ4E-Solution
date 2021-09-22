from django.contrib import admin

# Register your models here.
from .models import Iso,Site,Category,State,Region

admin.site.register(Site)
admin.site.register(Category)
admin.site.register(State)
admin.site.register(Region)
admin.site.register(Iso)
