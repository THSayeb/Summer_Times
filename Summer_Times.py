temperature = float(input("Enter the temperature in degrees Celsius: "))

if temperature < 10:
    print("It's cold outside. Wear a warm coat, scarf, and gloves.")
elif 10 <= temperature < 20:
    print("It's cool outside. A light jacket or sweater would be good.")
elif 20 <= temperature < 30:
    print("The weather is warm. Wear something comfortable, like a T-shirt and jeans.")
else:
    print("It's hot outside. Wear light, breathable clothing like shorts and a tank top.")
