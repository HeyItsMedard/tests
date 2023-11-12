import { createContext, useReducer } from 'react'
import reducer, { ADD, NUKE, REMOVE, initialState } from './FavouritesReducer'

export const FavouritesContext = createContext()

const FavouritesProvider = (props) => {
  const [favourites, dispatch] = useReducer(reducer, initialState)
  const favourite = (id) => {
    if (!favourites.includes(id)) {
      dispatch({ type: ADD, payload: id })
    }
  }

  const removeFavourite = (id) => {
    dispatch({ type: REMOVE, payload: id })
  }

  const nuke = () => {
    dispatch({ type: NUKE })
  }

  return (
    <FavouritesContext.Provider
      value={{ favourites, add: favourite, remove: removeFavourite, nuke }}
      {...props}
    />
  )
}

export default FavouritesProvider
