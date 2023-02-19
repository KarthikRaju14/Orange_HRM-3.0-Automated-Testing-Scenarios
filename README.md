# Orange_HRM-3.0-Automated-Testing-Scenarios
This repository contains automated testing scenarios for Orange HRM 3.0 using Python Selenium. The test cases cover login, employee addition, employee edition, and employee deletion scenarios. Each scenario has preconditions, steps, and expected results outlined in detail.

The following scenarios are covered in this repository:

Branch "Testcase1":

Open the OrangeHRM 3.0 login page ->
Enter valid credentials in the username and password fields ->
Click on the Login button ->
Verify that the user is successfully logged in.


Branch "Testcase2":

Open the OrangeHRM 3.0 login page ->
Enter invalid credentials in the username and password fields ->
Click on the Login button ->
Verify that an error message is displayed indicating invalid login credentials.


Branch "Testcase3":

Login to the OrangeHRM 3.0 site with valid credentials ->
Navigate to the PIM module ->
Click on the Add button to add a new employee ->
Enter the employee details such as name, employee ID, employment status, etc. ->
Click on the Save button to save the employee details->
Verify that the employee is successfully added in the system.


Branch "Testcase4":

Login to the OrangeHRM 3.0 site with valid credentials->
Navigate to the PIM module ->
Search for an existing employee by employee ID or name ->
Click on the Edit button for the employee ->
Update the employee's information such as name, employment status, etc. ->
Click on the Save button to save the changes ->
Verify that the changes are successfully saved and reflected in the employee's information.


Branch "Testcase5":

Login to the OrangeHRM 3.0 site with valid credentials ->
Navigate to the PIM module ->
Search for an existing employee by employee ID or name ->
Click on the employee's name to view their details ->
Click on the Delete button to delete the employee ->
Confirm the deletion ->
Verify that the employee is successfully deleted from the system.
