from rest_framework.viewsets import ModelViewSet
from .models import employees
from . serializers import employeesSerializer


# Create your views here.
class employeeList(ModelViewSet):

    serializer_class = employeesSerializer
    queryset = employees.objects.all()