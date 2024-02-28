from django.shortcuts import render
from django.contrib.auth import authenticate, login
from .models import SearchData  # Import the SearchData model



# Create your views here.
from django.shortcuts import render, redirect,HttpResponse
from .forms import SignupForm

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('taketea')  # Redirect to login page after signup
            # return HttpResponse("Login")
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)  # Log in the user
            # Redirect to a specific page after successful login
            return redirect('taketea')  # Replace 'dashboard' with the appropriate URL name

        else:
            # Handle authentication failure (incorrect credentials)
            error_message = "Invalid username or password. Please try again."
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')

# def taketea(request):
#     return render(request,'taketea.html')

def search_paragraphs(n1, n2):
    paragraphs = n1.split('\n\n')  # Split input text into paragraphs

    found_paragraphs = []
    for idx, paragraph in enumerate(paragraphs, 1):  # Enumerate paragraphs starting from 1
        if n2.lower() in paragraph.lower():  # Case-insensitive search
            found_paragraphs.append(idx)

    return found_paragraphs
# def taketea(request):
#     try:
#         if request.method == "POST":
#             n1 = str(request.POST.get('num1'))
#             n2 = str(request.POST.get('num2'))
#             message=""
#             found_paragraphs = search_paragraphs(n1, n2)
#             if found_paragraphs:
#                 # message = f"Search term '{n2}' found in paragraph(s): {found_paragraphs}"
#                 search_data = SearchData(paragraph=n1, word=n2)
#                 search_data.save()
#                 message = f" {n2}| Paragraph: {found_paragraphs}"
#             else:
#                 message = f"Search term '{n2}' not found."
#         else:
#             message = "Invalid request method. Please use POST."
#     except Exception as e:
#         message = f"An error occurred: {str(e)}"
    
#     return render(request, "taketea.html", {'message': message})

def taketea(request):
    try:
        message = None
       
        if request.method == "POST":
            n1 = request.POST.get('num1', '').strip()  # Get input data and remove leading/trailing whitespace
            n2 = request.POST.get('num2', '').strip()
           
            if not n1 or not n2:  # Check if either input is empty
                message = "Please enter both paragraph and word to search."
            else:
                found_paragraphs = search_paragraphs(n1, n2)
                if found_paragraphs:
                    search_data = SearchData(paragraph=n1, word=n2)
                    search_data.save()
                    message = f"Search term '{n2}' found in paragraph(s): {found_paragraphs}"
                else:
                    message = f"Search term '{n2}' not found."
          
    except Exception as e:
        message = f"An error occurred: {str(e)}"
    
    return render(request, "taketea.html", {'message': message})