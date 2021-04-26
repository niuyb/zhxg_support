// created by TomTsong, 20191231.

//主要针对POST请求返回数据中的errmsg信息进行处理
var errmsg = $("#errmsg").text();
if (errmsg){
    Tip(errmsg);
}

function clearTip(){
    $(".tishi").hide();
}

