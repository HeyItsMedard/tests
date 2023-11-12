import PropTypes from 'prop-types'

const About = ({ date, user }) => (
  <div>The application was created at: {date}</div>
)

About.propTypes = {
  date: PropTypes.string,
  user: PropTypes.string.isRequired
}

About.defaultProps = {
  date: 'holnap'
}

export default About
