from django.contrib import admin
from .models import Task

admin.site.register(Task)


admin.site.index_title = " Pushti Title"
admin.site.site_header = " Pushti Header"
admin.site.site_title = "Site Title"

