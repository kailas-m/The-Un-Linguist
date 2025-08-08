from django.http import JsonResponse
from .utils import generate_response, jumble_translate
import nltk

nltk.data.path.append('D:/unlinguist/nltk_data')

def chatbot_view(request):
    prompt = request.GET.get("prompt", "")
    if prompt:
        gpt_response = generate_response(prompt)
        jumbled = jumble_translate(gpt_response)
        return JsonResponse({"response": gpt_response, "jumbled": jumbled})
    return JsonResponse({"error": "No prompt provided"})
