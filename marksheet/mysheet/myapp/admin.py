from django.contrib import admin
from myapp.models import subject,names

class nameAdmin(admin.ModelAdmin):
    list_display = ("id","name","class1","date_created")


class SubjectAdmin(admin.ModelAdmin):
    list_display = ["id"]    
    
admin.site.register(names,nameAdmin)
admin.site.register(subject,SubjectAdmin)