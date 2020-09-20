import csv

#global variables
surface_depth = 0
#==================================
#fill in global variables here
#==================================
ratio = 0

def main():
    file_name = "jimmy.csv"
    output_csv = "output.csv"
    with open(file_name, "r") as csv_file, open(output_csv, "w") as answers_file:
        num_of_globals = 2  #set this to 5 for real data
        data_start_row = 2  #set this to 14 for real data
        parse(csv_file, answers_file, num_of_globals, data_start_row)
    
def parse(csv_file, answers_file, num_of_globals, data_start_row):
    csv_reader = csv.reader(csv_file)       #csv function to read the csv
    csv_writer = csv.writer(answers_file)   #csv functino to write to the output csv
    matrix = list(csv_reader)               #a matrix (a list of lists) representing your csv file.
    global_vars = []                        #a list to hold all of your global variables
    global_var_column = 1                   #the value is assumed to be in column B/column 2
    for row in range(1, num_of_globals + 1):
        global_vars.append(matrix[row][global_var_column])
    #==================================
    #manually assign global variables. ensure to use the word 'global'
    global surface_depth
    surface_depth = global_vars[0]
    global ratio
    ratio = global_vars[num_of_globals - 1]
    #==================================
    #parse the matrix and perform the expression
    for row in range(data_start_row, len(matrix)):  #starting at data_start_row to the last row of the csv file
        row_as_a_list = matrix[row]                 #a list containing all of the comma-separated items as strings
        values = []                                 #a list of strings containing just numbers and booleans (but as strings)
        before_E = True                             #a flag to help us know the boundary between values and expression(s)
        output = 0                                  #the output after your expression is evaluated
        for column in range(len(row_as_a_list)):
            value = row_as_a_list[column]
            if before_E == True and value != "E":
                values.append(value)
            elif value == "E":
                before_E = False
            else:
                output = evaluate(values)           #evaluate the expression on the value of the given row
        values.append(output)                       #tack on the answer onto the row
        csv_writer.writerow(values)
        print("Row", row, ": ", values)

def evaluate(values):
    #manually assigned our variables from values, which is a list of strings
    """values: | num1 | bool1 | num2 | num3 | bool2 | bool3 |"""
    #convert the values into either floats or booleans
    num1 = float(values[0])
    bool1 = bool(values[1])
    num2 = float(values[2])
    num3 = float(values[3])
    bool2 = bool(values[4])
    bool3 = bool(values[5])
    output = 0                                          #variable signifying the output of the expression
    #manually hardcode the expression(s) to be evaluated
    condition1 = (num3 + num1) / num2 == surface_depth
    if condition1 and (bool1 == True or bool3 == True):
        output = (num3 + num1) / num1
    elif (bool1 == True or bool3 == True):
        output = (num1 + num2) * num1
    elif bool2 == False:
        output = num2 - num1
    
    return output


if __name__=="__main__":
    main()