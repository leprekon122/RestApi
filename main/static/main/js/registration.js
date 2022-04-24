function login_off(){
    var current_url = document.URL
    console.log(current_url)
    if(current_url == 'https://rest-api111.herokuapp.com/registration/'){
        document.getElementById('login_nav').style.display='none';
    }
}
login_off()