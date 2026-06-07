*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${Base_URL}         https://mock-api-h0g7.onrender.com/
${API_KEY}          Cle-API-ReqRes-test-academy
${User_Id}          1

*** Test Cases ***
Test Requete GET Single User
    &{headers}=     Create Dictionary    Authorization=Bearer ${API_KEY}
    
    # Creation d'un utilisateur pour le recuperer ensuite
    &{Corps_Creation}=  Create Dictionary    first_name=GetMe    last_name=User    email=get.me@test.com
    ${CreateReponse}=   POST    ${Base_URL}api/users    json=${Corps_Creation}    headers=${headers}    expected_status=201
    ${User_Id}=         Get From Dictionary    ${CreateReponse.json()}    id

    ${Reponse}=     GET    ${Base_URL}api/users/${User_Id}    headers=${headers}    expected_status=200
    Log             ${Reponse.json()}
    
    # Validation structurelle
    Dictionary Should Contain Key    ${Reponse.json()}    data
    Dictionary Should Contain Key    ${Reponse.json()}    support
    
    # Validation du contenu DATA
    ${data}=        Get From Dictionary    ${Reponse.json()}    data
    Dictionary Should Contain Key    ${data}    id
    Dictionary Should Contain Key    ${data}    email
    Dictionary Should Contain Key    ${data}    first_name
    Dictionary Should Contain Key    ${data}    last_name
    Dictionary Should Contain Key    ${data}    avatar
    
    # Validation type de données (exemple simple)
    ${id}=          Get From Dictionary    ${data}    id
    Should Be Equal As Integers    ${id}    ${User_Id}