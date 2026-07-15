response = {
    "status": "Success",
    "message": "Login Successful",
    "user": "AK"
}
print(response['status'])
print(response['user'])
print(response['message'])

for key, value in response.items():
    print(key, ":", value)