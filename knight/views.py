from .serializer import KnightSerialize
from .serializer import PieceSerializer
from .models import Pieces
from .models import KnightAudits
from board.moves import knight_moves
from board.utilits import colors

from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class Prices(GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = PieceSerializer

    def post(self, request):

        try:
            name_piece = request.data['name']
            color = request.data['color']

            color_valid = colors()

            if color not in color_valid:
                return Response({'result': 'color invalid'}, 400)

            if not name_piece:
                return Response(None, 400)

            piece = Pieces.objects.create(name=name_piece, color=color)

            return Response({'id': piece.id}, 200)

        except Exception as e:
            return Response(e, 500)


class PossitionKinight(GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = KnightSerialize

    def get(self, request, id_piece, position):

        # position = request.data['position']

        if len(position) > 2:
            return Response({'result': 'position invalid'}, 404)

        moves = knight_moves(position)

        if moves['error']:
            return Response({'result': 'position invalid'}, 404)

        piece = Pieces.objects.get(id=id_piece)

        moves = {
            'type_piece': piece.name,
            'color': piece.color,
            'possibility': moves['result']

        }

        KnightAudits.objects.create(
            user_name=request.user,
            type_piece=piece.name,
            position=position,
            possibilities=moves['possibility']
        )
        return Response(moves, 200)


class Login(GenericAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        try:
            user = User.objects.get(username=username)

        except User.DoesNotExist:
            return Response({'error': True, 'result': 'Username or Password invalid'}, 400)

        pwd_valido = check_password(password, user.password)

        if not pwd_valido:
            return Response({'error': True, 'result': 'Username or Password invalid'}, 400)

        token, _ = Token.objects.get_or_create(user=user)
        return Response({'Authorization': f'Token {token.key}'}, 200)
