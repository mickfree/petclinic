from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Client)
admin.site.register(Pet)
admin.site.register(Veterinarian)
admin.site.register(ClinicalRecord)

