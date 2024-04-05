
from django.conf import settings
from rest_framework.serializers import ModelSerializer
from django.utils.translation import get_language_from_request


class TranslatableModelSerializer(ModelSerializer):

    def to_representation(self, instance):
        language = get_language_from_request(self.context['request'])
        if language not in settings.ALL_LANGUAGES:
            language = settings.DEFAULT_LANGUAGE
        
        rep = super().to_representation(instance)
        for field in self.Meta.translatable_fields:
            rep[f'{field}'] = rep[f'{field}_{language}']

            for lan in settings.ALL_LANGUAGES:
                del rep[f'{field}_{lan}']

        return rep


