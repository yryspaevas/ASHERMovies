from rest_framework.serializers import ModelSerializer
from .models import Comment, Rating, Favourite


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('user',)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        request = self.context.get('request')
        attrs['user'] = request.user

        return attrs


class FavouriteSerializer(ModelSerializer):
    class Meta:
        model = Favourite
        exclude = ('user',)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        request = self.context.get('request')
        attrs['user'] = request.user

        return attrs


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        exclude = ('user',)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        request = self.context.get('request')
        attrs['user'] = request.user

        return attrs
