import streamlit as st
# import pandas as pd

# st.markdown(
#     """
#     <style>
#     /* Change la couleur de l'arrière-plan */
#     .stApp {
#         background-color: red;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )
# st.title("Bienvenu sur le site web de Hassene")
# check_one = st.checkbox('Clique ici si tu veux.')
# if check_one:
#     st.write("haut li main batar")
#     st.image("http://pegleg.p.e.pic.centerblog.net/796ab94d.jpg")
# st.write('___')
# arrondissement = st.selectbox("Indiquez votre arrondissement de récupération ?",
#                               ['Brooklyn', 'Bronx', 'Manhassene','Queens',"nan"])
# st.write('___')

# # 

# if arrondissement == "Bronx":
#     st.write("Premiere video sur internet =) ")
#     st.video("https://www.youtube.com/watch?v=jNQXAC9IVRw")
# elif arrondissement == "Brooklyn":
#     st.write("timothee chalamet timothee machala :D ")
# elif arrondissement == "Manhassene":
#     st.img("C'est la ou je vis")

# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt

# # Charger le dataset Iris
# @st.cache_data
# def load_data():
#     return sns.load_dataset('iris')

# # Chargement des données
# data = load_data()

# # Titre principal
# st.title("Manipulation de données et création de graphiques")

# # Afficher le dataset
# st.write("Dataset Iris chargé :")
# st.dataframe(data)

# # Choix des colonnes pour X et Y
# x_col = st.selectbox("Choisissez la colonne X", data.columns)
# y_col = st.selectbox("Choisissez la colonne Y", data.columns)

# # Choix du type de graphique
# chart_type = st.selectbox("Quel graphique veux-tu utiliser ?", ["bar_chart", "scatter_chart", "line_chart"])

# # Création et affichage du graphique
# st.write("### Graphique sélectionné")
# if chart_type == "bar_chart":
#     # Bar Chart
#     if pd.api.types.is_numeric_dtype(data[y_col]):
#         fig, ax = plt.subplots()
#         sns.barplot(x=data[x_col], y=data[y_col], ax=ax)
#         st.pyplot(fig)
#     else:
#         st.write("Impossible de créer un bar chart : la colonne Y doit être numérique.")
# elif chart_type == "scatter_chart":
#     # Scatter Chart
#     fig, ax = plt.subplots()
#     sns.scatterplot(data=data, x=x_col, y=y_col, hue="species", ax=ax)
#     st.pyplot(fig)
# elif chart_type == "line_chart":
#     # Line Chart
#     if pd.api.types.is_numeric_dtype(data[y_col]):
#         fig, ax = plt.subplots()
#         sns.lineplot(data=data, x=x_col, y=y_col, hue="species", ax=ax)
#         st.pyplot(fig)
#     else:
#         st.write("Impossible de créer un line chart : la colonne Y doit être numérique.")

# # Option pour afficher la matrice de corrélation
# if st.checkbox("Afficher la matrice de corrélation"):
#     st.write("### Ma matrice de corrélation")
#     fig, ax = plt.subplots()
#     corr = data.select_dtypes(include="number").corr()
#     sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
#     st.pyplot(fig)






###### authentification


# import streamlit as st
# from streamlit_authenticator import Authenticate

# # Données des comptes utilisateurs
# lesDonneesDesComptes = {
#     'usernames': {
#         'utilisateur': {
#             'name': 'Utilisateur',
#             'password': 'utilisateurMDP',
#             'email': 'utilisateur@gmail.com',
#             'failed_login_attemps': 0,  # Géré automatiquement
#             'logged_in': False,         # Géré automatiquement
#             'role': 'utilisateur'
#         },
#         'root': {
#             'name': 'Administrateur',
#             'password': 'rootMDP',
#             'email': 'admin@gmail.com',
#             'failed_login_attemps': 0,  # Géré automatiquement
#             'logged_in': False,         # Géré automatiquement
#             'role': 'administrateur'
#         }
#     }
# }

# # Création d'une instance d'authentification
# authenticator = Authenticate(
#     lesDonneesDesComptes,  # Les données des comptes
#     "cookie_name",         # Nom du cookie
#     "cookie_key",          # Clé secrète du cookie
#     30                     # Expiration en jours
# )

# # Affichage du formulaire de connexion
# authenticator.login()

# # Gestion de l'accès en fonction de l'état d'authentification
# def accueil():
#     st.title("Bienvenue sur le contenu réservé aux utilisateurs connectés")
#     st.write("Vous êtes connecté avec succès !")

# if st.session_state.get("authentication_status"):
#     # Afficher le contenu protégé
#     accueil()
#     # Ajouter un bouton de déconnexion
#     authenticator.logout("Déconnexion", "sidebar")

# elif st.session_state.get("authentication_status") is False:
#     # Message d'erreur si les identifiants sont incorrects
#     st.error("Le nom d'utilisateur ou le mot de passe est incorrect.")

# elif st.session_state.get("authentication_status") is None:
#     # Message d'avertissement si les champs sont vides
#     st.warning("Les champs nom d'utilisateur et mot de passe doivent être remplis.")











import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ----------------------- Authentification ------------------------
# Données des comptes utilisateurs
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'Utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,  # Géré automatiquement
            'logged_in': False,         # Géré automatiquement
            'role': 'utilisateur'
        },
        'root': {
            'name': 'Administrateur',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,  # Géré automatiquement
            'logged_in': False,         # Géré automatiquement
            'role': 'administrateur'
        }
    }
}

# Création d'une instance d'authentification
authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie_name",         # Nom du cookie
    "cookie_key",          # Clé secrète pour le cookie
    30                     # Expiration en jours
)

# Affichage du formulaire de connexion
authenticator.login()

# ----------------------- Pages et navigation ------------------------
# Gestion de l'accès en fonction de l'état d'authentification
if st.session_state.get("authentication_status"):
    # Si l'utilisateur est connecté
    with st.sidebar:
        # Menu de navigation avec Streamlit Option Menu
        selection = option_menu(
            menu_title="Main Menu",  # Titre du menu
            options=["Accueil", "Dashboard", "Tâches", "Paramètres"],  # Options du menu
            icons=["house", "bar-chart", "list-task", "gear"],  # Icônes pour chaque option
            menu_icon="cast",  # Icône du menu principal
            default_index=0,  # Option par défaut
        )

    # ----------------------- Pages de contenu ------------------------
    if selection == "Accueil":
        st.title("Bienvenue sur la page d'accueil")
        st.write("Voici un aperçu général de votre application.")

    elif selection == "Dashboard":
        st.title("Dashboard : Manipulation de données et création de graphiques")

        # Charger le dataset Iris
        @st.cache_data
        def load_data():
            return sns.load_dataset('iris')

        # Chargement des données
        data = load_data()

        # Afficher le dataset
        st.write("Dataset Iris chargé :")
        st.dataframe(data)

        # Choix des colonnes pour X et Y
        x_col = st.selectbox("Choisissez la colonne X", data.columns)
        y_col = st.selectbox("Choisissez la colonne Y", data.columns)

        # Choix du type de graphique
        chart_type = st.selectbox("Quel graphique veux-tu utiliser ?", ["bar_chart", "scatter_chart", "line_chart"])

        # Création et affichage du graphique
        st.write("### Graphique sélectionné")
        if chart_type == "bar_chart":
            # Bar Chart
            if pd.api.types.is_numeric_dtype(data[y_col]):
                fig, ax = plt.subplots()
                sns.barplot(x=data[x_col], y=data[y_col], ax=ax)
                st.pyplot(fig)
            else:
                st.write("Impossible de créer un bar chart : la colonne Y doit être numérique.")
        elif chart_type == "scatter_chart":
            # Scatter Chart
            fig, ax = plt.subplots()
            sns.scatterplot(data=data, x=x_col, y=y_col, hue="species", ax=ax)
            st.pyplot(fig)
        elif chart_type == "line_chart":
            # Line Chart
            if pd.api.types.is_numeric_dtype(data[y_col]):
                fig, ax = plt.subplots()
                sns.lineplot(data=data, x=x_col, y=y_col, hue="species", ax=ax)
                st.pyplot(fig)
            else:
                st.write("Impossible de créer un line chart : la colonne Y doit être numérique.")

        # Option pour afficher la matrice de corrélation
        if st.checkbox("Afficher la matrice de corrélation"):
            st.write("### Ma matrice de corrélation")
            fig, ax = plt.subplots()
            corr = data.select_dtypes(include="number").corr()
            sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)

    elif selection == "Tâches":
        st.title("Gestion des tâches")
        st.write("Ajoutez ou visualisez vos tâches ici.")

    elif selection == "Paramètres":
        st.title("Paramètres de l'application")
        st.write("Modifiez vos paramètres ici.")

    # Bouton de déconnexion
    authenticator.logout("Déconnexion", "sidebar")

elif st.session_state.get("authentication_status") is False:
    # Message d'erreur si les identifiants sont incorrects
    st.error("Le nom d'utilisateur ou le mot de passe est incorrect.")

elif st.session_state.get("authentication_status") is None:
    # Message d'avertissement si les champs sont vides
    st.warning("Les champs nom d'utilisateur et mot de passe doivent être remplis.")
