from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .settings import domain_settings
from .models import Domain
from .signals import before_add_domain, after_add_domain


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        exclude = ["tenant", "instrument_id"]

    def validate_provider(self, value: str):
        if value in domain_settings.PROVIDERS:
            return value
        raise ValidationError(f"Provider '{value}' is not supported")

    def create(self, validated_data):
        before_add_domain.send(self.__class__, data=validated_data, **self.context)
        instance = super().create(validated_data)
        after_add_domain.send(self.__class__, instance=instance, **self.context)
        return instance
