"""
Implementáld az alábbi függvényeket, melyek személyek ismeretségi hálózatával dolgoznak.
Készíthetsz további segédfüggvényeket is.
"""


friend_network: dict[str, list[str]] = {}
"""A kulcsok a személyek nevei, az értékek pedig a személyek barátlistái.
A barátságok kétirányúak, azaz ha A-nak barátja B, akkor B-nek is barátja A.
"""


def add_friendship(name1: str, name2: str) -> None:
    """Hozzáadja a barátságot a hálózathoz.

    Ha a barátság már létezik, akkor nem csinál semmit.
    Senki sem lehet saját maga barátja, így ha name1 == name2, akkor nem csinál semmit.
    A barátságok kétirányúak, azaz ha A-nak barátja B, akkor B-nek is barátja A.

    >>> friend_network.clear()
    >>> add_friendship("Adam", "Bob")
    >>> add_friendship("Adam", "Cheryl")
    >>> friend_network == {"Adam": ["Bob", "Cheryl"], "Bob": ["Adam"], "Cheryl": ["Adam"]}
    True
    """
    if name2 == ' ':
        if name1 not in friend_network:
            friend_network[name1] = []
            return
        
    if name1 == ' ':
        if name2 not in friend_network:
            friend_network[name2] = []
            return
    if name1 == name2:
        return
    if name1 not in friend_network:
        friend_network[name1] = []
    
    if name2 not in friend_network:
        friend_network[name2] = []
    
    if name2 in friend_network[name1] or name1==name2:
        return
    
    friend_network[name1].append(name2)
    friend_network[name2].append(name1)

friend_network.clear()
add_friendship("Adam", "Bob")
add_friendship("Adam", "Cheryl")
add_friendship("Judy", " ")
add_friendship(" ", "Bruda")
print(friend_network)


def are_friends(name1: str, name2: str) -> bool:
    """Megadja, hogy két személy barát-e.

    >>> friend_network.clear()
    >>> add_friendship("Adam", "Bob")
    >>> add_friendship("Adam", "Cheryl")
    >>> are_friends("Adam", "Bob")
    True
    >>> are_friends("Cheryl", "Adam")
    True
    >>> are_friends("Bob", "Cheryl")
    False
    """
    if name1 in friend_network and name2 in friend_network[name1]:
        return True
    return False


def common_friends(name1: str, name2: str) -> list[str]:
    """Megadja két személy közös barátait.

    >>> friend_network.clear()
    >>> add_friendship("Adam", "Bob")
    >>> add_friendship("Adam", "Cheryl")
    >>> common_friends("Adam", "Bob")
    []
    >>> common_friends("Cheryl", "Bob")
    ['Adam']
    >>> common_friends("George", "Victoria")
    []
    """
    known_friend = []
    if name1 in friend_network and name2 in friend_network:
        for friend in friend_network[name1]:
            print(friend)
            if friend in friend_network[name2]:
                known_friend.append(friend)
    else:
        return []
    return known_friend
# common_friends("Cheryl", "Bob")
def most_popular() -> str:
    """Megadja a legnépszerűbb személyt.

    Feltételezi, hogy a hálózatban legalább egy baráti kapcsolat van.
    Egyezőség esetén bármelyik legnépszerűbb személyt adja vissza.

    >>> friend_network.clear()
    >>> add_friendship("Adam", "Bob")
    >>> add_friendship("David", "Adam")
    >>> add_friendship("Bob", "Cheryl")
    >>> most_popular()
    'Adam'
    """
    friend_counts = {}
    
    for person, friends in friend_network.items():
        for friend in friends:
            friend_counts[friend] = friend_counts.get(friend, 0) + 1
        friend_counts[person] = friend_counts.get(person, 0)
    
    max_count = max(friend_counts.values())
    most_popular_person = None
    for person, count in friend_counts.items():
        if count == max_count:
            most_popular_person = person
            break
    
    return most_popular_person
print(most_popular())

import json
def export_network(filename: str) -> None:
    """Kiírja a hálózatot a megadott JSON fájlba.

    Ha a fájl már létezik, akkor felülírja.
    A helytakarékosság érdekében a fájl minden baráti kapcsolatot csak az egyik fél oldaláról tárol.
    """
    json_dict = {}
    for person, friends in friend_network.items():
        json_dict[person] = list(set(friends) - set(json_dict.keys())) 
    with open(filename, 'w') as f:
        json.dump(json_dict, f)

export_network("hf2_social_network.json")
def import_network(filename: str) -> None:
    """Beolvassa a hálózatot a megadott JSON fájlból.

    Az aktuális hálózatot felülírja.
    A fájl minden baráti kapcsolatot csak az egyik fél oldaláról tárol.

    >>> friend_network.clear()
    >>> import_network("hf2_social_network.json")
    >>> are_friends("Bob", "Frank")
    True
    >>> are_friends("Frank", "Bob")
    True
    """
    with open(filename, 'r') as f:
        data = json.load(f)
    friend_network.clear()

    for name, friends in data.items():
        for friend in friends:
            add_friendship(name, friend)