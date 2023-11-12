export const INITIALIZED = 'INITIALIZED'

export const initialState = {
  images: [],
  loading: true
}

const reducer = (state, { type, payload }) => {
  switch (type) {
    case INITIALIZED:
      return { images: payload, loading: false }
    default:
      throw new Error('Unknown type')
  }
}

export default reducer
