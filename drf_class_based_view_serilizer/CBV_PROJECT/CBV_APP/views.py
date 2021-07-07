#------------- imports ------------------------

from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer
from django.views import View
from django.http import HttpResponse
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@method_decorator(csrf_exempt, name = "dispatch")

class TaskCBV(View):
    #=============================== GET ========================================================
    def get(self, request, *args, **kwargs):

        # 1. ------------------to convert the json data to binary data --------------------

        json_data = request.body
        print("json_data : ", json_data)
        print("json_datatype : ", type(json_data))

        #2. ------------------to stream(process) the binary data ---------------------------

        stream = io.BytesIO(json_data)
        print("stream : ", stream)
        print("stream_datatype : ", stream)

        #3.------------------ to convert binary data into dictionary (deserialization)----------------------------------------
        
        data = JSONParser().parse(stream)
        print("data : ", data)
        print('data_datatype : ', type(data))

        #4. ------------------ to get id(if exists else None) -------------------------------
        id = data.get("id", None)
        print("id : ",id)
        print("id_datatype : ", type(id))

        if id is not None:

        #5. ------------------ to get data related to id -----------------------------------

            tsk = Task.objects.get(id=id)
            print("tsk : ",tsk)
            print("tsk_datatype : ", type(tsk))
        #6. ----------------- to add the data present in the task in TaskSerializer for serialization purpose ------------------    
            
            serializer = TaskSerializer(tsk)
            print("serializer : ", serializer)
            print("serializer_datatype : ", type(serializer))

        #7. ----------------- actual serialization( dict --> json(bytes) happens here ------------------)   
            
            json_data = JSONRenderer().render(serializer.data)
            print("json_data : ", json_data)
            print("json_data_datatype : ", type(json_data))


            return HttpResponse(json_data, content_type = 'application/json')
        tsk = Task.objects.all()
        print("tsk : ",tsk)
        print("tsk_datatype : ", type(tsk))

        serializer = TaskSerializer(tsk, many = True)
        print("serializer : ", serializer)
        print("serializer_datatype : ", type(serializer)) 

        json_data = JSONRenderer().render(serializer.data)
        print("json_data : ", json_data)
        print("json_data_datatype : ", type(json_data))

        return HttpResponse(json_data, content_type = 'application/json')
    # ========================================================================================


    #==================================== POST ===============================================
    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        serializer = TaskSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            json_data = JSONRenderer().render({"msg":"data saved successfully"})
            return HttpResponse(json_data, content_type = 'application/json')
        msg = {"msg":"please enter valid data"}        
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data, content_type = 'application/json') 
    #========================================================================================



    #============================== PUT AND PATCH ===========================================
    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get("id")
        tsk = Task.objects.get(id=id)
        serializer = TaskSerializer(tsk, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            json_data = JSONRenderer().render("msg: data updated successfully")
            return HttpResponse(json_data, content_type = "application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type = "application/json")    
            
    #========================================================================================  
    
    
    # ================================= DELETE =============================================
    def delete(self, request,*args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get("id", None)
        if id is not None:
            tsk = Task.objects.get(id=id)
            tsk.delete()
            json_data = JSONRenderer().render({"msg":"data deleted successfully"})
            return HttpResponse(json_data,content_type ="application/json")
        json_data = JSONRenderer().render({"msg":"please provide valid id"})
        return HttpResponse(json_data,content_type ="application/json")    
        

    # ======================================================================================  
   

    
