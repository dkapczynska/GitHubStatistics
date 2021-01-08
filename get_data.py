import requests


def getRepositories(url):
    r = requests.get(url)
    print("Kod stanu:", r.status_code)
    response_dict = r.json()
    print(response_dict.keys())
    print("Całkowita liczba repozytoriów: ", response_dict['total_count'])
    return response_dict


def showKeys(repo_dicts):
    repo_dict_1 = repo_dicts[0]
    print("\nKlucze: ", len(repo_dict_1))
    for key in sorted(repo_dict_1.keys()):
        print(key)


def viewInformation(repo_dicts):
    print("Wybrane informacje o najbardziej popularnych projektach: \n")
    for repo_dict in repo_dicts:
        print("Język: ", repo_dict['language'])
        print("Nazwa projektu: ", repo_dict['name'])
        print("Gwiazdki: ", repo_dict['stargazers_count'])
        print("Repozytorium", repo_dict['html_url'])
        print("Opis: ", repo_dict['description'])
        print("____________________________________________________________________________________________\n")
