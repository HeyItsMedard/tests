import { createContext, useEffect, useReducer } from 'react'
import reducer, {
  ADD,
  INITIALIZE,
  NUKE,
  REMOVE,
  initialState
} from './FavouritesReducer'

export const FavouritesContext = createContext()

const FavouritesProvider = (props) => {
  const [favourites, dispatch] = useReducer(
    reducer,
    JSON.parse(window.localStorage.getItem('favourites')) || initialState
  )

  useEffect(() => {
    const data = JSON.parse(window.localStorage.getItem('favourites'))
    if (data) {
      // dispatch({ type: INITIALIZE, payload: data })
    }
  }, [])

  useEffect(() => {
    if (favourites.length > 0) {
      window.localStorage.setItem('favourites', JSON.stringify(favourites))
    }
  }, [favourites])

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
