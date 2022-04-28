  function panel(){
    var user = document.getElementById('username')
    if(user.innerHTML == 'AnonymousUser'){
        var panel = document.getElementById('panel').style.display = 'none'
    } else {
        var panel = document.getElementById('panel').style.display = 'run-in';
    }
 }
 panel()


 function edits(){
    var user = document.getElementById('username')
    if(user.innerHTML == 'AnonymousUser'){
        window.alert('you must login')
        return false;
        } else {
            return true
        }
 }



 function chose_color(){
    document.getElementById('panel').style.backgroundImage = "linear-gradient(to right, #145c51, #a68d14)"
    el = document.getElementById('panel')
    el.style.transitionDuration = '1s';
    el.style.boxShadow = "5px 5px 15px  yellow";

 }

function chose_color_out(){
    el = document.getElementById('panel')
    el.style.transitionDuration = '1s';
    el.style.backgroundImage = 'linear-gradient(to right, #69330d, #63a8bf)'
    el.style.boxShadow = "none";


}


function get_url(){
    var current_url = document.URL

    if(current_url == 'https://rest-api111.herokuapp.com/'){
        document.getElementById('create_news').innerHTML='Create News'
        document.getElementById('log_out').style.display='inline'
        document.getElementById('comments_button').style.display='inline';

    }
    }

get_url()

function log_btn(){
    var users = document.getElementById('username').innerHTML
    if(users != 'AnonymousUser'){
        document.getElementById('login_nav').style.display='none';
    }
}
log_btn();




