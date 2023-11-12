import { Link } from 'react-router-dom'
import styled, { css } from 'styled-components/macro'

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
  justify-content: center;
  align-items: center;
  width: 100%;
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

const Favourites = ({ favourites, removeFavourite, images }) => {
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
            <Button onClick={() => removeFavourite(favouriteId)}>🗑️</Button>
          </ListItem>
        )
      })}
    </Container>
  )
}

export default Favourites
