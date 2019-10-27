from rest_framework import serializers, status

from .models import Subscription, Trader


class TraderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Trader
        fields=('email',)


class SubscriptionSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model=Subscription
        fields=('ticker','email','max_price','min_price')

    def create(self, validated_data):
        subscription, created=Subscription.objects.update_or_create(ticker=validated_data.pop('ticker'),
                                                                    email=validated_data.pop('email'),
                                                                    max_price=validated_data.pop('max_price',None),
                                                                    min_price=validated_data.pop('min_price',None))
        return subscription

  
        
  