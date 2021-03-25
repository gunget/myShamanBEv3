from django.contrib import admin
from movieDrtr.models import DirectorInfo, FicWriterInfo, NonFicWriterInfo

admin.site.register(DirectorInfo)
admin.site.register(FicWriterInfo)
admin.site.register(NonFicWriterInfo)
# Register your models here.
