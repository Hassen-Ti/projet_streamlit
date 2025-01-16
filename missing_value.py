import streamlit as st
import pandas as pd

def matrix_theme():
    """Appliquer un style Matrix à l'application."""
    st.markdown("""
    <style>
    /* Background noir et vert */
    .main {
        background-color: #0d1117;
        color: #00ff41;
    }
    /* Titres en vert Matrix */
    h1, h2, h3, h4, h5, h6 {
        color: #00ff41;
    }
    /* Bordures des widgets */
    .stTextInput, .stSelectbox, .stSlider, .stFileUploader, .stButton, .stCheckbox {
        background-color: #0d1117 !important;
        color: #00ff41 !important;
        border: 1px solid #00ff41;
        border-radius: 5px;
    }
    /* Boutons stylisés */
    .stButton>button {
        background-color: #00ff41 !important;
        color: #0d1117 !important;
        border-radius: 8px;
        border: 1px solid #00ff41;
        padding: 8px 20px;
        font-size: 16px;
    }
    /* Boutons hover */
    .stButton>button:hover {
        background-color: #00cc33 !important;
        color: #ffffff !important;
    }
    /* Scrollbars */
    ::-webkit-scrollbar {
        width: 10px;
    }
    ::-webkit-scrollbar-thumb {
        background: #00ff41;
    }
    ::-webkit-scrollbar-track {
        background: #0d1117;
    }
    </style>
    """, unsafe_allow_html=True)

def missing_value_manager():
    """
    Gérer les valeurs manquantes dans un DataFrame avec Streamlit.
    """
    # Appliquer le style Matrix
    matrix_theme()

    st.title("💻 Matrix Data Manager")
    st.markdown("Bienvenue dans l'univers des données, où tout peut être maîtrisé...")

    # Étape 1 : Choix du mode de chargement du DataFrame
    st.header("📂 Charger un fichier")
    load_option = st.radio(
        "Choisissez une méthode pour charger les données :", 
        ("Téléverser un fichier", "Entrer une URL", "Utiliser un exemple")
    )

    df = None

    # Option 1 : Téléverser un fichier
    if load_option == "Téléverser un fichier":
        uploaded_file = st.file_uploader("Téléchargez un fichier CSV ou Excel :", type=["csv", "xlsx"])
        if uploaded_file is not None:
            try:
                if uploaded_file.name.endswith(".csv"):
                    df = pd.read_csv(uploaded_file)
                elif uploaded_file.name.endswith(".xlsx"):
                    df = pd.read_excel(uploaded_file)
                st.success("✅ Fichier chargé avec succès !")
                st.write("### 🌟 Aperçu du DataFrame :")
                st.dataframe(df)
            except Exception as e:
                st.error(f"❌ Erreur lors du chargement du fichier : {e}")

    # Option 2 : Entrer une URL
    elif load_option == "Entrer une URL":
        url = st.text_input("Entrez l'URL d'un fichier CSV :")
        if url:
            try:
                df = pd.read_csv(url)
                st.success("✅ Fichier chargé avec succès depuis l'URL !")
                st.write("### 🌟 Aperçu du DataFrame :")
                st.dataframe(df)
            except Exception as e:
                st.error(f"❌ Erreur lors du chargement du fichier depuis l'URL : {e}")

    # Option 3 : Utiliser un exemple intégré
    elif load_option == "Utiliser un exemple":
        example_dataset = st.selectbox(
            "Choisissez un dataset d'exemple :", 
            ["Iris Dataset", "Titanic Dataset", "Wine Quality Dataset"]
        )
        if example_dataset == "Iris Dataset":
            url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"
        elif example_dataset == "Titanic Dataset":
            url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
        elif example_dataset == "Wine Quality Dataset":
            url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/WineQuality.csv"

        try:
            df = pd.read_csv(url)
            st.success(f"✅ {example_dataset} chargé avec succès !")
            st.write("### 🌟 Aperçu du DataFrame :")
            st.dataframe(df)
        except Exception as e:
            st.error(f"❌ Erreur lors du chargement du dataset d'exemple : {e}")

    # Si un DataFrame a été chargé, passer à l'étape de gestion des valeurs manquantes
    if df is not None:
        # Étape 2 : Gérer les valeurs manquantes
        st.header("🔍 Colonnes avec des valeurs manquantes")
        missing_data = df.isna().sum()
        missing_data = missing_data[missing_data > 0]
        if not missing_data.empty:
            st.write("### 🛠️ Colonnes avec des valeurs manquantes :")
            st.dataframe(missing_data)
        else:
            st.write("✅ Aucune valeur manquante dans le DataFrame.")

        # Sélectionner les colonnes à traiter
        st.header("🎯 Sélection des colonnes")
        selected_columns = st.multiselect(
            "Sélectionnez les colonnes à traiter :", 
            df.columns
        )

        # Choisir la méthode de remplacement
        st.header("⚙️ Choix de la méthode de remplacement")
        method = st.selectbox(
            "Choisissez une méthode de remplacement :", 
            ["Moyenne", "Médiane", "Mode", "Valeur personnalisée", "Aucune"]
        )

        # Saisie d'une valeur personnalisée si choisie
        custom_value = None
        if method == "Valeur personnalisée":
            custom_value = st.text_input("Entrez la valeur personnalisée :")

        # Bouton pour appliquer la méthode de remplacement
        if st.button("🚀 Appliquer la méthode de remplacement"):
            if not selected_columns:
                st.warning("⚠️ Veuillez sélectionner au moins une colonne.")
            else:
                try:
                    if method == "Moyenne":
                        df[selected_columns] = df[selected_columns].fillna(df[selected_columns].mean())
                    elif method == "Médiane":
                        df[selected_columns] = df[selected_columns].fillna(df[selected_columns].median())
                    elif method == "Mode":
                        for col in selected_columns:
                            df[col] = df[col].fillna(df[col].mode()[0])
                    elif method == "Valeur personnalisée" and custom_value:
                        df[selected_columns] = df[selected_columns].fillna(custom_value)
                    st.success("✅ Valeurs manquantes remplacées avec succès !")
                    st.write("### 🌟 DataFrame après traitement :")
                    st.dataframe(df)
                except Exception as e:
                    st.error(f"❌ Une erreur s'est produite : {e}")

        # Option pour supprimer des colonnes avec trop de valeurs manquantes
        st.header("🗑️ Suppression des colonnes")
        threshold = st.slider(
            "Seuil de pourcentage de NaN au-delà duquel supprimer les colonnes :", 
            0, 100, 50
        )
        if st.button("🗑️ Supprimer les colonnes dépassant le seuil"):
            missing_percent = (df.isna().sum() / len(df)) * 100
            columns_to_drop = missing_percent[missing_percent > threshold].index
            if not columns_to_drop.empty:
                df.drop(columns=columns_to_drop, inplace=True)
                st.success(f"✅ Colonnes supprimées : {', '.join(columns_to_drop)}")
                st.write("### 🌟 DataFrame après suppression :")
                st.dataframe(df)
            else:
                st.info("ℹ️ Aucune colonne ne dépasse le seuil sélectionné.")

        # Option pour supprimer les lignes avec des NaN
        st.header("🗑️ Suppression des lignes")
        if st.button("🗑️ Supprimer les lignes contenant des NaN"):
            initial_shape = df.shape
            df.dropna(inplace=True)
            st.success(f"✅ Lignes supprimées : {initial_shape[0] - df.shape[0]}")
            st.write("### 🌟 DataFrame après suppression :")
            st.dataframe(df)

        # Afficher un résumé final du DataFrame
        st.header("📊 Résumé final")
        if st.checkbox("Afficher un résumé des données"):
            st.write("### 📊 Statistiques descriptives :")
            st.dataframe(df.describe(include='all'))

# Exemple d'utilisation
if __name__ == "__main__":
    # Lancer l'application Streamlit
    st.set_page_config(page_title="Matrix Data Manager", layout="wide")
    missing_value_manager()
