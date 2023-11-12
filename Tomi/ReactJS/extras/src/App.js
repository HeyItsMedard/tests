import { Suspense, lazy } from 'react'
import { Routes, Route } from 'react-router-dom'
import useImages from './hooks/useImages'
import Header from './components/Header'
import NotFound from './components/NotFound'

const Gallery = lazy(() => import('./components/Gallery'))
const Favourites = lazy(() => import('./components/Favourites'))
const About = lazy(() => import('./components/About'))

export default function App() {
  const { loading } = useImages()

  if (loading) {
    return <div>loading...</div>
  }

  return (
    <>
      <Header />
      <Suspense fallback={<div>loading...</div>}>
        <Routes>
          <Route path="/" element={<Gallery />} />
          <Route path="/favourites" element={<Favourites />} />
          <Route path="/about" element={<About />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </Suspense>
    </>
  )
}
