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
        print(f"Episódio: {e['episode']} | Nome: {e['name']} | Data: {e['air_date']}")

def main():
    print("\n=== Explorador do Universo de Rick and Morty ===")
    print("1 - Mostrar personagens")
    print("2 - Mostrar episódios")
    print("3 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        mostrar_personagens()
    elif escolha == "2":
        mostrar_episodios()
    elif escolha == "3":
        print("Saindo... até mais!")
        return
    else:
        print("Opção inválida, tente novamente!")

    main()


main()
