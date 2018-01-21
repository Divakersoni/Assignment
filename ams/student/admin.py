from django.contrib import admin
from .models import Student
class Student_Admin(admin.ModelAdmin):
    list_display = ('id', 'name', 'roll_no', 'date')
    list_per_page = 100
    search_fields = ('id', 'name')
    ordering = ['id']
    list_filter = ['id']
    fieldsets = [
        ('Name', {'fields': ['name']}),
        ('Roll No.', {'fields': ['roll_no']}),
        ('Upload File', {'fields': ['agn_file']}),
        ('Assignment', {'fields': ['assignment']}),
        ]
admin.site.register(Student,Student_Admin)
