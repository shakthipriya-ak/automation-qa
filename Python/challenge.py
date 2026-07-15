employees = {
    "AK": "QA",
    "John": "Developer",
    "Sara": "Manager"
}
for key,value in employees.items():
    if key == 'John':
        continue
    print(key,'->',value)
