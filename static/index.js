function calculateValue(){
    var Table = document.getElementById('tid');
    Table.innerHTML = '';
    res = document.getElementById("search").value
    if(res!= undefined && res.length >3){
        return res
    }
    else {
        return ""
    }
}
function hidetable(){
    window.onload = function() {
    var tableEL = $("weather_table").find("tr");
     for (var i = 0; i < tableEL.length; i++) {
    tableEL[i].hide();

        }
    };
}
hidetable()
// document.getElementById("search").addEventListener("onkeydown", calculateValue);