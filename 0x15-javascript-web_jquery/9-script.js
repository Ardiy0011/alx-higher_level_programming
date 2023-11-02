#!/usr/bin/node

$.ajax({
    url: "https://hellosalut.stefanbohacek.dev/?lang=fr", 
    success: function(data) {
        const helloTranslation = data.hello;

        $('#hello').text(helloTranslation);
    }
  });
