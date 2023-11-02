#!/usr/bin/node

$.ajax({
    url: "https://swapi-api.alx-tools.com/api/people/5/?format=json",

    success: function( result ) {
        const data = result.name;
      $( "#character" ).text(data);
    }
  });
