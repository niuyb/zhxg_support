var urlDataMoneyDay = "/sale/data/money/day";

function renderChart(Id, option){
    var dom = document.getElementById(Id);
    var myChart = echarts.init(dom);
    var app = {};
    if (option && typeof option === "object") {
        myChart.setOption(option, true);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }
}

function renderChartMoneyDay(){
    var url = urlDataMoneyDay;
    $.get(url, function(result, status){
        var Id = "money-day";
        renderChart(Id, result)
    });      
}


renderChartMoneyDay();