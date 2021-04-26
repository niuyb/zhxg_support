// 2020-04-26 added by TomTsong
var mainTabIds = [
    "g-center-tree", 
    "goal-regions-month",
    "work-daily", 
    // "about-salers-work-daily",
    "about-account",
    "about-opportunity",
    "about-customer"
];

var initedVues = {};

function toggleFunc(that){
    var h = $(that).attr("href");
    var h = h.replace("#tab-", "");
    setTimeout(function(){
        if (h=="main"){
            var inited = false;
            for (var i in mainTabIds){
                var tid = mainTabIds[i];
                var chart = echarts.getInstanceByDom(document.getElementById(tid));
                if (chart){
                    inited = true;
                    chart.resize();
                }
            }
            if (inited){
                return;
            }
        }
        var chart = echarts.getInstanceByDom(document.getElementById(h));
        if (chart){
            chart.resize();
        }else{
            var ini = initedVues[h];
            if (ini){
                return;
            }
            initedVues[h] = 1;
            if (h=="main"){
                initMain();
            }else{
                initVue(h);
            }
        }
    }, 100);
}

function initMain(){
    initVue("g-center-tree");
    initVue("goal-regions-month");
    initVue("work-daily");
    // initVue("about-salers-work-daily");
    initVue("about-account");
    initVue("about-opportunity");
    initVue("about-customer");
}
// // initVue("about-account-yqms");


$(document).ready(function(){
    // console.log($("ul.nav.nav-tabs li.active a")[0]);
    $($("ul.nav.nav-tabs li.active a")[0]).click();
});
