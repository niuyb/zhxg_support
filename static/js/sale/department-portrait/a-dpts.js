// achievement-departments

$(function () {
    aDpts();
    function aDpts() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('a-dpts'));
        myChart.clear();
        option = {
            title: {
                text: ''
            },
            tooltip: {
                trigger: 'axis'
            },
            legend: {
                x : 'center',
                y : 'top',
                itemWidth: 8,
                itemHeight: 8,
                textStyle:{//图例文字的样式
                    // color:'#fff',
                    fontSize:12
                },
                data:['计划目标','确认归档','实际完成'],
                // textStyle:{
                //     color: '#fff'
                // },
                // top: '8%'
            },
            grid: {
                top: '20%',
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            },
            xAxis: {
                type: 'category',
                boundaryGap: false,
                data: ['安徽','山东','浙江','江苏'],
                splitLine: {
                    show: false
                },
                axisLine: {
                    // lineStyle: {
                    //     color: '#fff'
                    // }
                }
            },
            yAxis: {
                // name: '亿吨公里',
                type: 'value',
                splitLine: {
                    show: false
                },
                axisLine: {
                    // lineStyle: {
                    //     color: '#fff'
                    // }
                }
            },
            series: [
                {
                    name:'计划目标',
                    type:'line',
                    data:[3961.88, 4233.63, 4183.14, 3633.01]
                },
                {
                    name:'确认归档',
                    type:'bar',
                    barWidth: 5,
                    data:[3374.76, 3364.76, 3274.76, 3371.82]
                },
                {
                    name:'实际完成',
                    type:'bar',
                    barWidth: 5,
                    data:[1400.77, 500.17, 1800.17, 148.56]
                }
            ]
        };
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }
});
