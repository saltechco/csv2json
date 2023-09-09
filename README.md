# Python CSV to JSON Converter
###### based on unicode UTF-8

You can export converted json string to a file when using a csv file

Instructions:

- For import to your project

    `import csv2json as converter`
- For convert csv to json and export to file

    `converter.csv_2_json_file("YOUR_CSV_FILE_PATH")`
- For convert csv to json as string:

    ```
    csv = "YOUR_CSV_STRING"
    json = converter.csv_2_json(csv)
    print(json) # Converted JSON String
    ```
  
Minimum Python Version Requirement is **3.7.0**