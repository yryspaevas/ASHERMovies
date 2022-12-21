from rest_framework.serializers import ModelSerializer
from .models import Genre, Country, Movie

class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
    

class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

    # def validate(self, attrs):
    #     attrs =  super().validate(attrs)
    #     request = self.context.get('request')
    #     attrs['movie'] = request.user
    #     return attrs
    
    # def to_representation(self, instance:Movie):
    #     rep = super().to_representation(instance)
    #     # rep['country']=instance.country_movie["title"]
    #     # rep['rating'] = instance.average_rating
    #     rep['likes'] = instance.likes.all().count()
    #     rep['favorites'] = instance.favorites.filter(favorited=True).count()
    #     return rep
