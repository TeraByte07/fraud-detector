from django.conf import settings
import joblib
import numpy as np
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .serializers import PredictSerializer, paymentListSerializer
from sklearn.exceptions import NotFittedError
from ml.models import paymentDetails

# Load the model when the server starts
try:
    model = joblib.load(settings.MODEL_PATH)
    print("Model loaded successfully.")
except FileNotFoundError as e:
    print(f"Model file not found: {e}")
    model = None
except Exception as e:
    print(f"Error loading the model: {e}")
    model = None

class PredictView(APIView):
    def post(self, request, *args, **kwargs):
        if model is None:
            return Response({"error": "Model not loaded"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
        serializer = PredictSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            features = np.array([
                [
                    data['amount'],
                    data['oldbalanceOrg'],
                    data['newbalanceOrig']
                ]
            ])
            try:
                prediction = model.predict(features)
                return Response({'prediction': int(prediction[0])})
            except NotFittedError:
                return Response({"error": "Model is not fitted."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class paymentLists(generics.ListCreateAPIView):
    queryset = paymentDetails.objects.all()
    serializer_class = paymentListSerializer