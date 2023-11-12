import { useContext } from 'react'
import { FavouritesContext } from '../utils/FavouritesContext'

const useFavourites = () => {
  const context = useContext(FavouritesContext)
  return context
}

export default useFavourites
