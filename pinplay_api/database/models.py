# useful resources:
    # 1. https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_many/
    # 2. https://docs.djangoproject.com/en/3.1/ref/models/fields/
    # 3. https://docs.djangoproject.com/en/3.1/ref/models/options/
    # 4. https://realpython.com/lessons/how-and-when-use-str/
 

from django.db import models
from django.db.models.fields.related import ForeignKey


class Playlist( models.Model ):
    playlist_name = models.CharField( max_length=20 )
    

    def get_data( self ):
        return self.playlist_name

    
    

class tracklist( models.Model ):
    name = models.CharField( max_length = 50 )

    
    

class track( models.Model ):
    title     = models.CharField( max_length = 50 )
    artist    = models.CharField( max_length = 50 )
    city      = models.CharField( max_length = 50 )
    explicit  = models.BooleanField()
    home_list = models.ForeignKey( tracklist, on_delete=models.CASCADE )


    def get_data( self ):
        return ( self.title, self.artist, self.city, self.explicit ) 




class location( models.Model ):
    city  = models.CharField( max_length = 40 )
    track = models.ManyToManyField( track )


    def get_data( self ):
        return self.city   
