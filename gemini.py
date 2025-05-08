import requests
import google.generativeai as gemini



model = gemini.GenerativeModel("gemini-1.5-flash")
gemini.configure(api_key='AIzaSyBSvCe6OXLOMlz8pOwpK4R-q8YAP9piZeY')

def Avaliation(data):
    prompt = f"""
    Com base aos seguintes dados:

    Usuário:
    - Nome: {data['user'].get('name')}
    - Seguidores: {data['user'].get('followers')}
    - Seguindo: {data['user'].get('following')}
    - Repositórios públicos: {data['user'].get('public_repos')}

    Repositórios:
    {str(data['repos'])}

    avalie o perfil, faça uma avaliação completa com sugestões de melhorias no perfil e repositórios e sugestões de como melhorar ex: como pode alcançar mais seguidores.
    """

    response =  model.generate_content([
        {"text": prompt}
    ])

    if response:
        return {"avaliacao": response.text}
    else:
        return f"Erro ao acessar Gemini: {response.text}"