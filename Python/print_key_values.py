def details(**info):
    for key, value in info.items():
        print(key, value)
details(name='ak', age=22, role='qa')