data={
    'a':'10',
    'b':'20',
    'c':'30'
}
for key, value in data.items():
    print(key)
    if value==20:
        continue
    print(value)