# Read Me

**Test Framework**: Selenium with Python

This ReadMe provides an overview of the code. The code uses the Selenium library to perform user actions on https://ryze-staging.formedix.com/sign-in.

## Code Structure
1. **LoginPage**: This class performs the login operation on the web page. It contains a **login** method that takes a username and password as parameters.
2. **NavigatePages**: This class represents the navigation through different pages once the user is logged in. It contains a **navigate_to_page** method that performs click actions to reach the Medical History Form.
3. **UserActions**: This class represents the user actions once the Medical History Form is reached. It includes methods such as **navigate_medical_history_form** which navigates the medical history form, **edit_description** which performs adding inputs in the Description and Local fields, **verify_description_changes** which verifies if the changes are applied to the Main Form and Property Panel, and **logout** that performs the logout operation once changes are verified.
4. **UserActionsFramework**: This class serves as a framework for executing user actions. It initializes the Webdriver, creates instances of other classes, and provides methods for the operation done on the web page.
