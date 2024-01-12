from django.contrib import admin
from .models import Resume

# Register your models here.
@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
    list_display=["Name","Gender","Locality","City","Pin","State","Mobile_No","Email","Job_City","Profile_Image"]