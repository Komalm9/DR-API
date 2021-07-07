from django.shortcuts import render
from django.views import View
from io import BytesIO
from rest_framework.parsers import JSONParser
from .models import Student
from.serializers import StudentModelSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse 
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@method_decorator(csrf_exempt, name="dispatch")
class StudentCBVM(View):
    def get(self, request, *args, **kwargs):

        json_data = request.body
        stream = BytesIO(json_data)
        deserialized_data = JSONParser().parse(stream)
        id = deserialized_data.get("id", None)

        if id is not None:
            stu_data = Student.objects.get(id=id)
            serializer = StudentModelSerializer(stu_data)
            serialized_data = JSONRenderer().render(serializer.data)
            return HttpResponse(serialized_data,content_type="application/json")

        stu_data = Student.objects.all()
        serializer = StudentModelSerializer(stu_data, many=True)
        serialized_data = JSONRenderer().render(serializer.data)
        return HttpResponse(serialized_data,content_type="application/json")

    
    
    
    def post(self, request, *args, **kwargs):

        json_data = request.body
        stream = BytesIO(json_data)
        deserialized_data = JSONParser().parse(stream)
        serializer = StudentModelSerializer(data=deserialized_data)

        if serializer.is_valid():
            serializer.save()
            msg={"msg":"data added successfully"}
            serialized_data = JSONRenderer().render(msg)
            return HttpResponse(serialized_data, content_type="application/json")

        msg = {"msg":"please enter valid data"}
        serialized_data = JSONRenderer().render(msg)
        return HttpResponse(serialized_data, content_type="application/json")  


    
    
    def put(self, request, *args, **kwargs):

        json_data = request.body
        stream = BytesIO(json_data)
        deserialized_data = JSONParser().parse(stream)
        id = deserialized_data.get("id")
        db_data = Student.objects.get(id=id)
        serializer = StudentModelSerializer(db_data, data=deserialized_data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            msg = {"msg":"data updated successfully"}
            serialized_data = JSONRenderer().render(msg)
            return HttpResponse(serialized_data, content_type="application/json") 

        
        serialized_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(serialized_data, content_type="application/json") 


    def delete(self, request,*args, **kwargs):

        json_data = request.body
        stream = BytesIO(json_data)
        deserialized_data = JSONParser().parse(stream)
        id = deserialized_data.get("id", None)

        if id is not None:
            db_data = Student.objects.get(id=id)
            db_data.delete()
            msg = {"msg":"data deleted successfully"}
            serialized_data = JSONRenderer().render(msg)
            return HttpResponse(serialized_data, content_type="application/json") 

        
        serialized_data = JSONRenderer().render({"msg":"please enter valid id"})
        return HttpResponse(serialized_data, content_type="application/json") 

        

        

    


            



    