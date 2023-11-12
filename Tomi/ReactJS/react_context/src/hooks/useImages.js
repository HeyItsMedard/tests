import { useContext } from 'react'
import { ImagesContext } from '../utils/ImagesContext'

const useImages = () => {
  return useContext(ImagesContext)
}

export default useImages
