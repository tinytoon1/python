*** Settings ***
Library  rf.addressbook
Library  Collections
Suite Setup  Init Fixtures
Suite Teardown  Destroy Fixtures

*** Test Cases ***
Add contact
    ${old_contacts}=  Get Contacts
    ${contact}=  New Contact  Alex  Murphy
    Add  ${contact}
    ${new_contacts}=  Get Contacts
    Append To List  ${old_contacts}  ${contact}
    Contacts Should Be Equal  ${old_contacts}  ${new_contacts}

Delete contact
    ${old_contacts}=  Get Contacts
    ${len}=  Get Length  ${old_contacts}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${contact}=  Get From List  ${old_contacts}  ${index}
    Delete  ${contact}
    ${new_contacts}=  Get Contacts
    Remove Values From List  ${old_contacts}  ${contact}
    Contacts Should Be Equal  ${old_contacts}  ${new_contacts}

Update contact
    ${old_contacts}=  Get Contacts
    ${len}=  Get Length  ${old_contacts}
    ${index}=  Evaluate  random.randrange(${len})  random
    ${new data}=  New Contact  Anne  Lewis
    ${contact}=  Get From List  ${old_contacts}  ${index}
    Update  ${contact}  ${new data}
    ${new_contacts}=  Get Contacts
    Set List Value  ${old_contacts}  ${index}  ${new data}
    Contacts Should Be Equal  ${old_contacts}  ${new_contacts}
