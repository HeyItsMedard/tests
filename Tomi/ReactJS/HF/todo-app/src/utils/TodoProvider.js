export const initialState = []

export const ADD_TODO = 'add_todo'
export const TOGGLE_TODO = 'toggle_todo'
export const DELETE_TODO = 'delete_todo'

const reducer = (state, action) => {
  switch (action.type) {
    case ADD_TODO:
      return [...state, action.payload]
    case TOGGLE_TODO:
      return state.map((todo) =>
        todo.id === action.payload
          ? { ...todo, completed: !todo.completed }
          : todo
      )
    case DELETE_TODO:
      return state.filter((todo) => todo.id !== action.payload)
    default:
      throw new Error('Unknown type')
  }
}

export default reducer