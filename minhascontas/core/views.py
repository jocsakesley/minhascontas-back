from minhascontas.core.serializers import BillSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from minhascontas.core.models import Bill
from datetime import datetime


class BillViewSet(ModelViewSet):
    #queryset = Bill.objects.all()
    serializer_class = BillSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Bill.objects.filter(date__month=datetime.now().month, date__year=datetime.now().year)
        return queryset

