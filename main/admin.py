from django.contrib import admin
from . models import *
# Register your models here.
admin.site.register(Posts)
admin.site.register(Comments)

admin.site.site_header = 'django rest_api'


