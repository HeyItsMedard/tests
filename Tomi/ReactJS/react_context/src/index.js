import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import { BrowserRouter } from 'react-router-dom'
import './styles.css'

import App from './App'
import ImagesProvider from './utils/ImagesContext'
import FavouritesProvider from './utils/FavouritesContext'

const rootElement = document.getElementById('root')
const root = createRoot(rootElement)

root.render(
  <StrictMode>
    <BrowserRouter>
      <ImagesProvider>
        <FavouritesProvider>
          <App />
        </FavouritesProvider>
      </ImagesProvider>
    </BrowserRouter>
  </StrictMode>
)
