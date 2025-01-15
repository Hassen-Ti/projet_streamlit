import pytest
from bibliotheque import Bibliotheque

@pytest.fixture
def biblio():
    byb = Bibliotheque()
    byb.ajouter_livre("Python pour les débutants", "Alice")
    byb.ajouter_livre("L'art du testing", "Bob")
    return byb

def test_ajouter_livre(biblio):
    biblio.ajouter_livre("Nouveau livre", "Auteur inconnu")
    livre = biblio.rechercher_livre("Nouveau livre")
    assert livre is not None
    assert livre["auteur"] == "Auteur inconnu"

def test_rechercher_livre(biblio):
    livre = biblio.rechercher_livre("Python pour les débutants")
    assert livre is not None
    assert biblio.rechercher_livre("Inexistant") is None

def test_emprunter_livre(biblio):
    biblio.emprunter_livre("Python pour les débutants")
    assert biblio.rechercher_livre("Python pour les débutants")["emprunté"] is True
    with pytest.raises(ValueError):
        biblio.emprunter_livre("Python pour les débutants")
    with pytest.raises(ValueError):
        biblio.emprunter_livre("Inexistant")

def test_retourner_livre(biblio):
    biblio.emprunter_livre("L'art du testing")
    biblio.retourner_livre("L'art du testing")
    assert biblio.rechercher_livre("L'art du testing")["emprunté"] is False
    with pytest.raises(ValueError):
        biblio.retourner_livre("L'art du testing")
    with pytest.raises(ValueError):
        biblio.retourner_livre("Inexistant")
