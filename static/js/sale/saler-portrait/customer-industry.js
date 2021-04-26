$(function() {
    var dom = document.getElementById("customer-industry");
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
            data:['公安','宣传','教育','其他']
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
                radius : [30, 80],
                center : ['50%', '60%'],
                roseType : 'area',
                data:[
                    {value:56, name:'公安'},//,itemStyle:{normal:{color:'#ff7800'}}},
                    {value:307, name:'宣传'},//,itemStyle:{normal:{color:'#23eb6a'}}},
                    {value:69, name:'教育'},//,itemStyle:{normal:{color:'#7627cb'}}},
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