from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import comment
import json
from django.utils import timezone


# Create your views here.

def index(request):
    return render(request, 'index.html')

def get_comments(request):
    if request.method == 'GET':
        comments = comment.objects.all().order_by('-created_at')
        data = [
            {
                'name': c.name,
                'comment': c.comment,
                'created_at': c.created_at.strftime('%Y-%m-%d %H:%M:%S')
            } for c in comments
        ]
        return JsonResponse({'comments': data}, status=200)  # 包在物件裡

@csrf_exempt
def post_comment(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        name = body.get('name')
        comment_text = body.get('comment')
        c = comment(name=name, comment=comment_text, created_at=timezone.now())
        c.save()
        return HttpResponse(status=201)