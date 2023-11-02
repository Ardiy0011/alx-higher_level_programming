#!/usr/bin/node

var headertext = $('header')
// change inter text to a nother text
$('#update_header').on('click', ()=>{
    headertext.text('New Header!!!')
});
