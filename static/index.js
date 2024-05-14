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

// document.getElementById("search").addEventListener("onkeydown", calculateValue);