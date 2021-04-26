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
        }

        initVue(h);

    }, 100);
}




$(document).ready(function(){
    // console.log($("ul.nav.nav-tabs li.active a")[0]);
    $($("ul.nav.nav-tabs li.active a")[0]).click();
});
