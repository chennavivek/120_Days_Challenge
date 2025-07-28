# Temperature Convert

def convert_temperature(temp,unit):
    """This function converts temperature between Celsius and Fahrenheit"""
    if unit == 'C':
        return temp * 9/5 + 32 ## C to F
    elif unit == 'F':
        return (temp-32)*5/9 ## F to C
    else:
        return None
print(convert_temperature(25,"C"))
print(convert_temperature(75,"F"))