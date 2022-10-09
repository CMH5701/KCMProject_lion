console.log('h1h1');

let elInputid = document.querySelector('id_username');
let elInputPassword = document.querySelector('id_password1');
let elInputPasswordretype = document.querySelector('id_password2');
let signupbutton = document.querySelector('#submit');

let elFailmessage = document.querySelector('.failure_message');
let elSuccessmessage = document.querySelector('.success_message');
let elMismatchmessage = document.querySelector('.mismatch_message');
let elMatchmessage = document.querySelector('.match_message');

function isMoreThan4Length(value){
    return value.length >= 4;
}
elInputid.onkeyup = function(){
    if(isMoreThan4Length(elInputid.value)){
        elSuccessmessage.classList.remove('hide');
        elFailmessage.classList.add('hide');
    }
    else{
        elSuccessmessage.classList.add('hide');
        elFailmessage.classList.remove('hide');
    }
}
function isMatch(pass1,pass2){
    if(pass1 == pass2){
        return 1;
    }
    else{
        return 0;
    }
}
elInputPasswordretype.onkeyup = function(){
    if(isMatch(elInputPassword.value,elInputPasswordretype.value)){
        elMatchmessage.classList.remove('hide');
        elMismatchmessage.classList.add('hide');
    }
    else{
        elMatchmessage.classList.add('hide');
        elMismatchmessage.classList.remove('hide');
    }
}

elInputid.addEventListener('keyup',button);
elInputPasswordretype.addEventListener('keyup',button);

function button(){
    switch(!(elInputid.value && elInputPassword.value && elInputPasswordretype.value && elInputPassword.value == elInputPasswordretype.value)){
        case true : signupbutton.disabled = true; break;
        case false: signupbutton.disabled = false; break;
    }
}