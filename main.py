from pathlib import Path
import json

# data = {'name': "Rabby",
#         'age' : 24,
#         'Profession': "Student"
#         }
# j_file = Path('main.json')
# content = json.dumps(data) #converted dictonary into json format
# j_file.write_text(content)


j_file = Path('main.json')
content = j_file.read_text()
python_style = json.loads(content)

print(python_style)











