from django.shortcuts import render
# import io
# from rest_framework.parsers import JSONParser
# from .models import Student
# from .serializers import StudentSerializer
# from rest_framework.renderers import JSONRenderer
# from django.http import HttpResponse

#  def student_api(request):
#   if request.method == 'GET':
#    json_data = request.body
#    stream = io.ByteIo(json_data)
#    pythondata = JSONParser().parse(stream)
#    id = pythondata.get('id', None)
#    if id is not None:
#     stu = Student.objects.get(id = id)
#     serializer = StudentSerializer(stu)
#     json_data = JSONRenderer().render(serializer.data)
#     return HttpResponse(json_data, content_type = 'application/json')

