import os
import json
import torch
import torchvision.transforms as transforms
from PIL import Image

from .inferences import FashionMNIST
from .models import Member
from django.core.files.storage import FileSystemStorage

from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MemberSerializer


class SignUpAPI(APIView):
    def post(self, request):
        data = json.loads(request.body)
        user_id = data['user_id']
        user_pwd = data['user_pwd']
        member = Member(user_id=user_id, user_pwd=user_pwd)
        member.save()

        return Response(member.user_id)


class InferenceCnnAPI(APIView):
    def post(self, request):
        # image 파일 추출
        file = request.FILES['cnn_image']

        if file is None:
            return '선택된 파일이 없습니다'
        elif os.path.exists('k8s/assets/image/cnn.png'):
            os.remove('k8s/assets/image/cnn.png')

        # image 저장
        fs = FileSystemStorage()
        filename = fs.save('k8s/assets/image/cnn.png', file)

        # 저장한 image load, 1차원으로 수정
        try:
            im = Image.open(filename).convert('L')
        except Exception as e:
            return Response('')


        # PIL Image -> Tensor로 변환
        t = transforms.Compose([
            transforms.Resize(size=(28, 28)),
            transforms.ToTensor()
        ])

        # model parameter 맞게 차원 조정 ( 1, 1 , 28, 28 )
        test_data = t(im).unsqueeze(0)

        # cuda 설정
        device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

        model = FashionMNIST()
        model.to(device=device)
        model.load_state_dict(torch.load('k8s/models/cnn.pt'))
        model.eval()

        out = model(test_data)

        _, predicted = torch.max(out.data, 1)

        output_label = {
            0: 'T-shirt/Top',
            1: 'Trouser',
            2: 'Pullover',
            3: 'Dress',
            4: 'Coat',
            5: 'Sandal',
            6: 'Shirt',
            7: 'Sneaker',
            8: 'Bag',
            9: 'Ankle Boot'
        }

        result = output_label[predicted.item()]
        return Response(result)