import json
from rest_framework.response import Response
from rest_framework.views import APIView
from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from .models import Subscription, Trader
from .serializers import SubscriptionSerializer
from django.http import JsonResponse

class SubscriptionView(APIView):

    def get(self, request):
        subscriptions = Subscription.objects.all()
        serializer=SubscriptionSerializer(subscriptions, many=True)
        return Response({"subscriptions": serializer.data})

    def post(self, request):
        subscription=request.data.get('subscription')
        
            
        
        
        if subscription.get('ticker',None)==None:
            Subscription.objects.filter(email=subscription.get('email')).delete()
            return Response({"Ticker was empty. All subscriptions of email '{}' deleted".format(subscription.get('email'))})

        else:
            if Subscription.objects.filter(email=subscription.get('email')).count()>=5:
                return Response({"Subscription limit of email {} exceeded".format(subscription.get('email'))})
            else:
                ts=TimeSeries(key='6CB8I2158LF2I0ZE', output_format='pandas')
                data, meta_data=ts.get_intraday(symbol=subscription.get('ticker'),interval='1min',outputsize='full')

                if not subscription.get('max_price', None)==None and not subscription.get('min_price',None)==None:
                    
                    if data['4. close'][0]<subscription.get('min_price') or data['4. close'][0]>subscription.get('max_price'):
                        send_mail('News about your tickers',
                              'Cost of your ticker is changed', 
                              'cursoriam@hushmail.com', 
                              [subscription.get('email')],
                              fail_silently=False)
                        return Response({"{}".format(subscription.get('email'))})
                elif not subscription.get('max_price', None)==None:
                    if data['4. close'][0]>subscription.get('max_price'):
                        send_mail('News about your tickers',
                              'Cost of your ticker is changed', 
                              'cursoriam@hushmail.com', 
                              [subscription.get('email')],
                              fail_silently=False)
                        return Response({"{}".format(subscription.get('email'))})
                elif not subscription.get('min_price', None)==None:
                    if data['4. close'][0]<subscription.get('min_price'):
                        send_mail('News about your tickers',
                              'Cost of your ticker is changed', 
                              'cursoriam@hushmail.com', 
                              [subscription.get('email')],
                              fail_silently=False)
                        return Response({"{}".format(subscription.get('email'))})
                else:
                    return Response({"Wrong request"})
        
                

                try:
                    Trader.objects.get(email=request.data.get('subscription').get('email'))
                except Trader.DoesNotExist:
                    tr=Trader(email=request.data.get('subscription').get('email'))
                    tr.save()
        
                

                serializer=SubscriptionSerializer(data=subscription)

                
        
                if serializer.is_valid(raise_exception=True):
                    subscription_saved=serializer.save(validated_data=subscription)
                return Response({"success":"Subscription '{}' created successfully".format(subscription_saved.ticker)})

    
    def delete(self, request, email,ticker):
        try:
            subscription=Subscription.objects.get(email=email,ticker=ticker)
        except:
            return Response({"Subscription does not exist"})
        subscription.delete()
        return Response({"Subscription {} of {} was deleted".format(ticker,email)}) 
        
