from rest_framework.response import Response # type: ignore
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from SistemaRV.decorators import jwt_required
from SistemaRV.decorators import CustomJWTAuthentication
from rest_framework.views import APIView
from rest_framework import status

class GenerateFacturacionFromIds(APIView):
    authentication_classes = [CustomJWTAuthentication]
    permission_classes = []
    
    
    @swagger_auto_schema(
        operation_summary="Generate Facturación",
        operation_description="Generate a facturación document based on specified IDs and other details.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['comprobante', 'emisor', 'comprador', 'items', 'payTerms', 'observaciones', 'tipoPago'],
            properties={
                'comprobante': openapi.Schema(type=openapi.TYPE_INTEGER, description="ID of the comprobante"),
                'emisor': openapi.Schema(type=openapi.TYPE_INTEGER, description="ID of the emisor"),
                'comprador': openapi.Schema(type=openapi.TYPE_INTEGER, description="ID of the comprador"),
                'items': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'id': openapi.Schema(type=openapi.TYPE_INTEGER, description="ID of the item"),
                            'quantity': openapi.Schema(type=openapi.TYPE_INTEGER, description="Quantity of the item")
                        }
                    ),
                    description="List of items with id and quantity"
                ),
                'payTerms': openapi.Schema(
                    type=openapi.TYPE_ARRAY,
                    items=openapi.Schema(
                        type=openapi.TYPE_OBJECT,
                        properties={
                            'metodo': openapi.Schema(type=openapi.TYPE_STRING, description="Payment method")
                        }
                    ),
                    description="List of payment terms, each with a metodo"
                ),
                'observaciones': openapi.Schema(type=openapi.TYPE_STRING, description="Observations for the document"),
                'tipoPago': openapi.Schema(type=openapi.TYPE_INTEGER, description="ID of the payment type"),
            },
            description="Data required to generate a facturación document"
        ),
        responses={
            200: openapi.Response(description="Successful Request", examples={"application/json": {"response": "Successful Request"}}),
            400: openapi.Response(description="Bad Request")
        }
    )
    @jwt_required
    def post(self, request, *args):
        data = request.data
        
        # Required keys for validation
        required_keys = {
            'comprobante': int,
            'emisor': int,
            'comprador': int,
            'items': list,
            'payTerms': list,
            'observaciones': str,
            'tipoPago': int,
        }
        
        # Check if each required key is in the data
        for key, expected_type in required_keys.items():
            if key not in data:
                return Response({"error": f"'{key}' is a required field."}, status=status.HTTP_400_BAD_REQUEST)
            if not isinstance(data[key], expected_type):
                return Response({"error": f"'{key}' must be of type {expected_type.__name__}."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check that items is a list of dictionaries with 'id' and 'quantity' keys
        for item in data['items']:
            if not isinstance(item, dict) or 'id' not in item or 'quantity' not in item:
                return Response({
                    "error": "Each item in 'items' must be a dictionary with 'id' and 'quantity' keys."
                }, status=status.HTTP_400_BAD_REQUEST)
        
        # Check that payTerms is a list of dictionaries with 'metodo' key
        for term in data['payTerms']:
            if not isinstance(term, dict) or 'metodo' not in term:
                return Response({
                    "error": "Each entry in 'payTerms' must be a dictionary with a 'metodo' key."
                }, status=status.HTTP_400_BAD_REQUEST)
        
        # If all checks pass, return a success response
        return Response({'response': 'Successful Request'})
    
if __name__ == '__main__':
    data = {
        'comprobante': 1,
        'emisor' : 1,
        'comprador' : 2,
        'items' : [
            {'id': 2,
            'quantity' : 5},
            {'id': 4,
            'quantity' : 1}
        ],
        "payTerms": [
            {
                "metodo": "contado",
            }
        ],
        'observaciones': 'Observaciones para poner en el documento pdf',
        'tipoPago': 3,
    }