from rest_framework.serializers import ModelSerializer
from .models import Comment, Rating, Favourite, Like


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        # exclude = ('user',)
        fields = '__all__'

    def validate(self, attrs):
        attrs = super().validate(attrs)
        request = self.context.get('request')
        attrs['user'] = request.user

        return attrs


class FavouriteSerializer(ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'

    def validate(self, attrs):
        attrs = super().validate(attrs)
        request = self.context.get('request')
        attrs['user'] = request.user

        return attrs

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['user'] = instance.user.email
        representation['movie'] = instance.movie.title
        del representation['favorite']
        return representation


class RatingSerializer(ModelSerializer):
    class Meta:
        model = Rating
        exclude = ('user',)

    def validate(self, attrs):
        attrs = super().validate(attrs)
        request = self.context.get('request')
        attrs['user'] = request.user

        return attrs


class LikeSerializer(ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
