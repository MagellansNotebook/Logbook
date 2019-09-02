# PassMngr
![main_menu](https://user-images.githubusercontent.com/51066040/64084137-8babd600-cd6b-11e9-8113-a1c3c0e4b2d1.png)

**PassMngr** is a simple vault which stores and encrypts plain text passwords use to login into any personnal or business accounts. The application uses Argon2 and Cryptography libraries for encryption and Peewee for database storage.

**Menu**

To navigate, press the corressponding number of the menu name.

**[ 0 ] Exit**

Press zero to exit the application.

**[ 1 ] Create New Account**

Press 1 to create a new account.

![create_new_account](https://user-images.githubusercontent.com/51066040/64084313-9bc4b500-cd6d-11e9-808d-91d4d8aec1da.png)

**Service Name** -  is the name of the host ie Github, Yahoo, Google, and Facebook accounts.

**Username** - is the username used to login into an account. Typically, the username uses the email address. However, some accounts may have a different set of rules. 

**Password** - is the secret word used to verify the username againts the password assigned to it.

**Group Item** - is a type of account. It is defined by the user how he/she wants to identify it. (ie Email, for example@yahoo.com.au, Account Login, for facebook.com)

Press enter key once the details are complete.

Note: If you made an error simply press enter and dont add any details on the following prompts. This will force an error to occur which will take you back to the main menu.

If all details are correct simply press enter. It will display all the input you have entered so you can verify if it is correct. Select Y if you wish to store the account in the database. Else, select N to go back to the main menu.

![encryption](https://user-images.githubusercontent.com/51066040/64085581-05958c80-cd77-11e9-8b45-bad99d72dd46.png)

If you select Y then it will prompt you to enter another set of password which will be used to encrypt the password used to login into your account. 
