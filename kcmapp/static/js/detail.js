let modal = document.querySelector('#modal-notice');
let modalActive = document.querySelector('#modal-active');
let modalClose = document.querySelector('#modal-close');

function activeModal(){
    modal.classList.add('active');
    document.querySelector('body').style.overflow = 'hidden';
}

function hideModal(){
    modal.classList.remove('active');
    document.querySelector('body').style.overflow = 'visible';
}

modalActive.addEventListener('click',activeModal);
modalClose.addEventListener('click',hideModal);