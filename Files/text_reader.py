from pathlib import Path

try:
    path1 = Path('dogs.txt')
    path2 = Path('dogs.txt')
    content = path1.read_text()
    content1 = path2.read_text()
    print(content)
except FileNotFoundError:
    print("The file you are looking for is not found.")