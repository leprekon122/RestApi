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
    if(current_url == 'http://127.0.0.1:8000/'){
        document.getElementById('create_news').innerHTML='Create News';

    }
}
get_url()

console.log(window.location.href, window.location.hostname, window.location.protocol)