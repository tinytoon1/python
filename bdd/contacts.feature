Scenario Outline: add contact
  Given contacts
  Given new contact with <firstname> and <lastname>
  When add a new contact
  Then the new contacts are equal to the old one

  Examples:
  | firstname | lastname |
  | Alex | Murphy |


Scenario Outline: delete contact
  Given non-empty contacts
  Given random contact
  When delete contact
  Then the new contacts are equal to the old contacts without the deleted contact


Scenario Outline: update contact
  Given non-empty contacts
  Given random contact
  When update firstname for contact
  Then the new contacts are equal to the old contacts after updating
