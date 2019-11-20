# This import statement makes the csv module and it's features, available for zillow_with_metadata.py
import csv

# the with sets the context for the file to be open, in this case it's in read mode.
with open('zillow_with_metadata.csv', mode='r') as csv_file:

# readline function reads a single line from the file and assigns it to the variable "line". its used on the file object.
    line = csv_file.readline()
    while line != '':
        '''Below condition checks if the line begins with a '#', saves the current line position from the file,
        in the variable current_line_position by using the tell function and it goes on to
        the tell() returns an integer giving the file object’s current position in the file
        represented as number of bytes from the beginning of the file when in binary mode and an opaque number when in text mode.
        It continues to read subsequent line until the line doesn't start with '#' '''
        if line.startswith('#'):
            # the current line position is updated with the position of the latest line read.
            current_line_position = csv_file.tell()
            line = csv_file.readline()
        else:
            '''once the readline() reads the header "Index,LivingSpace,Beds,Baths,Zip,Year,ListPrice", the control moves here
            and positions the file object to the next line after the header, by using calling seeking function on the file object.
            and breaks the while loop.'''
            csv_file.seek( current_line_position )
            break

    '''the DictReader function then starts reading the file from the next line position
    and saves an ordered dict it into csv_reader object variable.
    the quotechar argument takes in the '"'(quote) to quote the fields containing special characters.
    '"' quote also happens to be the default value.'''
    csv_reader = csv.DictReader(csv_file, quotechar='"')

    '''The join function takes a iterable argument in this case a dictionary of field names or header from the csv file
    and separate each element with a comma'''
    print(','.join(csv_reader.fieldnames))

    '''Below for loop will iterate each item from the dictionary and pull it's values alone and forms a row string separated by comma.
    and each line is printed to the console until it reaches the last line in the file object.'''
    for row in csv_reader:
        rowStr = ','.join(row.values())
        print(rowStr)
