from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


def home(request):
    if request.user.is_authenticated:
        return redirect("companies:list")
    return render(request, "base.html")


@api_view(["GET"])
@permission_classes([AllowAny])
def health_check(request):
    return Response({
        "status": "success",
        "message": "Swarno EventOS API is running",
        "application": "Swarno EventOS",
        "version": "0.1.0",
    })
