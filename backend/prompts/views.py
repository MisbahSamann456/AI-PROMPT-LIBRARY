import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Prompt


@require_http_methods(["GET"])
def list_prompts(request):
    prompts = Prompt.objects.all()
    data = []
    for p in prompts:
        data.append({
            'id': str(p.id),
            'title': p.title,
            'complexity': p.complexity,
            'created_at': p.created_at.isoformat(),
            'view_count': 0
        })
    return JsonResponse(data, safe=False)


@require_http_methods(["GET"])
def get_prompt(request, prompt_id):
    try:
        prompt = Prompt.objects.get(id=prompt_id)
    except Prompt.DoesNotExist:
        return JsonResponse({'error': 'Prompt not found'}, status=404)

    return JsonResponse({
        'id': str(prompt.id),
        'title': prompt.title,
        'content': prompt.content,
        'complexity': prompt.complexity,
        'created_at': prompt.created_at.isoformat(),
        'view_count': 0
    })


@csrf_exempt
@require_http_methods(["POST"])
def create_prompt(request):
    data = json.loads(request.body)

    prompt = Prompt.objects.create(
        title=data['title'],
        content=data['content'],
        complexity=data['complexity']
    )

    return JsonResponse({
        'id': str(prompt.id),
        'title': prompt.title,
        'content': prompt.content,
        'complexity': prompt.complexity,
        'created_at': prompt.created_at.isoformat(),
        'view_count': 0
    })