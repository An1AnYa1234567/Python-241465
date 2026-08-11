# WAP to demonstrate  automated CSV file inspector and data exporter.
import csv

print("---CSV FILE INSPECTOR AND DATA EXPORTER---")

filename = input("Enter CSV file name: ")

try:
    # Open CSV file
    file = open(filename, "r", newline="")
    reader = csv.reader(file)

    # Read all rows
    rows = list(reader)
    file.close()

    if len(rows) == 0:
        print("The CSV file is empty.")

    else:
        # First row contains column names
        headers = rows[0]
        data = rows[1:]

        # Display basic information
        print("\n----- FILE INFORMATION -----")
        print("File name:", filename)
        print("Number of columns:", len(headers))
        print("Number of data rows:", len(data))

        print("\nColumns:")
        for column in headers:
            print("-", column)

        # Display first 5 records
        print("\n----- FIRST 5 RECORDS -----")

        limit = 5
        if len(data) < 5:
            limit = len(data)

        for i in range(limit):
            print(data[i])

        # Search/filter data
        search = input("\nEnter text to search in the file: ")

        filtered_rows = []

        for row in data:
            for value in row:
                if search.lower() in value.lower():
                    filtered_rows.append(row)
                    break

        print("\n----- FILTERED DATA -----")

        if len(filtered_rows) == 0:
            print("No matching records found.")

        else:
            for row in filtered_rows:
                print(row)

            # Export filtered data
            output_file = input(
                "\nEnter output file name : "
            )

            output = open(output_file, "w", newline="")
            writer = csv.writer(output)

            # Write column names
            writer.writerow(headers)

            # Write filtered records
            for row in filtered_rows:
                writer.writerow(row)

            output.close()

            print("\nFiltered data exported successfully!")
            print("Output file:", output_file)

except FileNotFoundError:
    print("Error: CSV file not found.")

except Exception as e:
    print("Error:", e)