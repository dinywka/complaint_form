from django.http import HttpResponse
from django.shortcuts import render
import sqlite3
from .models import UserComplaint


def home(request):
    return render(request, "home.html")

# def complaint(request):
#     if request.method == "GET":
#         return render(request, "complaint.html")
#     elif request.method == "POST":
#         username = request.POST.get("username")
#         user_complaint = request.POST.get("user_complaint")
#
#         with sqlite3.connect('database/db.db') as connection:
#             cursor = connection.cursor()
#             query = """
#             INSERT INTO users (username, user_complaint) VALUES (?, ?)
#                         """
#             cursor.execute(query, (username, user_complaint))
#             connection.commit()
#         return HttpResponse("Жалоба успешно отправлена")
#     else:
#         return HttpResponse("Что-то пошло не так")
#
# def list(request):
#     if request.method == "GET":
#         with sqlite3.connect('database/db.db') as connection:
#             cursor = connection.cursor()
#             query = """
#             SELECT username, user_complaint from users
#                         """
#             cursor.execute(query)
#             result = cursor.fetchall()
#             connection.commit()
#     return HttpResponse(result)
#

def complaint(request):
    if request.method == "GET":
        return render(request, "complaint.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        user_complaint = request.POST.get("user_complaint")

        complaint = UserComplaint(username=username, user_complaint=user_complaint)
        complaint.save()

        return (HttpResponse("Жалоба успешно отправлена"))
    else:
        return HttpResponse("Что-то пошло не так")


def list(request):
    if request.method == "GET":
        complaints = UserComplaint.objects.all()

        formatted_complaints = ["{}: {}".format(complaint.username, complaint.user_complaint) for complaint in
                                complaints]
        response_text = "\n".join(formatted_complaints)

        return HttpResponse(response_text)













