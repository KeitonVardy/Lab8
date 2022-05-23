import requests

def get_poke_info(poke_name): 

    print("Getting Pokemon information...", end='')

    poke_name = poke_name.lower().strip()

    response = requests.get('https://pokeapi.co/api/v2/pokemon/' + str(poke_name))

    if response.status_code == 200:
        print('Success!')
        return response.json()
    else:
        print('Error',response.status_code)
        return