import React, { useState } from 'react';

function Favorites({ favoriteImages }) {
  const removeFromFavorites = (index) => {
  };

  return (
    <div className="favorites">
      <h2>Favorites</h2>
      <ul>
        {favoriteImages.map((image, index) => (
          <li key={index}>
            <img src={image.url} alt={image.alt} />
            <button onClick={() => removeFromFavorites(index)}>Remove</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Favorites;
