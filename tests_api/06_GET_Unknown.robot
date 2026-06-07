*** Settings ***
Library    RequestsLibrary
Library    Collections

*** Variables ***
${Base_URL}         https://mock-api-h0g7.onrender.com/
${API_KEY}          Cle-API-ReqRes-test-academy

*** Test Cases ***
Test Requete GET Resource List
    &{headers}=     Create Dictionary    Authorization=Bearer ${API_KEY}
    ${Reponse}=     GET    ${Base_URL}api/unknown    headers=${headers}    expected_status=200
    Log             ${Reponse.json()}
    
    # Validation structurelle typique d'une liste paginée
    Dictionary Should Contain Key    ${Reponse.json()}    page
    Dictionary Should Contain Key    ${Reponse.json()}    per_page
    Dictionary Should Contain Key    ${Reponse.json()}    total
    Dictionary Should Contain Key    ${Reponse.json()}    total_pages
    Dictionary Should Contain Key    ${Reponse.json()}    data
    Dictionary Should Contain Key    ${Reponse.json()}    support
    
    # Validation que 'data' est bien une liste
    ${data_list}=   Get From Dictionary    ${Reponse.json()}    data
    ${is_list}=     Evaluate    isinstance($data_list, list)
    Should Be True  ${is_list}
    
    # Validation Optionnelle : vérifier qu'il y a des éléments dans la liste
    ${len}=         Get Length    ${data_list}
    Should Be True  ${len} > 0