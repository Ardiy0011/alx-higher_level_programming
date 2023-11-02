#!/usr/bin/node
const headerchange = $('header');
$('toggle_header').on('click', ()=>{
    headerchange.toggleClass('red green');

})
