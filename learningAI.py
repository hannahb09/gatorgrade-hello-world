import json
"""created an command line interface to read json file and prints json file content"""
def read_json_file_cli(file_path):
    """Reads a JSON file and prints 'read' if successful."""
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python learningAI.py <path_to_json_file>")
    else:
        data = read_json_file_cli(sys.argv[1])
        print(data)

"""run gatorgrade and only show the answer that got "red" """
def extract_x_answers(data):
    """Extracts and prints answers marked with "red" from the provided data."""
    x_answers = []
    for item in data:
        if item.get('answer') == "red":
            x_answers.append(item)
    return x_answers