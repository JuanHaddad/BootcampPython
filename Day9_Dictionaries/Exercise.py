
country = input() # Add country name
visits = int(input())
list_of_cities = eval(input())

travel_log = [
    {
        "country":"France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]

def add_new_country(country, num_visits, cities):
    # criando um dictionary do 0 e adicionando seus respectivos keys/values
    new_country = {}
    new_country['country'] = country
    new_country['visits'] = num_visits
    new_country['cities'] = cities

    # como o travel_log é uma LISTA, damos um .append com o nosso new_country
    travel_log.append(new_country)




# chamamos a função que adiciona um novo country na travel_log
add_new_country(country, visits, list_of_cities)

# printamos o novo country a partir das manipulações do nosso travel_log através de suas keys e indices da lista
print(f"i've been to {travel_log[2]['country']} {travel_log[2]['visits']}")
print(f"My favourite city was {travel_log[2]['cities'][0]}")