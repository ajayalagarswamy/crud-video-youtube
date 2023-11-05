let menuIcon = document.querySelector('.menu-icon')
let sidebar = document.querySelector('.sidebar')
let container =document.querySelector('.container')

menuIcon.onClick =function(){
    sidebar.classlist.toggle('small-sidebar')
    container.claslist.toggle('large-container')
}
console.log(container)