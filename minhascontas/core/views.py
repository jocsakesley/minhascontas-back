from minhascontas.authentication.models import User
from minhascontas.core.serializers import BillSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from minhascontas.core.models import Bill
from datetime import date, datetime
import json

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
        year = datetime.strptime(serializer.data['date'], "%Y-%m-%d").year
        day = datetime.strptime(serializer.data['date'], "%Y-%m-%d").day 
        if serializer.data['is_recurrent']:
            for month in range(datetime.strptime(serializer.data['date'], '%Y-%m-%d').month + 1, 13):
                try:
                    date = datetime(year, month, day)
                except:
                    date = datetime(year, month, day-1)
                Bill.objects.create(name=serializer.data['name'], 
                type_bill=serializer.data['type_bill'], 
                value=float(serializer.data['value']), 
                date=date,
                is_recurrent=serializer.data['is_recurrent'],
                user=User.objects.get(id=serializer.data['user']))
                  
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)