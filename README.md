Ingesting CSV Files in Python
Introduction
Below are 3 sets of questions related to the 3 file exchange formats discussed in recent course work. You are to complete the questions using what you have learned from the readings and by completing the lab documents. Do not attempt to solve these problems until you have completed all related lab work.
CSV File Format
CSV Question 1
The freshman_kgs.csv file contains data detailing the weight (in kilos) and BMI (body mass index) measures for university freshman. Each row contains the subjects weight and BMI at the beginning and end of the school year.
NOTE: review the input file prior to beginning your script. You are NOT to edit the input file; rather, your script needs to configure your CSV reader to work with the data as given. You may use either reader() or DictReader() in your solution.
Author a script named freshman_kgs.py to parse the freshman_kgs.csv file and to answer the questions below.
1. Does the sample contain more men or women?
2. Which gender has the largest beginning BMI?
3. How many observations in the sample, regardless of gender, have a beginning BMI equal to the overall largest BMI?
4. Over the course of the school year, which gender experienced the largest average change in weight?
CSV Question 2
We said in class that although there is a published standard for the CSV file format it is the most likely file format to deviate from the standard.
Examine the zillow_with_metadata.py and the corresponding zillow_with_metadata.csv files.
Write a description of what script is doing. That is, I’m asking you to reverse engineer the script and explain (in writing) its purpose. This will require that you explore (and understand) the documentation for any functions used by the script. For example, you will need to understand the role of the tell() and seek() functions in this script.
JSON File Format
JSON Question 1
The movies_db.json file contains movie related data including title, year, director and actors.
Review the input file. You’ll note that the JSON data contains several nested objects. For example, director, is an object that contains the name and birth year of the director. actors is an array of actor objects that contain an actor’s name, birth year and role.
Page – 2
After deserialization of the JSON data, you can access nested attributes in many ways; however, the following approach is very common.
# Assume the JSON data has been deserialized into a Python list named movies.
# Access director last name and actor’s role.
for movie in movies:
director_dict = movie['director']
dir_last_nm = director_dict['last_name']
print( dir_last_nm )
actors_list = movie['actors']
for actor in actors_list:
print(actor['role'])
Author a script named movies_db.py to deserialize the movies_db.json file and to answer the questions below.
1. What is the total number of movies included the sample data?
2. Which movie summary contains the most characters
3. How many actors were born after 1970 and what were their last names?
4. Which movie had the most actors
5. Which actors played more than one role in a single movie? Note: you may assume that an actor’s last name is unique. That is, there are no actors that have the same last name.
XML File Format
XML Question 1
The CustomersOrders.xml file contains customer order related data. The top-level Root element contains two related child elements – Customers and Orders. Customers are related to Orders via the CustomerID element.
Review the input file. You’ll note that the XML data contains several nested nodes. For example, FullAddress, is a complex element that contains address related data for each customer. Similarly, ShipInfo is a complex element that contains shipping related information.
After parsing the XML data, you can access nested element in many ways; however, the following approach is very common.
# Assume the JSON data has been deserialized into a Python list named movies.
# Access director last name and actor’s role.
<Root>
<Orders>
<Order>
<CustomerID>GREAL</CustomerID>
<ShipInfo ShippedDate="1997-05-09T00:00:00">
<ShipPostalCode>97403</ShipPostalCode>
Page – 3
</ShipInfo>
</Order>
</Orders>
</Root>
# assume we have the above XML data that has been parsed by ElementTree and whose root
# element is available in the Python variable root.
# To Find customer ids for Orders I find the list of Order elements
# With in an Order, find the CustomerID element.
# Once found the text attribute reveals the text value stored between
# the <CustomerID> and </CustomerID> tags.
#
for order in root.findall(r"./Orders/Order"):
# find is used when I expect a single element by this name
# to be located "under" the Order element. This is enforced by the schema.
custId = order.find('CustomerID')
print(custId.text)
# Likewise, there exists a single ShipPostaCode element
zip = order.find(r"./ShipInfo/ShipPostalCode")
print(f'\t{zip.text}')
# ShipDate is an attribute (not an element) in the ShipInfo element
sinfo = order.find(r"./ShipInfo")
# any attributes are returned as a dictionary
ship_info_attributes = sinfo.attrib
# Not all attributes are required
if 'ShippedDate' in ship_info_attributes:
ship_date = ship_info_attributes['ShippedDate']
print(f'\t{ship_date}')
Using the xml.etree.ElementTree module, author a script named customer_orders.py to parse the CustomersOrders.xml file and to answer the questions below.
1. Validate CustomersOrders.xml against the CustomersOrders.xsd schema.
2. How many customers appear in the data?
3. Which customers’ PostalCode occurs most frequently?
4. Which customer has the most orders
Deliverables
Once you have completed the tasks above, create upload all supporting Python scripts (there should be 3) along with a Word document that includes any required response text to the Blackboard assignment item. You may upload you solutions as many times as necessary. Your final submission will be graded.
