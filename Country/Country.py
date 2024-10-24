#Saquorya Arnold
#CIS261
#Country

def menu_heading():
    print(" Countries Management" )
    print(" 1. List all countries ")
    print(" 2. Add a country ")
    print(" 3. Delete a country ")
    print(" 4. Exit ")
    
def get_countries():
    countries = {
        'US' : 'United States',
        'BB' : 'Barbados',
        'BR' : 'Brazil',
        'BS' : 'Bahamas'
    }
    return countries

def show_countries(countries):
    print("Current country keys: ")
    for key in countries:
        print(key)
    while True:
        abbr = input(" Enter a country key to view: ")
        if abbr in countries:
            print(f" The country for {abbr} is {countries[abbr]}.")
            break
        else:
            print("Invalid Key! Try again!")
            
def add(countries):
    abbr = input("What key do you want to add: ").upper()
    if abbr in countries:
        print(f" The key '{abbr}' already exists with the name '{countries[abbr]}'.")
    else:
        name = input(" Please enter the country name: ")
        countries[abbr] = name
        print(f" Country '{name}' successfully added with key '{abbr}'.")
        
def delete(countries):
    abbr = input(" What key do you want to delete? ").upper()
    if abbr in countries:
        del countries[abbr]
        print(f"Country '{abbr}' has been successfully deleted. ")
    else:
        print("Invalid Key! Try again!")
        
def main():
    countries_dictionary = get_countries()
    while True:
        menu_heading()
        choice = input("Which option do you want? (1-4): ")
        if choice == '1':
            show_countries(countries_dictionary)
        elif choice == '2': 
            add(countries_dictionary)
        elif choice == '3':
            delete(countries_dictionary)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid! Try again!")
            
if __name__ == "__main__":
    main()

