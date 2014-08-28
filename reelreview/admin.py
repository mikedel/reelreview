from reelreview.models import *
from django.contrib import admin


class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'year',)
    list_filter = ('title', 'year',)

admin.site.register(Movie, MovieAdmin)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Genre, GenreAdmin)


class MovieGenreAdmin(admin.ModelAdmin):
    list_display = ('movie', 'genre',)
    list_filter = ('movie', 'genre',)

admin.site.register(MovieGenre, MovieGenreAdmin)


class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie',)
    list_filter = ('user', 'movie',)

admin.site.register(Favorite, FavoriteAdmin)


class SourceAdmin(admin.ModelAdmin):
    list_display = ('origin', 'link', 'movie',)
    list_filter = ('origin', 'movie',)

admin.site.register(Source, SourceAdmin)


class PersonAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Person, PersonAdmin)


class CreditAdmin(admin.ModelAdmin):
    list_display = ('role', 'movie', 'person',)
    list_filter = ('role', 'movie', 'person',)

admin.site.register(Credit, CreditAdmin)


class RecommendationAdmin(admin.ModelAdmin):
    list_display = ('sender', 'receiver', 'movie', 'source', 'review', 'date', 'stars',)
    list_filter = ('sender', 'receiver', 'movie', 'date')

admin.site.register(Recommendation, RecommendationAdmin)
