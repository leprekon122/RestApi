function login_off(){
    var current_url = document.URL
    console.log(current_url)
    if(current_url == 'http://127.0.0.1:8000/registration/'){
        document.getElementById('login_nav').style.display='none';
    }
}
login_off()