const burgerBtn = document.getElementById('burger-btn');
const navMenu = document.getElementById('nav_menu');
const closeBtn = document.getElementById('close-btn');

// Open the menu
burgerBtn.addEventListener('click', () => {
  navMenu.classList.add('active');
});
navMenu.addEventListener('click',()=>{navMenu.classList.remove('active')})

// Close the menu
closeBtn.addEventListener('click', () => {
  navMenu.classList.remove('active');
});

// Close when any link is clicked
menuLinks.forEach(link => {
  link.addEventListener('click', () => {
    menu.classList.remove('active');
  });
});
