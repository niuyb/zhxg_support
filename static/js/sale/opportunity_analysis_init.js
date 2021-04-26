//商机分析


function toggleFunc(that){
    var h = $(that).attr("href");
    var h = h.replace("#tab-", "");
    setTimeout(function(){
            initVue(h);
    }, 100);
}

function initVue(Id){
    // var dptTree = new Vue({
     if(Id == "opportunity"){
        return initOpportunityVue();
    }

}

$(document).ready(function(){
    $($("ul.nav.nav-tabs li.active a")[0]).click();
});