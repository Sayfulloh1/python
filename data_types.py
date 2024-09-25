none_value = None
print(none_value)

int_value = 1
print(type(int_value))

float_value = 12.32
print(type(float_value))

complex_value = 2 + 5j
print(type(complex_value))

boolean_value = True
print(type(boolean_value))

# casting
int_value = int(float_value)
print(int_value)

float_value = float(int_value)
print(float_value)

complex_value = complex(int_value, float_value)
print(complex_value)

string_value = "ibroximjon"
print(type(string_value))
string_value = str(int_value)
print(string_value)

range(0, 10)
print(list(range(10)))
print(list(range(2, 12, 3)))
print(type(range(100)))
print(list(range(0, 100, 5)))

dictionary = {"Ibroximjon":"Redmi", "Navfalbek":"One Plus", "Azizbek":"Samsung"}
print(dictionary.keys())
print(dictionary.values())
print(type(dictionary.keys()))
print(type(dictionary.values()))
