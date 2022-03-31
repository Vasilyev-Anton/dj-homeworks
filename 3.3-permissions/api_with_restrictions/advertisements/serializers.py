from django.contrib.auth.models import User
from rest_framework import serializers

from advertisements.models import Advertisement


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name',)


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = '__all__'

    def create(self, validated_data):
        """Метод для создания"""
        print(validated_data)
        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # Обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # Само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data["creator"] = self.context["request"].user
        return super().update(instance, validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""

        # TODO: добавьте требуемую валидацию
        adv_valid = Advertisement.objects.filter(creator=self.context["request"].user, status="OPEN").count()
        if self.context["request"].method == 'POST' and adv_valid >= 10:
            raise serializers.ValidationError('Превышено количество открытых объявлений')

        if self.context["request"].method == 'PATCH' and adv_valid >= 10 and data.get('status') == 'OPEN':
            raise serializers.ValidationError('Превышено количество открытых объявлений')
        return data
