import xmlschema
import xml.etree.ElementTree as ET
#import pprint
from collections import Counter
# Please use pip install prettytable command to install this package.
from prettytable import PrettyTable

# Variables to hold xml file name and the schema file name.
xml, xsd = 'CustomersOrders.xml', 'CustomersOrders.xsd'

# Assignment question list.
question_list = [
"1. Validate CustomersOrders.xml against the CustomersOrders.xsd schema?",
"2. How many customers appear in the data?",
"3. Which customers’ PostalCode occurs most frequently?",
"4. Which customer has the most orders"
]

answer_list = []

# Function to validate the schema of the xml against the xsd.
def validate_xml_schema(xml, xsd):
    schema = xmlschema.XMLSchema(xsd)

    if not schema.is_valid(xml):
        raise RuntimeError(f"{xml} doesn't comply with {xsd} schema")
    else:
        answer_list.append(f" - The {xml} structure comply to {xsd} schema")

# Function that returns answers to all questions in the assignment.
def assignment_tasks(xml, xsd):
    validate_xml_schema(xml, xsd)
    tree = ET.parse(xml)
    root = tree.getroot()

    # Solution to count number of customers in the xml.
    count_cust = []
    for customer in root.findall(r"./Customers/Customer"):
        count_cust.append(customer.get('CustomerID'))

    answer_list.append(f" - There are {len(count_cust)} customers in the sample xml file.")

    count_zip = []
    cust_name = {}
    cust_zip = {}

    # Pull the required information to solve questions 2 to 4.
    for order in root.findall(r"./Orders/Order"):
        custid = order.find(r"./CustomerID")
        postal = order.find(r"./ShipInfo/ShipPostalCode")
        shipname = order.find(r"./ShipInfo/ShipName")
        count_zip.append([custid.text, postal.text])
        cust_zip.update({custid.text: postal.text})
        cust_name.update({custid.text: shipname.text})
        #cust_name_zip.update({custid.text: [shipname.text, postal.text]})

    # Identify the most common postal code.
    most_postal = Counter(x for postal in count_zip for x in postal).most_common(1)

    answer_list.append(f" - The customer {cust_name[most_postal[0][0]]} has {most_postal[0][1]} "
                       f"occurrence of the postal code {cust_zip[most_postal[0][0]]} in orders")

    # Show which customer has the most number of orders.
    answer_list.append(f" - The customer {cust_name[most_postal[0][0]]} "
                       f"has {most_postal[0][1]} orders, the most in the sample data.")

    #pprint.pprint(answer_list)

    # Below piece of code helps pretty print the Questions and Answers in a tabular format using Pretty Table.
    result_table = PrettyTable(['Assignment Questions', 'Answers'])
    for x in range(len(question_list)):
        result_table.add_row([question_list[x], answer_list[x]])
        result_table.align = "l"

    print(result_table)

# Call the function to execute the program.
assignment_tasks(xml, xsd)

