results = {
    "Login": "Pass",
    "Signup": "Pass",
    "Payment": "Fail",
    "Search": "Pass"
}
for process, step in results.items():
    if step=="Fail":
        print('Skipping', process)
    else:
        print('Executing',process)