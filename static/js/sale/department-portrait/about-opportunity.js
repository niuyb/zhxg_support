// about-opportunity

$(function () {
    aboutOpportunity();
    function aboutOpportunity() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('about-opportunity'));
        myChart.clear();
        option = {
            title: {
                text: '',
                textStyle:{//图例文字的样式
                    color:'gray',
                    fontSize:12
                },
            },
            tooltip: {
                trigger: 'axis'
            },
            legend: {
                x : 'right',
                y : 'top',
                itemWidth: 8,
                itemHeight: 8,
                textStyle:{//图例文字的样式
                    // color:'#fff',
                    fontSize:12
                },
                data:['数量'],
                // textStyle:{
                //     color: '#fff'
                // },
                // top: '8%'
            },
            grid: {
                top: '15%',
                left: '3%',
                right: '4%',
                bottom: '3%',
                containLabel: true
            },
            // color: ['#FF4949','#FFA74D','#FFEA51','#4BF0FF','#44AFF0','#4E82FF','#584BFF','#BE4DFF','#F845F1'],
            xAxis: {
                type: 'category',
                boundaryGap: false,
                data: ['总数', '新建', '无账号', '停留三个月'],
                splitLine: {
                    show: false
                },
                axisLine: {
                    // lineStyle: {
                    //     color: '#fff'
                    // }
                },
                axisLabel: {
                    interval:0, //坐标刻度之间的显示间隔，默认就可以了（默认是不重叠）
                    rotate:38   //调整数值改变倾斜的幅度（范围-90到90）
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
                    name:'数量',
                    type:'bar',
                    barWidth: 10,
                    data:[1000, 20, 8, 50]
                }
            ]
        };
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }
});
