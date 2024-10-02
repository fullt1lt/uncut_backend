from rest_framework import serializers
from myappback.models import CategoryActivity, ProcedureActivity


class ProcedureActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcedureActivity
        fields = ['text_en', 'text_uk']
        
        
class CategoryActivitySerializer(serializers.ModelSerializer):
    procedures = ProcedureActivitySerializer(many=True)

    class Meta:
        model = CategoryActivity
        fields = ['title_en', 'title_uk', 'procedures']