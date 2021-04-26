// created by
document.write("<script language=javascript src='/static/js/common.js'></script>");

$(document).ready(function () {
    renderTable();
    moneyAnalysis();
    localAnalysis();
    industry1Analysis();
    industry2Analysis();
    occupiedAnalysis();

});


function occupiedAnalysis(){
    // 基于准备好的dom，初始化echarts实例
    var myChart1 = echarts.init(document.getElementById('occupiedEcharts'));
    var occupiedAnalysis_url = $("#occupied_analysis").text();
    // alert(occupiedAnalysis_url);
    $.get(occupiedAnalysis_url, function(data, status){
        if (data.status == null || data.status == undefined){
            // window.location.reload();
            return;
        }
        if (data.status < 1){
            alert(data.message);
        }

        // 指定图表的配置项和数据
        option = {
            title : {
                text: '客户占有率分析',
                // subtext: '纯属虚构',
                x:'left'
            },
            tooltip : {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c} ({d}%)"
            },
            // legend: {
            //     orient : 'vertical',
            //     x : 'left',
            //     data:data.items.legend
            // },
            toolbox: {
                show : true,
                feature : {
                    mark : {show: true},
                    dataView : {show: true, readOnly: false},
                    magicType : {
                        show: true,
                        type: ['pie', 'funnel'],
                        option: {
                            funnel: {
                                x: '25%',
                                width: '50%',
                                funnelAlign: 'left',
                                max: 1548
                            }
                        }
                    },
                    restore : {show: true},
                    saveAsImage : {show: true}
                }
            },
            calculable : true,
            series : [
                {
                    name:'客户占有率',
                    type:'pie',
                    // radius : '55%',
                    // center: ['50%', '60%'],
                    data:data.items.data,
                    clickable:true,　　　　　　 //是否开启点击
                    minAngle: 3,           　　 //最小的扇区角度（0 ~ 360），用于防止某个值过小导致扇区太小影响交互
                    avoidLabelOverlap: true,   //是否启用防止标签重叠策略
                    // hoverAnimation:false,　　  //是否开启 hover 在扇区上的放大动画效果。
                    // silent: true,　　　　　　　　//图形是否不响应和触发鼠标事件
                    radius: ['25%', '40%'],
                    center: ['50%', '50%'],
                    label:{
                        align: 'left',
                        normal:{
                            textStyle : {
                                fontSize : 12
                            }
                        }
                    }
                }
            ]
        };
        myChart1.setOption(option);
        });
}

function moneyAnalysis(){
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('moneyEcharts'));
    var moneyAnalysis_url = $("#money_analysis").text();
    var id = $("#competitor_id").attr("value");
    // alert(id);
    var url = moneyAnalysis_url + "?id=" + id;
    // alert(url);
    $.get(url, function(data, status){
        if (data.status == null || data.status == undefined){
            // window.location.reload();
            return;
        }
        if (data.status < 1){
            alert(data.message);
        }
        // alert(data.items);
        // 指定图表的配置项和数据
        option = {
            title : {
                text: '签单金额分布',
                // subtext: '数据来自网络',
                x:'center'
            },
            tooltip : {
                trigger: 'axis'
            },
            // legend: {
            //     data:['money'],
            //     x:'left'
            // },
            toolbox: {
                show : true,
                x: 'left',
                y: 'top',
                feature : {
                    mark : {show: true},
                    dataView : {show: true, readOnly: false},
                    magicType: {show: true, type: ['line', 'bar']},
                    restore : {show: true},
                    saveAsImage : {show: true}
                }
            },
            calculable : true,
            xAxis : [
                {
                    type : 'value',
                    boundaryGap : [0, 0.01]
                }
            ],
            yAxis : [
                {
                    type : 'category',
                    data : data.items.keys
                }
            ],
            series : [
                {
                    name:'签单量',
                    type:'bar',
                    data:data.items.data
                }
            ]
        };
        myChart.setOption(option);
        function reloaded(items){
            $("#table_list_2").jqGrid('clearGridData');
            $("#table_list_2").jqGrid('setGridParam', {
                datatype: 'local',
                data: items,
                page: 1
            }).trigger("reloadGrid");
        };
        reloaded(data.items.items);
        });
}


function localAnalysis(){
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('localEcharts'));
    var localAnalysis_url = $("#local_analysis").text();
    var id = $("#competitor_id").attr("value");
    var url = localAnalysis_url + "?id=" + id;
    $.get(url, function(data, status){
        if (data.status == null || data.status == undefined){
            // window.location.reload();
            return;
        }
        if (data.status < 1){
            alert(data.message);
        }
        // 指定图表的配置项和数据
        option = {
            title : {
                text: '签单地域分布',
                // subtext: '纯属虚构',
                x:'center'
            },
            tooltip : {
                trigger: 'item'
            },
            // legend: {
            //     orient: 'vertical',
            //     x:'left',
            //     data:['订单量']
            // },
            dataRange: {
                x: 'left',
                y: 'bottom',
                splitList: [
                    {start: 15},
                    {start: 11, end: 15, label: '11~15'},
                    {start: 6, end: 10, label: '6~10'},
                    {start: 3, end: 5, label: '3~5'},
                    {start: 1, end: 2, label: '1~2'}, //, label: '10 到 200（自定义label）'
                    // {start: 5, end: 5, label: '5（自定义特殊颜色）', color: 'wight'},
                    {end: 1, label: '=0'}
                ],
                color: ['#E0022B', '#E09107', '#A3E00B']
            },
            toolbox: {
                show: true,
                orient : 'vertical',
                x: 'left',
                y: 'top',
                feature : {
                    mark : {show: true},
                    dataView : {show: true, readOnly: false},
                    restore : {show: true},
                    saveAsImage : {show: true}
                }
            },
            roamController: {
                show: true,
                x: 'right',
                mapTypeControl: {
                    'china': true
                }
            },
            series : [
                {
                    name: '签单量',
                    type: 'map',
                    mapType: 'china',
                    roam: false,
                    itemStyle:{
                        normal:{
                            label:{
                                show:true,
                                textStyle: {
                                   color: "rgb(249, 249, 249)"
                                }
                            }
                        },
                        emphasis:{label:{show:true}}
                    },
                    data:data.items
                }
            ]
        };
    myChart.setOption(option);
    function reloaded(items){
            $("#table_list_1").jqGrid('clearGridData');
            $("#table_list_1").jqGrid('setGridParam', {
                datatype: 'local',
                data: items,
                page: 1
            }).trigger("reloadGrid");
        };
    reloaded(data.data);
    });
}

// 获取api，访问api，获取数据后，渲染表格
function renderTable() {
    $.jgrid.defaults.styleUI = 'Bootstrap';
    for (var i=1;i<4;i++){
        var initData = JSON.parse($("#init-data" + i).text());
        configureTable(initData,i);
    }

}

// 配置并渲染表格
function configureTable(data,i){
    if(i==1){
        $("#table_list_" + i).jqGrid(
            {
                "data": data.items,
                datatype: "local",
                height: "380",
                autowidth: true,
                shrinkToFit: true,
                rowNum: data.row_num,
                rowList: data.row_list,
                colNames: data.col_names,
                colModel: data.col_model,
                pager: "#pager_list_" + i,
                viewrecords: true,
                // caption: "jqGrid 示例1",
                hidegrid: false
            }
        );
    }
    else if(i==2) {
        $("#table_list_" + i).jqGrid({
            "data": data.items,
            datatype: "local",
            // height: "250",
            height: "250",
            autowidth: true,
            shrinkToFit: true,
            rowNum: data.row_num,
            rowList: data.row_list,
            colNames: data.col_names,
            colModel: data.col_model,
            pager: "#pager_list_" + i,
            viewrecords: true,
            // caption: "jqGrid 示例1",
            hidegrid: false
        })}
        else if(i==3) {
        $("#table_list_" + i).jqGrid({
            "data": data.items,
            datatype: "local",
            // height: "250",
            height: "330",
            autowidth: true,
            shrinkToFit: true,
            rowNum: data.row_num,
            rowList: data.row_list,
            colNames: data.col_names,
            colModel: data.col_model,
            pager: "#pager_list_" + i,
            viewrecords: true,
            // caption: "jqGrid 示例1",
            hidegrid: false
        });
    }
    // Add responsive to jqGrid
    $(window).bind('resize', function () {
        var width = $('.jqGrid_wrapper').width();
        $('#table_list_' + i).setGridWidth(width);
        // $('#table_list_2').setGridWidth(width);
    });
}


function industry1Analysis(){
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('industry1echarts'));
    var industryAnalysis_url = $("#industry_analysis").text();
    var id = $("#competitor_id").attr("value");
    var url = industryAnalysis_url + "?id=" + id;
    $.get(url, function(data, status){
        if (data.status == null || data.status == undefined){
            // window.location.reload();
            return;
        }
        if (data.status < 1){
            alert(data.message);
        }
        option = {
            title: {
                text: '签单行业分布(一级行业)',
                // subtext: 'From ExcelHome',
                // sublink: 'http://e.weibo.com/1341556070/AjQH99che'
                x:'center'
            },
            tooltip : {
                trigger: 'axis',
                axisPointer : {            // 坐标轴指示器，坐标轴触发有效
                    type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                },
                formatter: function (params) {
                    var tar = params[0];
                    // return tar.name + '<br/>' + tar.seriesName + ' : ' + tar.value;
                    return tar.name;
                }
            },
            toolbox: {
                show : true,
                feature : {
                    mark : {show: true},
                    dataView : {show: true, readOnly: false},
                    restore : {show: true},
                    saveAsImage : {show: true}
                }
            },
            xAxis : [
                {
                    type : 'category',
                    splitLine: {show:false},
                    data : data.items.keys
                }
            ],
            yAxis : [
                {
                    type : 'value'
                }
            ],
            series : [
                {
                    name:'辅助',
                    type:'bar',
                    stack: '总量',
                    itemStyle:{
                        normal:{
                            barBorderColor:'rgba(0,0,0,0)',
                            color:'rgba(0,0,0,0)'
                        },
                        emphasis:{
                            barBorderColor:'rgba(0,0,0,0)',
                            color:'rgba(0,0,0,0)'
                        }
                    },
                    // data:[0,31, 11, 2, 0]
                    data:data.items.bar
                },
                {
                    name:'签单量',
                    type:'bar',
                    stack: '总量',
                    itemStyle : { normal: {label : {show: true, position: 'inside'}}},
                    data:data.items.data
                }
            ]
        };
        myChart.setOption(option);
    });
}



function industry2Analysis(){
    // 基于准备好的dom，初始化echarts实例
    var myChart = echarts.init(document.getElementById('industry2echarts'));
    var industryAnalysis_url = $("#industry2_analysis").text();
    var id = $("#competitor_id").attr("value");
    var url = industryAnalysis_url + "?id=" + id;
    $.get(url, function(data, status){
        if (data.status == null || data.status == undefined){
            // window.location.reload();
            return;
        }
        if (data.status < 1){
            alert(data.message);
        }
        option = {
            title: {
                text: '签单行业价值(二级行业)',
                // subtext: 'From ExcelHome',
                // sublink: 'http://e.weibo.com/1341556070/AjQH99che'
                x:'center'
            },
            tooltip: {
                trigger: 'axis',
                axisPointer: {
                    type: 'cross',
                    crossStyle: {
                        color: '#999'
                    }
                }
            },
            toolbox: {
                feature: {
                    dataView: {show: true, readOnly: false},
                    magicType: {show: true, type: ['line', 'bar']},
                    restore: {show: true},
                    saveAsImage: {show: true}
                }
            },
            legend: {
                data: ['竞品签单量', '智慧星光签单量', '竞品签单平均金额', '智慧星光签单平均金额'],
                x: 'center',
                y: 'bottom'
            },
            xAxis: [
                {
                    type: 'category',
                    data: data.items.industry2,
                    axisPointer: {
                        type: 'shadow'
                    },
                    axisLabel:{
                        interval:0
                    } //设置全部显示，不间隔
                }
            ],
            yAxis: [
                {
                    type: 'value',
                    name: '签单量:单',
                    min: 0,
                    max: data.items.max_num,
                    interval: data.items.max_num/10,
                    axisLabel: {
                        formatter: '{value} '
                    }
                },
                {
                    type: 'value',
                    name: '平均签单金额:万',
                    min: 0,
                    // max: 35,
                    max:data.items.max_money,
                    // interval: 5,
                    interval: data.items.max_money/10,
                    axisLabel: {
                        formatter: '{value} '
                    }
                }
            ],
            series: [
                {
                    name: '竞品签单量',
                    type: 'bar',
                    data: data.items.competitor_num
                },
                {
                    name: '智慧星光签单量',
                    type: 'bar',
                    data: data.items.our_num
                },
                {
                    name: '竞品签单平均金额',
                    type: 'line',
                    yAxisIndex: 1,
                    data: data.items.competitor_money
                }
                ,
                {
                    name: '智慧星光签单平均金额',
                    type: 'line',
                    yAxisIndex: 1,
                    data: data.items.our_money
                }
            ]
        };

        myChart.setOption(option);
        function reloaded(items){
            $("#table_list_3").jqGrid('clearGridData');
            $("#table_list_3").jqGrid('setGridParam', {
                datatype: 'local',
                data: items,
                page: 1
            }).trigger("reloadGrid");
        };
        // alert(data.items);
        reloaded(data.data);
    });
}