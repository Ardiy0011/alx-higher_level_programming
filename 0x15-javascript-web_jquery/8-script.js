#!/usr/bin/node

$.ajax({
    url: "https://swapi-api.alx-tools.com/api/films/?format=json",

    success: function( data ) {
            const movies = data.results;
            $.each(movies, function(i, movie) {
                var item = document.createElement('li');
                item.innerHTML = movie.title;
                $( "#list_movies" ).append(item);
            });
  }});
