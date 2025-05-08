from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .github import BuscarDadosnoGithub
from .gemini import Avaliation

class GeminiAvaliation(APIView):
    def post(self, request):
        username = request.data.get("username")
        if not username:
            return Response({"error": "Username é obrigatório."}, status=400)

        try:
            github_data = BuscarDadosnoGithub(username)
            if not github_data:
                return Response({"error": "Usuário não encontrado."}, status=404)

            gemini_response = Avaliation(github_data)

            return Response({
                "username": username,
                "Avaliation": gemini_response
            })
        
        except Exception as e:
            return Response({"error": f"Ocorreu um erro inesperado: {str(e)}"}, status=500)