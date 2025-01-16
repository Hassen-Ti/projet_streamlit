import streamlit as st

# Fonction pour le style Matrix
def matrix_theme():
    st.markdown("""
    <style>
    body {
        background-color: #0d1117;
        color: #00ff41;
        font-family: 'Courier New', Courier, monospace;
    }
    .main {
        background-color: #0d1117;
        color: #00ff41;
        text-align: center;
    }
    h1, h2, h3 {
        color: #00ff41;
    }
    .matrix-card {
        width: 170px; /* Taille ajustée */
        height: 170px; /* Taille ajustée */
        background-color: #0d1117;
        color: #00ff41;
        border: 2px solid #00ff41;
        border-radius: 10px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0px;
        text-align: center;
        font-size: 14px;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease-in-out;
        box-shadow: 0 0 10px #00ff41;
        animation: glow 2s infinite alternate;
        flex-direction: column;
    }
    .matrix-card:hover {
        transform: scale(1.1);
        box-shadow: 0 0 20px #00ff41;
        background-color: #00cc33;
    }
    .matrix-card i {
        font-size: 40px;
        margin-bottom: 20px;
    }
    @keyframes glow {
        from {
            box-shadow: 0 0 10px #00ff41;
        }
        to {
            box-shadow: 0 0 20px #00cc33;
        }
    }
   .matrix-container {
    display: grid;
    grid-template-columns: repeat(2, auto); /* Ajuste automatiquement la taille des colonnes */
    gap: 20px; /* Espace entre les cartes horizontalement et verticalement */
    justify-content: center; /* Centre les cartes horizontalement */
    align-items: center; /* Centre les cartes verticalement */
    margin-top: 30px; /* Réduit l'espace au-dessus des cartes */
}

.matrix-card {
    width: 150px; /* Taille ajustée */
    height: 150px; /* Taille ajustée */
    margin: 0; /* Supprime toute marge externe */
    padding: 0; /* Supprime tout padding interne */
}

    .matrix-title {
        text-align: center;
        margin-bottom: 30px;
        animation: fadeIn 2s ease-in-out;
    }
    @keyframes fadeIn {
        from {
            opacity: 0;
        }
        to {
            opacity: 1;
        }
    }
    </style>
    """, unsafe_allow_html=True)


# Fonction pour afficher l'accueil
def display_home():
    st.markdown("""
    <div class="matrix-title">
        <h1>💻 Welcome to the Matrix Data Manager 💻</h1>
        <p>Explorez, Manipulez, Analysez et Apprenez avec vos données.</p>
    </div>
    """, unsafe_allow_html=True)

# Fonction pour afficher les cartes animées
def display_cards():
    st.markdown("""
    <div class="matrix-container">
        <div class="matrix-card" onclick="window.location.href='/Missing Value Manager'">
            <i>🔍</i>
            Missing Value Manager
        </div>
        <div class="matrix-card" onclick="window.location.href='/Preprocessing'">
            <i>⚙️</i>
            Preprocessing
        </div>
        <div class="matrix-card" onclick="window.location.href='/Dashboard'">
            <i>📊</i>
            Dashboard
        </div>
        <div class="matrix-card" onclick="window.location.href='/Machine Learning'">
            <i>🤖</i>
            Machine Learning
        </div>
    </div>
    """, unsafe_allow_html=True)

# Fonction principale
def main():
    # Appliquer le style Matrix
    matrix_theme()

    # Afficher la page d'accueil
    display_home()

    # Afficher les cartes animées en forme de carré
    display_cards()

# Lancer l'application
if __name__ == "__main__":
    st.set_page_config(page_title="Matrix Data Manager", layout="wide")
    main()
