from rest_framework import generics, status
from rest_framework.response import Response
#from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from HospitalHomeBE.serializers.rolSerializer import RolSerializer
from HospitalHomeBE.models.rol import Rol

class RolListCreateView(generics.ListCreateAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
        print("GET a todos los roles")
        queryset = self.get_queryset()
        serializer = RolSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, *args, **kwargs):
        print("POST a Rol")
        serializer = RolSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

        """ tokenData = {
                     "username":request.data["username"],
                     "password":request.data["password"]
                    }
        tokenSerializer = TokenObtainPairSerializer(data=tokenData)
        tokenSerializer.is_valid(raise_exception=True)
        return Response(tokenSerializer.validated_data, status=status.HTTP_201_CREATED) """

class RolRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    queryset = Rol.objects.all()
    serializer_class = RolSerializer
    lookup_field = "tipo_usuario"   # campo con el que se realiza la búsqueda de los objetos
    lookup_url_kwarg = 'pk'         # nombre dado en la url al argumento
    #permission_classes = (IsAuthenticated,)

    def get(self, request, *args, **kwargs):
        print("GET a Rol")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().get(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        print("DELETE a Rol")
        """ if valid_data['user_id'] != kwargs['pk']:
            stringResponse = {'detail':'Unauthorized Request'}
            return Response(stringResponse, status=status.HTTP_401_UNAUTHORIZED) """
        return super().delete(request, *args, **kwargs)