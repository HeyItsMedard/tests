import requests

s = requests.Session()

def register(username, password):
  register = requests.post('http://localhost:4000/users', data={ 'username': username, 'password': password })
  return register

def login(username, password):
  login = requests.post('http://localhost:4000/login', data={ 'username': username, 'password': password })
  token = login.text
  s.headers.update({ 'Authorization': f'Bearer {token}'})
  return login

def get_todos(order='asc'):
  return s.get('http://localhost:4000/todos', params={'order': order })

def create_todo(text):
  return s.post('http://localhost:4000/todos', json={ 'text': text })

def get_todo_by_id(id):
  return s.get(f'http://localhost:4000/todos/{id}')

def update_todo_by_id(id, text):
  return s.patch(f'http://localhost:4000/todos/{id}', json={'text': text})

def delete_todo_by_id(id):
  return s.delete(f'http://localhost:4000/todos/{id}')

def complete_todo(id):
  return s.put(f'http://localhost:4000/todos/{id}')

# login('test', 'password')

def menu():
  print('1. Create todo')
  print('2. Get todos')
  print('3. Get todo by id')
  print('4. Update todo')
  print('5. Complete todo')
  print('6. Delete todo')
  print('7. Create user')
  print('8. Login user')
  print('0. Exit')

  choice = input('Choice: ')
  if choice == '1':
    text = input('Text? ')
    response = create_todo(text)
    print(response.json())
  elif choice == "2":
    order = input('Order? ')
    response = get_todos(order)
    print(response.json())
  elif choice == "3":
    id = input('ID? ')
    response = get_todo_by_id(id)
    print(response.json())
  elif choice == "4":
    id = input('ID? ')
    text = input('Text? ')
    response = update_todo_by_id(id, text)
    print(response.json())
  elif choice == "5":
    id = input('ID? ')
    response = complete_todo(id)
    print(response.json())
  elif choice == "6":
    id = input('ID? ')
    response = delete_todo_by_id(id)
    print(response.text)
  elif choice == '7':
    username = input('Username? ')
    password = input('Password? ')
    response = register(username, password)
    print(response.json())
  elif choice == "8":
    username = input('Username? ')
    password = input('Password? ')
    response = login(username, password)
    print(response.text)
  elif choice == '0':
    exit()
  else:
    print('Invalid command')

  menu()


if __name__ == '__main__':
  menu()
