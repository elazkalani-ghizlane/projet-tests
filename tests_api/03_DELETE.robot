*** Settings ***
Library    RequestsLibrary    # Import de la bibliothèque pour les requêtes HTTP
Library    Collections        # Import de la bibliothèque pour les collections

*** Variables ***
${Base_URL}         https://mock-api-h0g7.onrender.com/    # Définition de l'URL de base de l'API
${API_KEY}          Cle-API-ReqRes-test-academy            # Clé API pour l'authentification
${Id_Utilisateur}   5


*** Test Cases ***
Test Requete DELETE
    &{headers}=    Create Dictionary    Authorization=Bearer ${API_KEY}
    
    # Creation d'un utilisateur pour le supprimer ensuite
    &{Corps_Creation}=  Create Dictionary    first_name=DeleteMe    last_name=User    email=delete.me@test.com
    ${CreateReponse}=   POST    ${Base_URL}api/users    json=${Corps_Creation}    headers=${headers}    expected_status=201
    ${id}=              Get From Dictionary    ${CreateReponse.json()}    id
    
    # Suppression de l'utilisateur cree
    ${Reponse}=    DELETE    ${Base_URL}api/users/${id}    headers=${headers}    expected_status=204