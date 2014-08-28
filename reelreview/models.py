from django.db import models
from django.contrib.auth.models import User


class Movie(models.Model):
    '''
    Model to store all data for a movie
    '''
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    #image = models.ImageField()
    #TODO: add image field (involdes MEDIA_ROOT and MEDIA_URL)

    class Meta:
        unique_together = ('title', 'year',)

    def __unicode__(self):
        return self.title + ' (' + unicode(self.year) + ')'


class Genre(models.Model):
    '''
    Model for a specific genre
    Linked to movie through MovieGenre
    '''
    name = models.CharField(max_length=255, unique=True)

    def __unicode__(self):
        return self.name


class MovieGenre(models.Model):
    '''
    Relationship model for Movies and Genres
    Links a specific genre to a specific movie to emulate a many to many relationship
    '''
    movie = models.ForeignKey('Movie')
    genre = models.ForeignKey('Genre')

    class Meta:
        unique_together = ('movie', 'genre',)

    def __unicode__(self):
        return unicode(self.movie) + ': ' + unicode(self.genre)


class Favorite(models.Model):
    '''
    Model to store relationship between a Movie and a User
    '''
    user = models.ForeignKey(User)
    movie = models.ForeignKey('Movie')

    class Meta:
        unique_together = ('user', 'movie',)

    def __unicode__(self):
        return unicode(self.user) + ' Favorite - ' + unicode(self.movie)


class Source(models.Model):
    '''
    Model for the source of a Movie
    Origin is the provider of the Movie (i.e. Netflix)
    Link is a direct url to view the Movie on the Origin site
    '''
    origin = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    movie = models.ForeignKey('Movie')

    class Meta:
        unique_together = ('origin', 'link', 'movie',)

    def __unicode__(self):
        return


class Person(models.Model):
    '''
    Model for a Person in a Movie (i.e. Actors, Directors, etc.)
    '''
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Credit(models.Model):
    '''
    Model for relating a Person to a Movie
    The role defines the contribution type (i.e. Actor, Director, etc.)
    '''
    role = models.CharField(max_length=255)
    movie = models.ForeignKey('Movie')
    person = models.ForeignKey('Person')

    class Meta:
        unique_together = ('role', 'movie', 'person',)

    def __unicode__(self):
        return unicode(self.person) + ' in ' + unicode(self.movie) + ' as ' + self.role


class Recommendation(models.Model):
    '''
    Model for a Recommendation from one user to another for a specific movie
    Review (text), Rating (int), and Source are all optional fields
    Date is milliseconds since epoch
    '''
    sender = models.ForeignKey(User, related_name='sender')
    receiver = models.ForeignKey(User, related_name='receiver')
    movie = models.ForeignKey('Movie')
    source = models.ForeignKey('Source')
    review = models.CharField(max_length=255)
    date = models.BigIntegerField()
    stars = models.IntegerField()

    class Meta:
        unique_together = ('sender', 'receiver', 'movie', 'source',)

    def __unicode__(self):
        return unicode(self.sender) + '->' + unicode(self.receiver) + ': ' + unicode(self.movie)
