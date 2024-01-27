from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Group, Note

from .forms import GroupForm, NoteForm

from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from .serializers import GroupSerializer, NoteSerializer


# Create your views here.

# TODO: EZT MÉG MEG KELL CSINÁLNI
#* LOGIN and LOGOUT 
def login_user(request):
    error = ""
    if request.method == "POST":
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        user = authenticate(request, username=un, password=pw)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            error = "Inappropriate user or password"
            
    context = { 'error': error }        
    return render(request, 'note/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')

def reg_user(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')

    context = {'form' : form}
    return render(request, 'note/reg.html', context)


@login_required(login_url='login')
def index_page(request):
    logged_user = request.user
    groups = Group.objects.all()
    notes = Note.objects.all()
    # groups = Group.objects.filter(user=logged_user)
    # notes = Note.objects.all(user=logged_user)
    form = GroupForm(request.POST)

    if request.method == 'POST':    
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'groups' : groups, 'notes' : notes, 'form' : form}

    return render(request, 'note/index.html', context)

# /notes/{id}
@login_required(login_url='login')
def note_page(request, pk):
    note = Note.objects.get(id=pk)
    form = NoteForm(instance=note)

    context = {'form' : form, 'note' : note} 

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)

        if form.is_valid():
            form.save()
            return redirect('index')
        
    return render(request, 'note/note.html', context)

@login_required(login_url='login')
def delete_group(request, pk):
    group = Group.objects.get(id=pk)
    group.delete()

    return redirect('index')

@login_required(login_url='login')
def new_note(request): 
    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
        
    else:
        form = NoteForm()
        context = {'form' : form}
        return render(request, 'note/new-note.html', context)

@login_required(login_url='login')
def delete_note(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()

    return redirect('index')



#* API
@login_required(login_url='login')
@api_view(['GET'])
def api_overview(request):
    api_urls = {
        # groups
        'Groups list' : '/api/groups/',
        'Group detail' : '/api/groups/<str:pk>',
        "Group's Notes list" : '/api/groups/<str:pk>/notes',
        'Create group' : '/api/groups/create',
        'Update group' : '/api/groups/update/<str:pk>',
        'Delete group' : '/api/groups/delete/<str:pk>',
        # notes
        "Notes list" : '/api/notes',
        'Note detail' : '/api/notes/<str:pk>/',
        'Create note' : '/api/notes/create/',
        'Update note' : '/api/notes/update/<str:pk>/',
        'Delete note' : '/api/notes/delete/<str:pk>/',
    }
    return Response(api_urls)


#* API GROUPS
@login_required(login_url='login')
@api_view(['GET'])
def api_groups(request):
    groups = Group.objects.all()
    serializer = GroupSerializer(groups, many=True)

    return Response(serializer.data)

@login_required(login_url='login')
@api_view(['GET'])
def api_group_by_id(request, pk):
    group = Group.objects.get(id=pk)
    serializer = GroupSerializer(group, many=False)
    return Response(serializer.data)

@login_required(login_url='login')
@api_view(['GET'])
def api_group_notes(request, pk):
    target_group = Group.objects.get(id=pk)
    notes = Note.objects.filter(group=target_group)
    serializer = NoteSerializer(notes, many=True)
    
    return Response(serializer.data)

@login_required(login_url='login')
@api_view(['POST'])
@parser_classes([JSONParser])
def api_create_group(request):
    serializer = GroupSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@login_required(login_url='login')
@api_view(['POST'])
def api_update_group(request, pk):
    target_group = Group.objects.get(id=pk)
    serializer = GroupSerializer(instance= target_group, data=request.data)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@login_required(login_url='login')
@api_view(['DELETE'])
def api_delete_group(request, pk):
    group = Group.objects.get(id=pk)
    group.delete()

    return Response({"detail" : 'Group deleted!'})


#* api/notes
@login_required(login_url='login')
@api_view(['GET'])
def api_notes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)

    return Response(serializer.data)

#* api/notes/<str:pk>
@login_required(login_url='login')
@api_view(['GET'])
def api_notes_by_id(request, pk):
    target_note = Note.objects.get(id=pk)
    serializer = NoteSerializer(target_note, many=False)
    
    return Response(serializer.data)

#* api/notes/create
@login_required(login_url='login')
@api_view(['POST'])
@parser_classes([JSONParser]) # ez a dekorátor kell ahhoz, hogy megfelelően működjön a kapott adat parse-olása
def api_create_notes(request):
    serializer = NoteSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

#* api/notes/update/<str:pk>
@login_required(login_url='login')
@api_view(['POST'])
@parser_classes([JSONParser])
def api_update_notes(request, pk):
    target_note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=target_note, data=request.data)
    
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

#* api/notes/delete/<str:pk>
@login_required(login_url='login')
@api_view(['DELETE'])
@parser_classes([JSONParser])
def api_delete_notes(request, pk):
    note = Note.objects.get(id=pk)
    note.delete()

    return Response({"detail" : 'Note deleted!'})
