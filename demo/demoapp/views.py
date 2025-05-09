from django.shortcuts import render


def index(request):
    return render(request, "demoapp/index.html")

def tfjs_coco_ssd(request):
    return render(request, "demoapp/tfjs_coco_ssd.html")

def video_classifier(request):
    return render(request, "demoapp/video_classifier.html")

def video_object_detector(request):
    return render(request, "demoapp/video_object_detector.html")


def video_classifier_basic(request):
    return render(request, "demoapp/video_classifier_basic.html")