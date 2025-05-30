from django.shortcuts import render
from .models import QuestionPaper

def paper_list(request):
    papers = QuestionPaper.objects.all()
    return render(request, 'papers/paper_list.html', {'papers': papers})
