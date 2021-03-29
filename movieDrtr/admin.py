from django.contrib import admin
from movieDrtr.models import DirectorInfo, FicWriterInfo, NonFicWriterInfo, OthersInfo

admin.site.register(DirectorInfo)
admin.site.register(FicWriterInfo)
admin.site.register(NonFicWriterInfo)
admin.site.register(OthersInfo)
# Register your models here.
