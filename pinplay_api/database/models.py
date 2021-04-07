# useful resources:
    # Tutorial: https://www.youtube.com/watch?v=UxTwFMZ4r5k
    
    # Documentation and tips
    # 1. https://docs.djangoproject.com/en/3.1/topics/db/examples/many_to_many/
    # 2. https://docs.djangoproject.com/en/3.1/ref/models/fields/
    # 3. https://docs.djangoproject.com/en/3.1/ref/models/options/
    # 4. https://realpython.com/lessons/how-and-when-use-str/
 

from django.db import models


class track( models.Model ):
    title     = models.CharField( max_length = 50 )
    artist    = models.CharField( max_length = 50 )
    city      = models.CharField( max_length = 50 )
    genre     = models.CharField( max_length = 50 )
    explicit  = models.BooleanField()
    
        
    # NOTE: 
        # to retireve genre, song_uri, and explicitness, must make call to Spotify API

    def get_data( self ):
        return ( self.title, self.artist, self.city, self.explicit ) 




class location( models.Model ):
    city  = models.CharField( max_length = 40 )
    track = models.ManyToManyField( track )


    def get_data( self ):
        return self.city   
