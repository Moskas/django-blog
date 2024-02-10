# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt


from .models import Post, Image


# Create your views here.
class TutorialListView(ListView):
    model = Post
    context_object_name = "tutorial_list"
    template_name = "tutorials/tutorial_list.html"


class TutorialDetailView(DetailView):
    model = Post
    context_object_name = "tutorial"
    template_name = "tutorials/tutorial_detail.html"


# @csrf_exempt  # Note: Only for simplicity, use proper CSRF protection in production
def upload_image(request):
    if request.method == "POST":
        # image_name = request.POST.get("image_name")
        image_file = request.FILES.get("image_file")
        alt_text = request.POST.get("alt_text")

        if not image_file or not alt_text:
            return JsonResponse(
                {"error": "Please provide all required fields"}, status=400
            )

        # Create a new Image instance
        new_image = Image(name=image_file.name, alt_text=alt_text, Main_Img=image_file)
        new_image.save()

        return JsonResponse({"message": "Image uploaded successfully"})
    else:
        return JsonResponse({"error": "Only POST requests are allowed"}, status=405)


def image_view(request, image_name):
    try:
        image = Image.objects.get(name=image_name)
        with open(image.Main_Img.path, "rb") as img_file:
            response = HttpResponse(img_file.read(), content_type="image/jpeg")
        return response
    except Image.DoesNotExist:
        return HttpResponse("Image not found", status=404)
