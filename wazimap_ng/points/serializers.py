from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from django.core.serializers import serialize

from . import models
from wazimap_ng.general.serializers import LicenceSerializer, MetaDataSerializer
from wazimap_ng.profile.serializers import SimpleProfileSerializer as ProfileSerializer

class SimpleThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Theme
        fields = ["id", "name"]

class CategorySerializer(serializers.ModelSerializer):
    metadata = MetaDataSerializer()
    name = serializers.ReadOnlyField()
    profile = ProfileSerializer()

    class Meta:
        model = models.Category
        fields = ("id", "profile", "permission_type", "name", "metadata")

class ThemeSerializer(serializers.ModelSerializer):
    # categories = CategorySerializer(many=True)

    class Meta:
        model = models.Theme
        fields = "__all__"

    def to_representation(self, obj):
        representation = super().to_representation(obj)

        if not obj.icon:
            representation["icon"] = "icon--%s" % obj.name.lower()
        return representation

class LocationSerializer(GeoFeatureModelSerializer):
    category = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    def get_category(self, obj):
        category_js = self.context.get("category_js", None)

        if not category_js:
            profile_id = self.context.get("profile_id", None)
            profile_category = obj.category.profilecategory_set.filter(
                profile_id=profile_id
            ).first()
            category_js = Profile(profile_category).data
        return category_js

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image != None and obj.image.url != None:
            photo_url = obj.image.url
            return request.build_absolute_uri(photo_url)
        return None

    class Meta:
        model = models.Location
        geo_field = "coordinates"

        fields = ('id', 'data', "category", "name", "url", "image")

class LocationInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Location
        fields = ('id', 'coordinates', 'data', )


class InlineThemeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Theme
        fields = ("id", "name", "icon",)

class ProfileCategorySerializer(serializers.ModelSerializer):
    metadata = MetaDataSerializer(source="category.metadata")
    theme = InlineThemeSerializer()
    name = serializers.ReadOnlyField(source="label")

    class Meta:
        model = models.ProfileCategory
        fields = ('id', 'name', 'description', 'theme', 'metadata',)
