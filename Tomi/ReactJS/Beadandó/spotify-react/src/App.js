import {useEffect, useState} from "react";
import './App.css';
import axios from 'axios';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Container, InputGroup, FormControl, Button, Row, Card} from 'react-bootstrap';

const CLIENT_ID = "ecba8775c2de416b9424c53286d9868a"
const CLIENT_SECRET = "0f765175790b438db56a6441de66ffe9"
const REDIRECT_URI = "http://localhost:3000"
const AUTH_ENDPOINT = "https://accounts.spotify.com/authorize"
const RESPONSE_TYPE = "token"

function App() {
    const [searchInput, setSearchInput] = useState("")
    const [accessToken, setAccessToken] = useState("")
    const [albums, setAlbums] = useState("")
    // const [artists, setArtists] = useState([])

    useEffect(() => {
        var authParameters = {
            method: 'POST',
            headers:{
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: 'grant_type=client_credentials&client_id=' +CLIENT_ID + '&client_secret=' + CLIENT_SECRET
        }
        fetch(`https://accounts.spotify.com/api/token`, authParameters)
            .then(result => result.json())
            .then(data => setAccessToken(data.access_token))
    }, [])

    async function search() {
        console.log("Search for " +searchInput);
        var searchParameters = {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': 'Bearer '+ accessToken
            }
        }
        var artistID = await fetch('https://api.spotify.com/v1/search?q='+searchInput+'&type=artist', searchParameters)
            .then(response => response.json())
            .then(data => {return data.artists.items[0].id})
        console.log('Artist ID: ' +artistID)
        var returnedAlbums = await fetch('https://api.spotify.com/v1/artists/' + artistID+'/albums'+ '?include_groups=album&market=US&limit=50', searchParameters)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                setAlbums(data.items)})
    }
    // const searchArtists = async (e) => {
    //     e.preventDefault()
    //     const {data} = await axios.get("https://api.spotify.com/v1/search", {
    //         headers: {
    //             Authorization: `Bearer ${token}`,
    //         },
    //         params: {
    //             q: searchKey,
    //             type: "artist",
    //         }
    //     })

    //     setArtists(data.artists.items)
    // }

    return (
        <div className="App">
            <Container>
                <InputGroup className="mb-3" size="lg">
                    <FormControl 
                        placeholder="Search for Artist"
                        type="input"
                        onKeyPress={event => {
                            if (event.key == "Enter"){
                                search();
                            }
                        }}
                        onChange={event => setSearchInput(event.target.value)}
                    />
                    <Button onClick={search}>
                        search
                    </Button>
                </InputGroup>
            </Container>
            <Container>
                <Row className="mx-2 row row-cols-4"></Row>
                {albums.map((album, i)=>{
                    return (<Card>
                        <Card.Img src = {album.images[0].url}/>
                        <Card.Body>
                            <Card.Title>{album.name}</Card.Title>
                        </Card.Body>  
                    </Card>)
                })}
                
            </Container>
        </div>
    );
}

export default App;