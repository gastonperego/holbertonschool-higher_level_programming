fetch('https://swapi-api.hbtn.io/api/films/?format=json')

  .then((res) => {
    return res.json();
  })

  .then((data) => {
    const list = document.querySelector('#list_movies');
    for (const movie of data.results) {
      const li = document.createElement('li');
      li.appendChild(document.createTextNode(movie.title));
      list.appendChild(li);
    }
  });
