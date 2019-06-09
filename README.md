# Logbook
Basic Logbook program using CLI.

Open the program using python 3.

![main_menu](https://user-images.githubusercontent.com/51066040/59157964-d6181080-8af6-11e9-8df4-57a64ae2cfc6.png)

**Add Entry**

Press **1** to add a new entry.

![add_entry](https://user-images.githubusercontent.com/51066040/59158012-5e96b100-8af7-11e9-8175-6ae991f1ae60.png)

Press Enter to save the new message. The next option will asked you whether you wish to use **Open**, **Close**, or **Info**.

**Open** messages are incomplete task.

**Close** messages are completed task.

**Info** messages are general facts or notices only.

![add_entry_save](https://user-images.githubusercontent.com/51066040/59158064-0b712e00-8af8-11e9-938d-b788ff843fc6.png)

Once the message is saved the program will terminate back to the main menu. If it was saved correctly then a **System** comment will appear on top of the logo. The **System** comment displays the date time group the message was saved.

![add_entry_save_complete](https://user-images.githubusercontent.com/51066040/59158146-67888200-8af9-11e9-89d5-5c46e6971beb.png)

**Edit Entry**

Press **2** to edit an entry. Insert the message serial number of the log you wish to update and press enter.

The edit entry only updates the status of the message.

![edit_menu](https://user-images.githubusercontent.com/51066040/59158181-0e6d1e00-8afa-11e9-9d3b-c22773fc6bd7.png)

Once you press enter the program will display the message you wish to edit.

![edit_entry](https://user-images.githubusercontent.com/51066040/59158283-30b36b80-8afb-11e9-8a49-06f816a5e012.png)

Select the new status of the message and press enter.

![edit_entry_change](https://user-images.githubusercontent.com/51066040/59158337-2e054600-8afc-11e9-8bf7-c8b9f52b2972.png)

Once complete and successful a **System** message will appear above the logo.

![edit_entry_complete](https://user-images.githubusercontent.com/51066040/59158377-d1eef180-8afc-11e9-8d3d-34af1244af56.png)

**View Entry**

Press **3** to view all entries. It will display 5 entries at a time.

![view_entry](https://user-images.githubusercontent.com/51066040/59158431-56da0b00-8afd-11e9-9e0b-8408acf4451f.png)

**Search Entry**

Press **4** to search a specific entry. Search entry by **Serial Number**, **DateTimeGroup**, **Status**, **Content**

![search_entry](https://user-images.githubusercontent.com/51066040/59158634-70c91d00-8b00-11e9-8c25-d1feaf4a4cd5.png)

**Serial Number** is straightforward to use. Simply enter the message serail number and press enter.

All fields on **Date Time Group** must be filled. Also, **Enter the message Hour:Min:** must have 4 digit numbers. Otherwise, a value error will occur. The **Date Time Group** displays all message logs greater than the entered date.

![searcg_dtg](https://user-images.githubusercontent.com/51066040/59158635-73c40d80-8b00-11e9-824c-0cbf2840986f.png)

**Status** and **Content** performs a similar function. For **Status**, it will display all message logs against the status entered. With **Content**, it will display all message logs that contains keywords specific to the entered value.

**Delete Entry**

Press **5** to delete a single entry. Similar to **Edit Entry** select the serial number of the message you want to delete.

![delete_entry](https://user-images.githubusercontent.com/51066040/59158727-f6010180-8b01-11e9-9a81-7c7a77f423d4.png)

The program will prompt you whether you wish to continue or not. If you choose to continue the message will be deleted. The program will go back to the main menu with a **System** message. The **System** message will state the deletion of message was successful. 

![delete_entry_value](https://user-images.githubusercontent.com/51066040/59158728-f8635b80-8b01-11e9-908d-b07bb0ba6bca.png)

However, if you do not wish to continue. The program will terminate the delete function and will revert back to the main menu. Also, a **System** message will appear above the log stating no messages was deleted.

**Save File**

Press **6** to create a text file for the logbook database.

![save_to_text](https://user-images.githubusercontent.com/51066040/59158757-71fb4980-8b02-11e9-875a-06371b125ea0.png)

The text file name is saved as a date time group. The file will be  at the same location as logbook.py. A **System** message will appear above the logo stating the file name of the log messages.

**Z All**

Press **9** will delete all log entry.





