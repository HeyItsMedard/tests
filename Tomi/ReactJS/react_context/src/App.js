import { Routes, Route } from 'react-router-dom'
import Gallery from './components/Gallery'
import Favourites from './components/Favourites'
import Header from './components/Header'
import NotFound from './components/NotFound'
import useImages from './hooks/useImages'

export default function App() {
  const { loading } = useImages()

  if (loading) {
    return <div>loading...</div>
  }

  return (
    <>
      <Header />
      <Routes>
        <Route path="/" element={<Gallery />} />
        <Route path="/favourites" element={<Favourites />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </>
  )
}
