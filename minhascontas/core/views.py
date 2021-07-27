from minhascontas.authentication.models import User
from minhascontas.core.serializers import BillSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from minhascontas.core.models import Bill
from datetime import datetime


class BillViewSet(ModelViewSet):
    serializer_class = BillSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Bill.objects.filter(date__month=datetime.now().month, date__year=datetime.now().year, user=self.request.user)
        return queryset

    def create(self, request, *args, **kwargs):
        data = request.data
        data['user'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
      
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)