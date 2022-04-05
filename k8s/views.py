import json

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MemberSerializer
from .models import Member


class SignUpAPI(APIView):
    def post(self, request):
        data = json.loads(request.body)
        user_id = data['user_id']
        user_pwd = data['user_pwd']
        member = Member(user_id=user_id, user_pwd=user_pwd)
        member.save()

        return Response(member.user_id)