with open('patient_list.txt', 'r') as file:
    for line in file:
        '''.strip() removes extra blank lines in the output'''
        print(line.strip()) 