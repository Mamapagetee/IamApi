from django.http import HttpResponse, JsonResponse;
from .models import Post, ContactMessage
from rest_framework import viewsets
from rest_framework import permissions
from portfolioApi.serializers import PostSerializer
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.views import APIView
# Create your views here.


class PostViewSet(viewsets.ModelViewSet):
    
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SendMail(APIView):

    def post(self, request):
        email = request.data
        newMessage = ContactMessage(email=email['email'], subject=email['subject'], message=email['message'])
        newMessage.save()
        send_mail(
            email['email'] + ': ' +email['subject'], #Subject
            email['message'], #Message
            'settings.EMAIL_HOST_USER', #Sender email
            ['ethan0jago@gmail.com'], #Recipients' email
            fail_silently=False,
        )
        return HttpResponse('sucess')
