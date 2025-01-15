import streamlit_authenticator as stauth

# Liste des mots de passe que tu veux utiliser
passwords = ["motdepasse1", "motdepasse2"]

# Générer les mots de passe hachés
hashed_passwords = stauth.Hasher(passwords).generate()

# Afficher les mots de passe hachés
print(hashed_passwords)
