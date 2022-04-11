  function panel(){
    var user = document.getElementById('username')
    console.log(user.innerHTML)
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
    document.getElementById('panel').style.backgroundColor = '#b85007'

 }

function chose_color_out(){
    document.getElementById('panel').style.backgroundColor = '#69330d'
}
