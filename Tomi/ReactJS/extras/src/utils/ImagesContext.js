import { createContext, useEffect, useReducer } from 'react'
import reducer, { INITIALIZED, initialState } from './ImagesProvider'

export const ImagesContext = createContext()

const ImagesProvider = (props) => {
  const [{ images, loading }, dispatch] = useReducer(reducer, initialState)

  useEffect(() => {
    const download = async () => {
      const resp = await fetch(process.env.REACT_APP_URL)
      const images = await resp.json()
      dispatch({ type: INITIALIZED, payload: images })
    }
    if (images.length === 0) {
      download()
    }
  }, [images.length])

  return (
    <ImagesContext.Provider
      value={{
        images,
        loading
      }}
      {...props}
    />
  )
}

export default ImagesProvider
