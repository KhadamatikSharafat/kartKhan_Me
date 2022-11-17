from rest_framework import serializers

from web.models import register, login


class registerSerializer(serializers.ModelSerializer):

    class Meta:
        model = register
        fields = '__all__'
        # fields = ('id','name','family','fatherName','birthday','codeMeli','serialMeli','shomareSh','serialSh')