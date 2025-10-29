# ...existing code...
from django.contrib import admin
from .models import AboutMe, LearningJourney

# Customize admin site titles to include your name
admin.site.site_header = "Dawa Zam — Admin"
admin.site.site_title = "Dawa Zam Admin"
admin.site.index_title = "Site Administration"

# Admin display for AboutMe
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

# Admin display for LearningJourney
class LearningJourneyAdmin(admin.ModelAdmin):
    list_display = ('title', 'date')
    list_filter = ('date',)
    search_fields = ('title', 'description')

# Register your models here.
admin.site.register(AboutMe, AboutMeAdmin)
admin.site.register(LearningJourney, LearningJourneyAdmin)
# ...existing code...