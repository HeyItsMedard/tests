import styled, { css } from 'styled-components/macro'
import { NavLink as RouterLink, useNavigate } from 'react-router-dom'

const StyledLink = styled.div`
  text-decoration: ${({ isActive }) => (isActive ? 'underline' : 'none')};
  color: black;
  font-weight: ${({ isActive }) => (isActive ? 'bold' : '')};
`

const NavLink = ({ children, ...rest }) => {
  return (
    <RouterLink
      {...rest}
      css={css`
        text-decoration: none;
        margin-right: 10px;
      `}
    >
      {({ isActive }) => (
        <StyledLink isActive={isActive}>{children}</StyledLink>
      )}
    </RouterLink>
  )
}

const Header = () => {
  const navigate = useNavigate()
  const isDevMode = process.env.NODE_ENV === 'development'

  return (
    <nav
      css={css`
        display: flex;
        align-items: center;
        height: 50px;
        background: lightgray;
        padding: 10px;
        width: 100%;
        justify-content: space-between;
      `}
    >
      <div
        onClick={() => navigate('/')}
        css={css`
          text-decoration: none;
          font-weight: 0;
          cursor: pointer;
          display: flex;
          flex-direction: row;
          justify-content: center;
          align-items: center;
        `}
      >
        Gallery
        <div
          css={css`
            margin-left: 10px;
            background: ${isDevMode ? 'red' : 'green'};
            text-transform: uppercase;
            border-radius: 4px;
            padding: 5px;
            color: white;
          `}
        >
          {console.log(process.env)}
          {process.env.REACT_APP_TITLE}
        </div>
      </div>
      <div
        css={css`
          display: flex;
          text-transform: capitalize;
        `}
      >
        <NavLink to="/">home</NavLink>
        <NavLink to="/favourites">favourites</NavLink>
        <NavLink to="/about">?</NavLink>
      </div>
    </nav>
  )
}

export default Header
