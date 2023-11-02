#!/usr/bin/node

var list = $('UL.my_list')
var item = document.createElement('li');
item.innerHTML = 'Item';
$('#add_item').on('click', ()=>{
    list.append(item);
});
