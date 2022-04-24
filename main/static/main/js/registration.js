function log_btn(){
    var current_url = document.URL
    if(current_url != 'https://rest-api111.herokuapp.com/'){
    document.getElementById('login_nav').style.display='none';
    }
}

log_btn()