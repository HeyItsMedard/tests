import { Link } from 'react-router-dom'
import styled, { css } from 'styled-components/macro'
import useFavourites from '../hooks/useFavourites'
import useImages from '../hooks/useImages'

const ListItem = styled.div`
  font-size: 20px;
  text-decoration: none;
  color: black;
  display: flex;
  height: 30px;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 10px;
  width: 100%;
`

const Container = styled.div`
  padding: 10px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  width: 100%;
  flex-direction: column;
  height: 100dvh;
`

const Button = styled.button`
  outline: none;
  border: 0;
  background: transparent;
  height: 100%;
  aspect-ratio: 1/1;
  font-size: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  cursor: pointer;
`

const Favourites = () => {
  const { favourites, remove, nuke } = useFavourites()
  const { images } = useImages()

  if (favourites.length === 0) {
    return <Container>No favourites yet :(</Container>
  }

  return (
    <Container>
      {favourites.map((favouriteId) => {
        const image = images.find((image) => image.id === favouriteId)
        return (
          <ListItem key={favouriteId}>
            <Link
              css={css`
                text-decoration: none;
                color: black;
              `}
              to="/"
              state={{ id: favouriteId }}
            >
              {image.alt_description}
            </Link>
            <Button onClick={() => remove(favouriteId)}>
              <span role="img" aria-label="remove">
                🗑️
              </span>
            </Button>
          </ListItem>
        )
      })}
      <button
        onClick={nuke}
        css={css`
          background: transparent;
          border: 0;
          font-size: 30px;
        `}
      >
        <span role="img" aria-label="remove all">
          💣
        </span>
      </button>
    </Container>
  )
}

export default Favourites
