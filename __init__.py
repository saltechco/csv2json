# Function: csv_2_json_file
#
# This function takes in as input a CSV file and converts it to a JSON file. The converted JSON contents are written to a new file
# in the same location with '.json' extension. Encoding for reading from and writing to a file is set to UTF-8.
#
# Args:
#     path: A string representing the absolute path of the CSV file to be converted to JSON.
#
# Returns:
#     None
#
# Raises:
#     Throws any exception raised during file operations directly to the caller.


def csv_2_json_file(path: str) -> None:
	"""
		Convert CSV (Comma Separated Values) Files to JSON (JavaScript Object Notation) File

		Parameters:

		-   path
			The CSV File absolute path
	"""
	path = _split_path(path)
	with open(''.join(path), encoding="utf-8") as csvFile:
		json = csv_2_json(csvFile.read())
	with open(path[0] + ''.join(path[1].split(".")[:-1]) + ".json", 'w', encoding="utf-8") as jsonFile:
		jsonFile.write(json)


# This function, csv_2_json, takes a string formatted as Comma Separated Values (CSV) and converts it into a string formatted in
# JavaScript Object Notation (JSON). Firstly, it splits the CSV data at every newline character ('\n'), assigning the first row as
# 'subjects'. The function then checks if the number of 'subjects' is even. If yes, it converts the subsequent rows into a list of
# lists (of values), initializes a JSON-formatted string and starts filling it with key-value pairs taken from the 'subjects' and the
# rows, respectively. For every key-value pair, it increases the index. If the index is greater than the number of pairs, it adds a
# comma to the JSON string. When all rows have been processed, it closes the JSON string with a '}'. If the number of 'subjects' is
# not even, it raises a ValueError. This function returns a JSON-formatted string.
def csv_2_json(csv: str) -> str:
	"""
		Convert CSV (Comma Separated Values) Files to JSON (JavaScript Object Notation) File

		Parameters:

		-   csv
			The CSV String
	"""
	csv = csv.split("\n")
	subjects = csv[0].split(",")
	if len(subjects) % 2 == 0:
		rows = list(map(lambda e: e.split(","), csv[1:]))
		json = "[" if len(rows) > 1 else ""
		i = 0
		for row in rows:
			j = 0
			json += "{"
			for subj, obj in zip(subjects, row):
				json += f"\"{subj}\":\"{obj}\"{',' if j < len(row) - 1 else ''}"
				j += 1
			json += "}" + (',' if i < len(rows) - 1 else '')
			i += 1
		json += "]" if len(rows) > 1 else ""
	else:
		raise ValueError("The count of columns must be even!")
	return json


def _split_path(file_path: str):
	file_path = file_path[1:-1] if file_path.count("\"") else file_path
	_WINDOWS_FILE_SEP = "\\"
	_UNIX_FILE_SEP = "/"
	if file_path.count(_WINDOWS_FILE_SEP):
		file_path_part = file_path.split(_WINDOWS_FILE_SEP)
		file_separator = _WINDOWS_FILE_SEP
	else:
		file_path_part = file_path.split(_UNIX_FILE_SEP)
		file_separator = _UNIX_FILE_SEP
	return [''.join(map(lambda path: path + file_separator, file_path_part[:-1])), file_path_part[-1]]
