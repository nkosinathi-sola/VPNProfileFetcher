from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .ec2_connection import get_files_from_ec2

def home(request):
    files = get_files_from_ec2()
    print(files)  # Add this line for debugging
    return render(request, 'file_manager/home.html', {'files': files})

def download_files(request):
    if request.method == 'POST':
        selected_files = request.POST.getlist('file_selection')
        # Implement file download logic here using selected_files
        # For example, using the 'paramiko' library to fetch files from the EC2 instance
        return HttpResponse("Files downloaded successfully.")
    else:
        return HttpResponse("Invalid request method.")
    