from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer, NoteSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Note


class NoteListCreate(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(author=self.request.user)
        else:
            print(serializer.errors)


class NoteDelete(generics.DestroyAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Note.objects.filter(author=user)


class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]



# from django.shortcuts import render
# from django.contrib.auth.models import User
# from rest_framework import generics
# from .serializers import UserSerilalizer, NoteSerializer
# from rest_framework.permissions import IsAuthenticated, AllowAny
# from .models import Note

# # Create your views here.
# #built in django to auntomaticallly creat enew user or new object

# class CreateUserView(generics.CreateAPIView):
#     queryset =  User.objects.all()
#     serializer_class = UserSerilalizer
#     permission_classes = [AllowAny]


# # queryset =  User.objects.all()
# # check already exixts user -> list of all the object that will looking while creating a new -> so same user doesnot get cretaed

# #serializer_class = User
# # what kind of data we use to create the new user

# # permission_classes = [AllowAny]
# #who can actually call this 

# class NoteListCreate(generics.ListCreateAPIView):
#     serializer_class = NoteSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         user= self.request.user
#         return Note.objects.filter(author=user)
    
#     def perform_create(self, serializer):
#         if serializer.is_valid():
#             serializer.save(author=self.requet.user)
#         else:
#             print(serializer.errors)

# class NoteDelete(generics.DestroyAPIView):
#     serializer_class = NoteSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         user= self.request.user
#         return Note.objects.filter(author=user)

# #author=self.requet.user =>added field to note

        
       
    
    
   
# #list all the notes that user has created or create new note
# # self.request.user-> to get specified user 
# # to get user which is authenticated and interacting with the root -> give user object
# #return Note.objects.all() = for all user
# # Note.objects.filter(author=user) -> note written by that perticular author