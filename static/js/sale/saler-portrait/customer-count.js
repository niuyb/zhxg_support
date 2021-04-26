$(function() {
    var dom = document.getElementById("customer-count");
    var myChart = echarts.init(dom);
    var app = {};
    option = null;
    option = {
        legend: {
            x : 'center',
            y : 'top',
            itemWidth: 8,
            itemHeight: 8,
            textStyle:{//图例文字的样式
                // color:'#fff',
                fontSize:12
            },
            data:['正式','试用','停用','其他']
        },
        grid: {
            top: '40%',
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        calculable : true,
        label: {
            show: true,
            formatter: '{b}: {c}'
        },
        series : [
            {
                name:'面积模式',
                type:'pie',
                radius : [0, 60],
                center : ['50%', '60%'],
                // roseType : 'area',
                data:[
                    {value:56, name:'正式'},//,itemStyle:{normal:{color:'#ff7800'}}},
                    {value:307, name:'试用'},//,itemStyle:{normal:{color:'#23eb6a'}}},
                    {value:69, name:'停用'},//,itemStyle:{normal:{color:'#7627cb'}}},
                    {value:80, name:'其他'}//,itemStyle:{normal:{color:'#fffc00'}}},
                ]
            }
        ]
    };
    ;
    if (option && typeof option === "object") {
        myChart.setOption(option, true);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }
});