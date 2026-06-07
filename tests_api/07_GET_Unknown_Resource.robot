*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${Base_URL}         https://mock-api-h0g7.onrender.com/
${API_KEY}          Cle-API-ReqRes-test-academy
${Resource_Id}      2

*** Test Cases ***
Test Requete GET Single Resource
    &{headers}=     Create Dictionary    Authorization=Bearer ${API_KEY}
    ${Reponse}=     GET    ${Base_URL}api/unknown/${Resource_Id}    headers=${headers}    expected_status=200
    Log             ${Reponse.json()}
    
    # Validation structurelle
    Dictionary Should Contain Key    ${Reponse.json()}    data
    Dictionary Should Contain Key    ${Reponse.json()}    support
    
    # Validation du contenu DATA
    ${data}=        Get From Dictionary    ${Reponse.json()}    data
    Dictionary Should Contain Key    ${data}    id
    Dictionary Should Contain Key    ${data}    name
    Dictionary Should Contain Key    ${data}    year
    Dictionary Should Contain Key    ${data}    color
    Dictionary Should Contain Key    ${data}    pantone_value
    
    # Validation de l'ID
    ${id}=          Get From Dictionary    ${data}    id
    Should Be Equal As Integers    ${id}    ${Resource_Id}