from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<p>We are at the index view</p>')



def listStudents(request):
    list= [
        {
            'id': 1,
            'name': 'John Doe',
            'age': 20,
        },
        {
            'id': 2,
            'name': 'Jane Doe',
            'age': 25,
        },
    ]
    return render(request, 'djangoApp/list.html', {
        # 'students': [student for student in list if student['id'] == id],
        'studens': list
    })

def detailsStudent(request, id):
    list= [
        {
            'id': 1,
            'name': 'John Doe',
            'age': 20,
        },
        {
            'id': 2,
            'name': 'Jane Doe',
            'age': 25,
        },
    ]
    student = next((student for student in list if student['id'] == id), None)
    return render(request, 'djangoApp/details.html', {
        'student': student
        })
