
const menu = document.querySelector('.navbar_menu');
const login_Btn = document.querySelector('.navbar_loggin_Btn');
login_Btn.addEventListener('click', ()=>{
    menu.classList.toggle('active');
    login_popup.style.display = 'flex';
});
