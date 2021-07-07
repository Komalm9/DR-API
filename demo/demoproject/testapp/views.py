from django.shortcuts import render
from .models import Task
from django.views.generic import View
import io
from rest_framework.parsers import JSONParser
from .serializers import TaskSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class TaskCBV(View):
    def get(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get('id', None)

        if id is not None:
            tsk = Task.objects.get(id=id)
            serializer = TaskSerializer(tsk)
            json_data = JSONRenderer().render(serializer.data)
            return HttpResponse(json_data, content_type='application/json')

        qs = Task.objects.all()
        serializer = TaskSerializer(qs, many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data, content_type='application/json')

    def post(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        serializer = TaskSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            msg = {'msg': 'resource created successfully !'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')
        msg = {'msg': 'please send valid data'}
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data, content_type='application/json')

    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get('id')
        tsk = Task.objects.get(id=id)
        serializer = TaskSerializer(tsk, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            msg = {'msg': 'resource updated successfully !'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')

        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        data = JSONParser().parse(stream)
        id = data.get('id', None)

        if id is not None:
            tsk = Task.objects.get(id=id)
            tsk.delete()
            msg = {'msg': 'resource deleted successfully !'}
            json_data = JSONRenderer().render(msg)
            return HttpResponse(json_data, content_type='application/json')

        msg = {'msg': 'please provide valid id'}
        json_data = JSONRenderer().render(msg)
        return HttpResponse(json_data, content_type='application/json')
