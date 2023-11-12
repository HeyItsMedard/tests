export const initialState = []

export const ADD = 'add'
export const REMOVE = 'remove'
export const NUKE = 'nuke'
export const INITIALIZE = 'initialize'

const reducer = (state, action) => {
  switch (action.type) {
    case ADD:
      return [...state, action.payload]
    case NUKE:
      return initialState
    case REMOVE:
      return state.filter((favourite) => favourite !== action.payload)
    case INITIALIZE:
      return action.payload
    default:
      throw new Error('Unknown type')
  }
}

export default reducer
