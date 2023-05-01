import requests
import streamlit as st

BASE_URL = 'https://api.github.com'

def selecionarUsuario(username):
    url = f'{BASE_URL}/users/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def ui():
    st.markdown('<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">', unsafe_allow_html=True)

    st.title('Consulta Github')
    username = st.text_input('Insira o username do usuário')

    if st.button('Buscar'):
        infoUsuario = selecionarUsuario(username)
        if infoUsuario is not None:
            st.markdown(f'''

                <div class="card" style="width: 18rem;">
                    <img class="card-img-top" src="{infoUsuario['avatar_url']}" alt="Imagem de capa do card">
                    <div class="card-body">
                        <h5 class="card-title">{infoUsuario['login']}</h5>
                        <p class="card-text">{infoUsuario['bio']}</p>
                        <a href="{infoUsuario['html_url']}" style="color: white;text-decoration: none;" class="btn btn-primary">Ver perfil</a>
                    </div>
                </div>

            ''', unsafe_allow_html=True)


ui()