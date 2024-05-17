from django.contrib import admin

from apps.post.models import Post

class PostAdmin(admin.ModelAdmin):
    list_display=("title","created_at") #parametros del modelo que se previsualizan en el admin
    search_fields=("title",) #parametros para buscar en el admin
    #list_filter = ('created_at',) #Filtros laterales con campos seleccionados
    date_hierarchy = "created_at" #Agrega un control de navegación por fecha
admin.site.register(Post, PostAdmin)