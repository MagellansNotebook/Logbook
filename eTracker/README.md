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

![InformationPage](https://user-images.githubusercontent.com/51066040/62019448-3a577680-b202-11e9-8edc-49893bc9d1aa.jpg)

**Scan Page**

The Scan Page is where the item check against the database. If the item exists then it will update its date on the current time it was scanned. Also, the item will be displayed under the **Equipment List Box**. However, if the item is not recorded in the database it will not appear in the **Equipment List Box**. The user has to manually add the item into the database.

If the details of the item is incorrect simply double click on it and it will auto-populate the **Edit Item Box**. The user can update any information required. The **Commit Button** will save the changes made into the database.

![ScanPage](https://user-images.githubusercontent.com/51066040/62019465-4e9b7380-b202-11e9-8173-b212435b88cf.jpg)

**Track Page**

The Track Page is used to check the item's history. It keeps 10 recorded events which displays when it was last checked and the updates made to the item. Particularly, the changes made on the **Location** is important because it will tell the user where it was last seen.

The user can search for a particular item either by the following:
* Unique ID
* Description
* Serial Number
* Asset Number

By simply clicking on the **Add Button** or pressing **Enter** will seach for the item from the database. It will display its information in the **Equipment List Box** if it existed.

Double-click on the item to check its history. The details will be displayed on the **Record List Box**.

![TrackPage](https://user-images.githubusercontent.com/51066040/62019485-63780700-b202-11e9-8204-657d33a5e5b6.jpg)

**Upload**

The Upload option in the File menu uploads a spreadsheet with details entered in the format below. This makes it easier to add a large amount of data into the database.

![Spreadsheet](https://user-images.githubusercontent.com/51066040/62019772-b0101200-b203-11e9-8f59-b615b88b7b5b.jpg)

The Upload option can only upload spreadsheet with **.xlsx**.

![Upload](https://user-images.githubusercontent.com/51066040/62019779-bf8f5b00-b203-11e9-9ea9-db4a5219b761.jpg)

**Add Page**

The Add Page adds a new items into the database. The user can add 10 item simultaneously by clicking on the **Add Button**. The items will be displayed on the **Equipment List Box**. Double-clicking on the selected item would remove it from the **Equipment List** if the user made an error. The **Upload Button** will add the items into the database.

![AddPage](https://user-images.githubusercontent.com/51066040/62021224-8c4fca80-b209-11e9-8260-1f2370bf8279.jpg)

**Edit Page**

The Edit Page simply updates any new changes made into an item. The user will search the equipment first by either looking for its **Unique ID**, **Serial Number** or **Asset Number**. If the item exists it will be displayed on the **Equipment List Box**. Double-clicking on the selected item would populate the details under the **Edit Item Box**. From there, the user would be able to change any details and the **Commit Button** will update the item into the database.

![EditPage](https://user-images.githubusercontent.com/51066040/62022079-d2a72880-b20d-11e9-869c-71f58f41519f.jpg)

**Delete Page**

The Delete Page is used to remove any item saved in the database. Like **Edit Page**, the user can search for the item by either searching for its **Unique ID**, **Serial Number** or **Asset Number**. If the item exists it will be displayed on the **Equipment List Box**. By clicking on the **Commit Box**, it will delete all items in the **Equipment List Box**.

![DeletePage](https://user-images.githubusercontent.com/51066040/62023150-f456de80-b212-11e9-8815-49e842fc7105.jpg)

**Search Page**

The Search Page is used to look for a specific item or a group of items in the database. The search query accepts any combination. If the item exists then it will display its details on the equipment list.

The **Save Button** saves all details displayed on the **Equipment List**. It will save it as an Excel file.

![SearchPage](https://user-images.githubusercontent.com/51066040/62023690-616b7380-b215-11e9-8d1a-a909a9bb7274.jpg)
