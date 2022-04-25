function log_btn(){
    var current_url = document.URL
    if(current_url != 'https://127.0.0.1:8000/'){
    document.getElementById('login_nav').style.display='none';
    }
}

log_btn()