from django.contrib import admin

from info.models import Article, Discipline, Film, Interview, News

admin.site.register(Discipline)
admin.site.register(Article)
admin.site.register(Interview)
admin.site.register(Film)
admin.site.register(News)
