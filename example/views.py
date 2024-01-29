# example/views.py
from datetime import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ImageForm
from PIL import Image, ImageFilter
import base64
from io import BytesIO


def index(request):
    now = datetime.now()
    html = f"""
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    """
    return HttpResponse(html)


def cover(request):
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data["user_image"]
            print(data)
            print(type(data))
            original_image = base64.b64encode(data.read())
            original_image = original_image.decode("utf-8")
            converted = Image.open(data)
            converted = converted.filter(ImageFilter.SHARPEN)
            image_bytes = BytesIO()
            converted.save(image_bytes, "JPEG")
            image = base64.b64encode(image_bytes.getvalue())
            image = image.decode("utf-8")
            # handle_uploaded_file(data)
            # return HttpResponseRedirect("image", image_id=str(data))
            # return redirect("image", image_id=str(data))
            html = f"""
                    <html>
                        <body>
                            <h1>Original image:
                            &emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;
                            Sharpened image:
                            </h1>
                            <img src="data:image/png;base64,{ original_image }">
                            <img src="data:image/png;base64,{ image }">
                        </body>
                    </html>
                    """
            return HttpResponse(html)
        else:
            print("Invalid form")
    else:
        form = ImageForm()
    return render(request, "example/cover.html", {"form": form})


def handle_uploaded_file(f):
    with open("example/static/media/" + str(f), "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    # blur_image("example/static/media/" + str(f))


def display_image(request, image_id):
    return render(request, "example/product.html", {"image_id": image_id})
