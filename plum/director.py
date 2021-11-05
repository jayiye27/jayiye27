from pathlib import Path

path = Path()
print(path.glob('*.py'))

path = Path()
for file in path.glob():
    print(file)