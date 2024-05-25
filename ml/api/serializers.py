from ml.models import paymentDetails
from rest_framework import serializers

class PredictSerializer(serializers.ModelSerializer):
    class Meta:
        model = paymentDetails
        fields = ["amount", "oldbalanceOrg", "newbalanceOrig"]
        
class paymentListSerializer(serializers.ModelSerializer):
    class Meta:
        model = paymentDetails
        fields = "__all__"