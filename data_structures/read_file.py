import os
file_path = os.path.join(os.path.dirname(__file__), "demo.txt")
file = open(file_path, "a+")
file.seek(0)
file_content = file.read()
print(file_content)
file.write("\n These are the political view of AI")
file.close()
print(file.closed)