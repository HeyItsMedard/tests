import { useEffect, useState } from 'react'
import { useLocation } from 'react-router-dom'
import styled from 'styled-components'
import useFavourites from '../hooks/useFavourites'
import useImages from '../hooks/useImages'

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

const Gallery = () => {
  const [index, setIndex] = useState(0)
  const location = useLocation()
  const { favourites, add, remove } = useFavourites()
  const { images } = useImages()

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
        <Button onClick={prev}>
          <span role="img" aria-label="previous">
            ⬅️
          </span>
        </Button>
        {favourites.includes(images[index].id) ? (
          <Button onClick={() => remove(images[index].id)}>
            <span role="img" aria-label="unfavourite">
              💔
            </span>
          </Button>
        ) : (
          <Button onClick={() => add(images[index].id)}>
            <span role="img" aria-label="favourite">
              ❤️
            </span>
          </Button>
        )}
        <Button onClick={next}>
          <span role="img" aria-label="next">
            ➡️
          </span>
        </Button>
      </ButtonRow>
    </GalleryContainer>
  )
}

export default Gallery
