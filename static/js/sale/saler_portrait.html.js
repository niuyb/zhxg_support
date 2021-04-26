var urlDataTask = "http://127.0.0.1:8000/sale/data/task";
var urlDataTaskRegional = "http://127.0.0.1:8000/sale/data/task/regional";
var urlDataCustomerAll = "http://127.0.0.1:8000/sale/data/customer/all";
var urlDataCustomerDay = "http://127.0.0.1:8000/sale/data/customer/day";
var urlDataMoneyAll = "http://127.0.0.1:8000/sale/data/money/all";
var urlDataMoneyDay = "http://127.0.0.1:8000/sale/data/money/day";
var urlDataWorkDaily = "http://127.0.0.1:8000/sale/data/work/daily";
function renderChart(Id, option){
    var dom = document.getElementById(Id);
    var myChart = echarts.init(dom);
    var app = {};
    if (option && typeof option === "object") {
        myChart.setOption(option, true);
    }
}

function renderChartTask(){
    var url = urlDataTask;
    $.get(url, function(result, status){
        var Id = "echarts-task-chart";
        renderChart(Id, result)
    });      
}

function renderChartTaskRegional(){
    var url = urlDataTaskRegional;
    $.get(url, function(result, status){
        var Id = "echarts-task-regional-chart";
        renderChart(Id, result)
    });      
}

function renderChartCustomerAll(){
    var url = urlDataCustomerAll;
    $.get(url, function(result, status){
        var Id = "echarts-line-chart";
        renderChart(Id, result)
    });      
}

function renderChartCustomerDay(){
    var url = urlDataCustomerDay;
    $.get(url, function(result, status){
        var Id = "echarts-bar-chart";
        renderChart(Id, result)
    });      
}

function renderChartMoneyAll(){
    var url = urlDataMoneyAll;
    $.get(url, function(result, status){
        var Id = "echarts-scatter-chart";
        renderChart(Id, result)
    });      
}

function renderChartMoneyDay(){
    var url = urlDataMoneyDay;
    $.get(url, function(result, status){
        var Id = "echarts-k-chart";
        renderChart(Id, result)
    });      
}

function renderChartWorkDaily(){
    var url = urlDataWorkDaily;
    $.get(url, function(result, status){
        var Id = "echarts-daily-chart";
        renderChart(Id, result)
    });      
}

// renderChartTask();
// renderChartTaskRegional();
renderChartCustomerAll();
renderChartCustomerDay();
renderChartMoneyAll();
renderChartMoneyDay();
renderChartWorkDaily();