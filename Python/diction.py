employees={
    'ak':'qa',
    'john':'developer',
    'sara':'manager',
    'david':'tester'
}
for name, role in employees.items():
    if role == 'developer':
        continue
    print(name)
    if role == 'manager':
        break
    print(role)