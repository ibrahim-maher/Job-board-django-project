
from django.contrib import admin

from .models import Apply, Job,Category

admin.site.register(Job),
admin.site.register(Category)
admin.site.register(Apply)



