import csv
import os


input_file = os.path.join('..', 'CSV_DB', 'sorted_merged_output.csv')
output_file = os.path.join('..', 'stock_data.csv')   # Use raw string literal for the output file path

with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    for row in reader:
        global_checking_flag = False
        global_checking_flag2 = False

        if all(row):
            writer.writerow(row)
        else:
            for value in row[1:]:
                if value == "" and global_checking_flag == False:
                    continue
                elif value == "" and global_checking_flag == True:
                    global_checking_flag2 = True
                else:
                    global_checking_flag = True

            if global_checking_flag == True and global_checking_flag2 == False:
                writer.writerow(row)
