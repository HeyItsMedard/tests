import { useEffect, useState } from 'react'
import { useLocation } from 'react-router-dom'
import styled from 'styled-components'

const GalleryContainer = styled.div`
  display: flex;
  flex-direction: column;
  align-items: center;
`

const Image = styled.img`
  width: 100%;
  aspect-ratio: 1/1;
  object-fit: contain;

  @media (min-width: 800px) {
    width: 50vw;
  }
`

const ButtonRow = styled.div`
  display: flex;
  width: 100%;
  justify-content: space-evenly;
  height: 50px;
`

const Button = styled.button`
  outline: none;
  background: transparent;
  min-width: 50px;
  border: 0;
  cursor: pointer;
  font-size: 40px;
`

const Gallery = ({ images, favourite, favourites, removeFavourite }) => {
  const [index, setIndex] = useState(0)
  const location = useLocation()

  useEffect(() => {
    if (location.state) {
      const findIndex = images.findIndex(
        (image) => image.id === location.state.id
      )
      setIndex(findIndex)
    }
  }, [location, images])

  const prev = () => {
    setIndex((index - 1 + images.length) % images.length)
  }

  const next = () => {
    setIndex((index + 1) % images.length)
  }

  return (
    <GalleryContainer>
      <Image
        src={images[index].urls.regular}
        alt={images[index].alt_description}
      />
      <ButtonRow>
        <Button onClick={prev}>⬅️</Button>
        {favourites.includes(images[index].id) ? (
          <Button onClick={() => removeFavourite(images[index].id)}>💔</Button>
        ) : (
          <Button onClick={() => favourite(images[index].id)}>❤️</Button>
        )}
        <Button onClick={next}>➡️</Button>
      </ButtonRow>
    </GalleryContainer>
  )
}

export default Gallery
