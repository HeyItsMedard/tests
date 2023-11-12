import { useEffect, useState } from 'react'
import { Routes, Route } from 'react-router-dom'
import Gallery from './components/Gallery'
import Favourites from './components/Favourites'
import Header from './components/Header'
import NotFound from './components/NotFound'

const URL =
  'https://gist.githubusercontent.com/szakitom/5aa9949fedec1596c591c664b98f0864/raw/49342a6f79234e79a1d66213a8eb42d14d96c47a/images.json'

export default function App() {
  const [images, setImages] = useState([])
  const [favourites, setFavourites] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    const download = async () => {
      const resp = await fetch(URL)
      const images = await resp.json()
      setImages(images)
      setLoading(false)
    }
    if (images.length === 0) {
      download()
    }
  }, [images.length])

  if (loading) {
    return <div>loading...</div>
  }

  const favourite = (id) => {
    if (!favourites.includes(id)) {
      setFavourites([...favourites, id])
    }
  }

  const removeFavourite = (id) => {
    const filtered = favourites.filter((favourite) => favourite !== id)
    setFavourites(filtered)
  }

  return (
    <>
      <Header />
      <Routes>
        <Route
          path="/"
          element={
            <Gallery
              images={images}
              favourite={favourite}
              favourites={favourites}
              removeFavourite={removeFavourite}
            />
          }
        />
        <Route
          path="/favourites"
          element={
            <Favourites
              favourites={favourites}
              removeFavourite={removeFavourite}
              images={images}
            />
          }
        />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </>
  )
}
