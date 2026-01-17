info = {
    "name": "Saurav mishra",
    "age": 24,
    "city": "Delhi",
    "profession": "Software Engineer",
    "favorite": "Football"
}

print(info)

info.update({"girlfriend": "Ankita"})

for key, value in info.items():
    print(f"{key}: {value}")
