from django.urls import path
from .views import list_prompts, get_prompt, create_prompt

urlpatterns = [
    path('prompts/', list_prompts, name='list_prompts'),
    path('prompts/create/', create_prompt, name='create_prompt'),
    path('prompts/<str:prompt_id>/', get_prompt, name='get_prompt'),
]