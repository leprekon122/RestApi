function log_btn(){
    var users = document.getElementById('username').innerHTML
    if(users != 'AnonymousUser'){
        document.getElementById('login_nav').style.display='none';
    }
}
log_btn()