# eTracker

eTracker is a simple python script used for accounting and tracking stocks. 

The eTracker has 3 main menu. 

**File** contains the following pages:
* Information
* Scan
* Track
* Upload
* Exit

**Edit**
* Add
* Edit
* Delete

**View**
* Search Item

**Information Page** 

The Information page displays the overall number of items checked within the last 30 days. It also shows the total number of Serial/Quantity track equipment and the latest date it was checked. 

By clicking on the **Refresh Button** will updated the **Statistics Box** with the latest information about the current stocks saved in the database.

The **NSN Box** is a quick search tool used in looking for NSN for a particular item.

The **Display Button** will show all of the current NSN saved in the database. By double-clicking on the highlighted item copies the NSN and paste it on the **Copy and Paste Value in the Search Page - "NSN"**. The box is used for ease of searching an item based on its NSN. 

![InformationPage](https://user-images.githubusercontent.com/51066040/62015403-9912f500-b1ee-11e9-9385-5213bf94f368.jpg)

**Scan Page**

The Scan Page is where the item check against the database. If the item exists then it will update its date on the current time it was scanned. Also, the item will be displayed under the **Equipment List Box**. However, if the item is not recorded in the database it will not appear in the **Equipment List Box**. The user has to manually add the item into the database.

If the details of the item is incorrect simply double click on it and it will auto-populate the **Edit Item Box**. The user can update any information required. The **Commit Button** will save the changes made into the database.

![ScanPage](https://user-images.githubusercontent.com/51066040/62017680-eb5a1300-b1fa-11e9-9d54-0f883656f166.jpg)

**Track Page**

The Track Page is used to check the item's history. It keeps 10 recorded events which displays when it was last checked and the updates made to the item. Particularly, the changes made on the **Location** is important because it will tell the user where it was last seen.

The user can search of a particular item either by the following:
* Unique ID
* Description
* Serial Number
* Asset Number

By simply clicking on the **Add Button** or pressing **Enter** will seach for the item from the database. It will display its information in the **Equipment List Box** if it existed.

Double-click on the item to check its history. The details will be displayed on the **Record List Box**.
