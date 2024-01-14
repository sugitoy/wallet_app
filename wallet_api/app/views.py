from rest_framework import filters, generics, viewsets
from .models import Transaction
from .serializer import TransactionSerializer

class TransactionViewSet(viewsets.ModelViewSet):
   queryset = Transaction.objects.all()
   serializer_class = TransactionSerializer
   filter_fields = ('date', 'category', 'memo', 'income', 'expenditure')