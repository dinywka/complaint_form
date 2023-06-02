from django.http import HttpResponse
from django.shortcuts import render
import sqlite3

def home(request):
    return render(request, "home.html")

def complaint(request):
    if request.method == "GET":
        return render(request, "complaint.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        user_complaint = request.POST.get("user_complaint")

        with sqlite3.connect('database/db.db') as connection:
            cursor = connection.cursor()
            query = """
            INSERT INTO users (username, user_complaint) VALUES (?, ?)
                        """
            cursor.execute(query, (username, user_complaint))
            connection.commit()
        return HttpResponse("Жалоба успешно отправлена")
    else:
        return HttpResponse("Что-то пошло не так")