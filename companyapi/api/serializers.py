from rest_framework import serializers
from api.models import Company
from api.models import Employee
class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__"


