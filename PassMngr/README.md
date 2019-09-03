# PassMngr
![main_menu](https://user-images.githubusercontent.com/51066040/64084137-8babd600-cd6b-11e9-8113-a1c3c0e4b2d1.png)

**PassMngr** is a simple password vault application. The program stores and encrypts plain text passwords use to login into any personnal or business accounts. It uses Argon2 and Cryptography libraries for encryption and Peewee for database storage. PassMngr runs a basic Command Line display with simplified selection for operations.

**Menu**

Each tile has a number corresponding to it. To navigate, press the number to run the option.

**[ 0 ] Exit**

The Exit menu simply closes the application.

**[ 1 ] Create New Account**

![create_new_account](https://user-images.githubusercontent.com/51066040/64084313-9bc4b500-cd6d-11e9-808d-91d4d8aec1da.png)

The Create New Account menu set-up a new entry into the Peewee database. The following details like Service Name, Username, Password, Group Item must be filled in order to save it into the database. If any of the details is blank then an error will occur. The information entered into the database is dependent on the user. 

Below is a basic example of the naming conventions used when entering a new account into the database:

* **Service Name** - the name of the host. Example: Github, Yahoo, Google, and Facebook accounts.

* **Username** - the username used to login into an account. Typically, the username uses the email address. However, some accounts may have a account rules. 

* **Password** - the password used to acccess the account.

* **Group Item** - type of account. Example: Email, for example@yahoo.com.au; Account Login, for facebook.com

Note: If the user made an error simply, press enter and dont add any details on it. This will force an error to occur which will take the user back to the main menu.

![encryption](https://user-images.githubusercontent.com/51066040/64085581-05958c80-cd77-11e9-8b45-bad99d72dd46.png)

The image above will appear as long as all information requested by the application is filled in. Also, the displayed data allows the user to confirm the input is correct.

By press the Y/y key, the application will prompt the user to enter a secret word to encrypt the password for the account.

Note: The secret word must be a maximum of 16 characters long. The same secret word can be used on multiple passwords. However, it is not ideal for security. Because, if the secret word is compromised then all password encryted by the secret word will be unlock. So, ensure to use a strong secret word when using it in multiple encryption. 

![successful_create_new_account](https://user-images.githubusercontent.com/51066040/64085870-76897400-cd78-11e9-89cb-15033d229361.png)

Once the process is complete a successful remark on top of the menu will appear. 

**[ 2 ] View Accounts**

![display_account](https://user-images.githubusercontent.com/51066040/64086695-0c270280-cd7d-11e9-91d1-bed8079189ac.png)

The View Accounts options displays all accounts saved in the database. It also includes the following details:

* **Service Name** - the actual host who provides services to the user.

* **Serial Number** - the number assigned to the account. The number is incremeting and automatically assigned by the database.

* **User Name** - it is the name used to access the account from the host services.

* **Group Item** - is defined by the type of account.

* **Date Time Group** - shows the time and date the account was created.

![account_details](https://user-images.githubusercontent.com/51066040/64086807-97a09380-cd7d-11e9-8463-67fda32e21ec.png)

Selecting Y/y and the serial number correspoding the account displays more information. The password will be displayed but it will be hashed. Also, the hash key is displayed.

Note: The secret key is case sensitive.

![decrypt](https://user-images.githubusercontent.com/51066040/64089130-fb2fbe80-cd87-11e9-93cf-d55de502ec1b.png)

Entering the correct secret word will decrypt the password and it will be diplayed on top of the main menu.

**[ 3 ] Update Key**

![update_key](https://user-images.githubusercontent.com/51066040/64089715-db4dca00-cd8a-11e9-8898-82e5fb48b364.png)

The Update Key edits the password of the account and secret word used to encrypt its password. Similar to View accounts, select Y/y and enter the serial number of the account. The user will be prompted to enter the secret word used for the account for verification.

![edit_account](https://user-images.githubusercontent.com/51066040/64090474-aa6f9400-cd8e-11e9-8a46-2e98fbafdd77.png)

Once, the secret key is verified a new message will appear below it. Simply, follow the prompt to edit/change the password followed by the secret word for encryption/decryption.

**[ 4 ] Delete Account**

![delete](https://user-images.githubusercontent.com/51066040/64092091-9d56a300-cd96-11e9-88d1-c31c557b812a.png)

The delete menu removes the account from the database. Directly, select Y/y and enter the serial number of the account the user wish to remove. 

Note: It will not ask the user to verify a secret word before deleting the account. So, be carefull when choosing delete because it cannot be undone once deleted.

**[ 5 ] Refresh Command Prompt**

This option simply refreshes the page and removes any excess entries and leaves only the menu page open.
