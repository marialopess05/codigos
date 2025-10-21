import requests 


def mostrar_personagens():
    url = "https://rickandmortyapi.com/graphql"
    query = """
    {
      characters(page: 1) {
        results {
          name
          status
          species
        }
      }
    }
    """
    response = requests.post(url, json={"query": query})
    data = response.json()
    personagens = data["data"]["characters"]["results"]

    print("\n=== Personagens de Rick and Morty ===\n")
    for p in personagens:
        print(f"Nome: {p['name']} | Status: {p['status']} | Espécie: {p['species']}")


def mostrar_episodios():
    url = "https://rickandmortyapi.com/graphql"
    query = """
    {
      episodes(page: 1) {
        results {
          name
          episode
          air_date
        }
      }
    }
    """
    response = requests.post(url, json={"query": query})
    data = response.json()
    episodios = data["data"]["episodes"]["results"]

    print("\n=== Episódios de Rick and Morty ===\n")
    for e in episodios:
        print(f"{e['episode']} | {e['name']} | Data: {e['air_date']}")


def mostrar_planetas():
    url = "https://rickandmortyapi.com/graphql"
    query = """
    {
      locations(page: 1) {
        results {
          name
          type
          dimension
        }
      }
    }
    """
    response = requests.post(url, json={"query": query})
    data = response.json()
    planetas = data["data"]["locations"]["results"]

    print("\n=== Planetas e Localizações ===\n")
    for p in planetas:
        print(f"Nome: {p['name']} | Tipo: {p['type']} | Dimensão: {p['dimension']}")


def mostrar_resumo():
    url = "https://rickandmortyapi.com/graphql"
    query = """
    {
      characters { info { count } }
      episodes { info { count } }
      locations { info { count } }
    }
    """
    response = requests.post(url, json={"query": query})
    data = response.json()
    info = data["data"]

    total_personagens = info["characters"]["info"]["count"]
    total_episodios = info["episodes"]["info"]["count"]
    total_planetas = info["locations"]["info"]["count"]

    print("\n=== RESUMO GERAL ===\n")
    print(f"Personagens totais: {total_personagens}")
    print(f"Episódios totais:   {total_episodios}")
    print(f"Planetas totais:    {total_planetas}")


def main():
    print("\n=== Explorador do Universo de Rick and Morty ===")
    print("1 - Mostrar personagens")
    print("2 - Mostrar episódios")
    print("3 - Mostrar planetas/localizações")
    print("4 - Mostrar resumo geral")
    print("5 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        mostrar_personagens()
    elif escolha == "2":
        mostrar_episodios()
    elif escolha == "3":
        mostrar_planetas()
    elif escolha == "4":
        mostrar_resumo()
    elif escolha == "5":
        print("Saindo... até mais!")
        return
    else:
        print("Opção inválida, tente novamente!")

    main()  


main()
