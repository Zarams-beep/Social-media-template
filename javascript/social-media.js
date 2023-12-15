function addClass(selector,formerinfo='', nowInfo=''){
    const button = document.querySelector(selector)
    if (!button.classList.contains('is-blue-button')){
        button.classList.add('is-blue-button');
        button.innerHTML=nowInfo
    }else{
        button.classList.remove('is-blue-button');
        button.innerHTML=formerinfo
    }
}