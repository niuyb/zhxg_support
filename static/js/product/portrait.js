// 政务事业部 - 销售中心
var departmentPortraitUrl = "/sale/portrait/fuzzy";
// var accountActivityUrl = "/sale/account/activity";

Vue.prototype.$echarts = echarts;

function clickFun(param) {
    if (typeof param.seriesIndex == 'undefined') {
        return;
    }
    if (typeof param.value == 'undefined') {
        return;
    }
    if (param.type == 'click') {
        var url = departmentPortraitUrl + "?did=" + param.value;
        window.open(url);
    }
}

function toggleFunc(that){
    var h = $(that).attr("href");
    var h = h.replace("#tab-", "");
    setTimeout(function(){
        var chart = echarts.getInstanceByDom(document.getElementById(h));
        //if (chart){
            chart.resize();
        //}else{
            initVue(h);
        //}
    }, 100);
}

var isinitVue= ''

function initVue(Id){
    if(Id === "yqms"){
        return initYqmsVue();
    }else if(Id == "yqms_log_calendar"){
        if(isinitVue == ''){
            yqmsLogCalendar();
            isinitVue = 1;
        }
    }else if(Id == "yqms_log_overview"){
        return initYqmsLogOverviewVue();
    }else if(Id == "yqms4_log"){
        return initYqms4LogVue();
    }else if(Id == "yqms3_log"){
        return initYqms3LogVue();
    }else if(Id == "zhwp"){
        return initZhwpVue();
    }
    
    
}
