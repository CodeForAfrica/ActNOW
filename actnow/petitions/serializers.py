from rest_framework import serializers

from actnow.accounts.serializers import UserSerializer

from .models import Petition, Signature, Source


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = "__all__"


class SignatureSerializer(serializers.ModelSerializer):
    signatory = UserSerializer(read_only=True)

    class Meta:
        model = Signature
        fields = "__all__"

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        if instance.anonymous:
            rep.pop("signatory")
        return rep


class PetitionSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    followers = UserSerializer(read_only=True, many=True)
    signatures = SignatureSerializer(read_only=True, many=True)
    source = SourceSerializer()

    class Meta:
        model = Petition
        fields = [
            "created_at",
            "updated_at",
            "title",
            "description",
            "recipients",
            "problem_statement",
            "number_of_signatures_required",
            "image",
            "video",
            "owner",
            "signatures",
            "source",
            "followers",
        ]

    def create(self, validated_data):
        source_validated_data = validated_data.pop("source")
        source = Source.objects.create(**source_validated_data)
        instance = Petition.objects.create(source=source, **validated_data)

        return instance
