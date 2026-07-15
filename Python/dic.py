student = {
    "name": "AK",
    "age": 22,
    "city": "Chennai"
}

for key, value in student.items():
    if key == "name":
        print(value)

    if key == "city":
        break

    print(key)