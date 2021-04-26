// var urlDataTopBar = "/sale/data/top/bar";
// var urlDataTaskCompany = "/sale/data/task/company";
// var urlDataTaskRegional = "/sale/data/task/regional";
var urlDataCustomerAll = "/sale/data/customer/all";
var urlDataCustomerDay = "/sale/data/customer/day";
var urlDataMoneyAll = "/sale/data/money/all";
var urlDataMoneyDay = "/sale/data/money/day";

var goalRegionalsYearApi = "/sale/goal/regionals/year/api";
var goalRegionalsMonthApi = "/sale/goal/regionals/month/api";

var paymentCompanyMonthsApi = "/sale/payment/company/months/api";
var paymentCompanyDaysApi = "/sale/payment/company/days/api";

function renderChart(Id, option){
    var dom = document.getElementById(Id);
    var myChart = echarts.init(dom);
    var app = {};
    if (option && typeof option === "object") {
        myChart.setOption(option, true);
        window.addEventListener("resize", function(){              
            myChart.resize();
        })
    }
    return myChart;
}

function renderChartTaskCompany(){
    var url = urlDataTaskCompany;
    $.get(url, function(result, status){
        var Id = "echarts-task-company-chart";
        renderChart(Id, result.data);
    });      
}

function renderChartTaskRegional(){
    var url = urlDataTaskRegional;
    $.get(url, function(result, status){
        var Id = "echarts-task-regional-chart";
        renderChart(Id, result);
    });      
}

function renderChartCustomerAll(){
    var url = urlDataCustomerAll;
    $.get(url, function(result, status){
        var Id = "echarts-line-chart";
        renderChart(Id, result);
    });      
}

function renderChartCustomerDay(){
    var url = urlDataCustomerDay;
    $.get(url, function(result, status){
        var Id = "echarts-bar-chart";
        renderChart(Id, result);
    });      
}

function renderChartMoneyAll(){
    var url = urlDataMoneyAll;
    $.get(url, function(result, status){
        var Id = "echarts-scatter-chart";
        renderChart(Id, result);
    });      
}

function renderChartMoneyDay(){
    var url = urlDataMoneyDay;
    $.get(url, function(result, status){
        var Id = "echarts-k-chart";
        renderChart(Id, result);
    });      
}

// 渲染图表 - 指定财年，政务事业部各大区目标完成情况
function renderChartGoalRegionalsYear(){
    var url = goalRegionalsYearApi;
    $.get(url, function(result, status){
        var Id = "echarts-g-rs-y";
        renderChart(Id, result.data);
    })
}

// 渲染图表 - 指定月份，政务事业部各大区目标完成情况
function renderChartGoalRegionalsMonth(){
    var url = goalRegionalsMonthApi;
    $.get(url, function(result, status){
        var Id = "echarts-g-rs-m";
        renderChart(Id, result.data);
    })
}

// // 监听柱状图点击事件
// function monitClickOnPcms(){
//     var Id = "echarts-pcms";
//     var myChart = echarts.getInstanceByDom(document.getElementById(Id));
//     console.log(myChart);
//     myChart.getZr().on('click', params => {
//         let pointInPixel = [params.offsetX, params.offsetY]
//         if (myChart.containPixel('grid', pointInPixel)) {
//             console.log(params);
//             let xIndex = myChart.convertFromPixel({ seriesIndex: 0 }, [params.offsetX, params.offsetY])[0];
//             console.log(xIndex);
//         }
//     });
// }

// 渲染图表 - 指定时间段内全公司每天的回款情况
function renderChartPaymentCompanyDays(start, end){
    var url = paymentCompanyDaysApi + "?";
    if (start){
        url = url + "start=" + start + "&";
    }
    if (end){
        url = url + "end=" + end;
    }
    // function makeOnClick(data){}
    $.get(url, function(result, status){
        var Id = "echarts-pcds";
        result.data.toolbox.feature.myDataView.onclick = function(){
            var this_url = this.model.option.url;
            window.open(this_url);
        }
        renderChart(Id, result.data);
    });
}

// 渲染图表 - 指定时间段内全公司每月的回款情况
function renderChartPaymentCompanyMonths(){
    var url = paymentCompanyMonthsApi;
    $.get(url, function(result, status){
        var Id = "echarts-pcms";
        var myChart = renderChart(Id, result.data);
        var xdata = result.data.xAxis.data;
        myChart.getZr().on('click', params => {
            let pointInPixel = [params.offsetX, params.offsetY]
            if (myChart.containPixel('grid', pointInPixel)) {
                let xIndex = myChart.convertFromPixel({ seriesIndex: 0 }, [params.offsetX, params.offsetY])[0];
                var start = xdata[xIndex];
                renderChartPaymentCompanyDays(start);
            }
        });
    })
}

// renderChartGoalRegionalsYear();
renderChartGoalRegionalsMonth();

renderChartPaymentCompanyMonths();
renderChartPaymentCompanyDays();

// renderChartCustomerAll();
// renderChartCustomerDay();
// renderChartMoneyAll();
// renderChartMoneyDay();

// 强制echarts图表随父级元素大小变化而发生变化
$(function(){
    $(".echarts").each(function(){
        var this_id = this.id;
        $(this).resize(function(){
            var myChart = echarts.getInstanceByDom(document.getElementById(this_id));
            myChart.resize();
        });
    });
});

// 当侧边栏宽度发生变化时，强制echarts图表自适应
$(function(){
    $(".nav-header").click(function(){
        $(".echarts").each(function(){
            var this_id = this.id;
            var myChart = echarts.getInstanceByDom(document.getElementById(this_id));
            myChart.resize();
        });
    });
});

// 当点击 "x" 按钮时，隐藏图表的祖级元素
$(function(){
    $(".close-link").each(function(){
        $(this).bind("click", function(){
            $(this.parentElement.parentElement.parentElement.parentElement).css("display", "none");
        });
    });
});

// $(document).ready(function(){
//     var Id = "echarts-pcms";
//     var myChart = echarts.getInstanceByDom(document.getElementById(Id));
//     console.log(myChart);
//     myChart.on('click', params => {
//         let pointInPixel = [params.offsetX, params.offsetY]
//         if (myChart.containPixel('grid', pointInPixel)) {
//         let xIndex = myChart.convertFromPixel({ seriesIndex: 0 }, [params.offsetX, params.offsetY])[0];
//         console.log(xIndex);
//         }
//     });
// });
