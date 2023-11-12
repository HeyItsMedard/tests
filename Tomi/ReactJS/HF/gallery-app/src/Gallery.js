import React, { useState, useEffect } from 'react';

function Gallery() {
  const [images, setImages] = useState([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [favorites, setFavorites] = useState([]);
  const [newFavorite, setNewFavorite] = useState('');

  useEffect(() => {
    fetch('https://gist.githubusercontent.com/szakitom/5aa9949fedec1596c591c664b98f0864/raw/49342a6f79234e79a1d66213a8eb42d14d96c47a/images.json')
      .then((response) => response.json())
      .then((data) => setImages(data))
      .catch((error) => console.error('Hiba történt a képek betöltése közben:', error));
  }, []);

  const prevImage = () => {
    if (currentIndex > 0) {
      setCurrentIndex(currentIndex - 1);
    }
  };

  const nextImage = () => {
    if (currentIndex < images.length - 1) {
      setCurrentIndex(currentIndex + 1);
    }
  };

  const addFavorite = () => {
    const altDescription = images[currentIndex]?.alt_description;
    if (altDescription && !favorites.includes(altDescription)) {
      setFavorites([...favorites, altDescription]);
      setNewFavorite(altDescription);
    }
  };

  const removeFavorite = (altDescriptionToRemove) => {
    const updatedFavorites = favorites.filter((altDescription) => altDescription !== altDescriptionToRemove);
    setFavorites(updatedFavorites);
  };

  return (
    <div className="gallery">
      <div className="image-container">
        <img src={images[currentIndex]?.urls.regular} alt={images[currentIndex]?.alt_description} />
      </div>

      <div className="controls-container">
        <div className="image-controls">
          <button onClick={prevImage} disabled={currentIndex === 0}>Előző</button>
          <button onClick={addFavorite}>Kedvelés</button>
          <button onClick={nextImage} disabled={currentIndex === images.length - 1}>Következő</button>
        </div>

        <div className="favorite-container">
          <h2>Kedvelt képek</h2>
          <ul className="favorite-list">
            {favorites.map((favorite, index) => (
              <li key={index}>
                {favorite}
                <button onClick={() => removeFavorite(favorite)}>Törlés</button>
              </li>
            ))}
            {favorites.length === 0 && <li>Nincs kedvelt kép.</li>}
          </ul>
        </div>
      </div>
    </div>
  );
}

export default Gallery;