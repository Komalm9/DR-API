from .models import Student
from rest_framework import serializers

 # 2. ---------------- applying multiple validations to single field ---------------


def only_str_and_num_allowed(value):
   if not value.isalnum():
            raise serializers.ValidationError("only numbers and alphabets are allowed")


def username_already_exists(value):
    print(value)
    for data in Student.objects.all():
        if data.username == value:
            raise serializers.ValidationError("username already exists")   

#-------------------------------------------------------------------------------------

class StudentModelSerializer(serializers.ModelSerializer):

    username = serializers.CharField(
        validators=[only_str_and_num_allowed, username_already_exists]
    )

    class Meta:
        model = Student
        fields = "__all__"


    # 1. field-level validations
    
    def validate_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("only characters are allowed")
        return value    

        
        
    

    # 3. applying multiple validations to multiple fields
    def validate(self,data):
        print(data)
        pass1 = data.get("password1")
        pass2 = data.get("password2")
        if pass1 != pass2:
            raise serializers.ValidationError("passwords do not match")
        return data
