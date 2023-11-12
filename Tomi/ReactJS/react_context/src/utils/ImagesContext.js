import { createContext, useEffect, useReducer } from 'react'
import reducer, { INITIALIZED, initialState } from './ImagesProvider'

export const ImagesContext = createContext()

const URL =
  'https://gist.githubusercontent.com/szakitom/5aa9949fedec1596c591c664b98f0864/raw/49342a6f79234e79a1d66213a8eb42d14d96c47a/images.json'

const ImagesProvider = (props) => {
  const [{ images, loading }, dispatch] = useReducer(reducer, initialState)

  useEffect(() => {
    const download = async () => {
      const resp = await fetch(URL)
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
