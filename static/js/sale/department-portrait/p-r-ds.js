// payment-region-days

$(function () {
    pRDs();
    function pRDs() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('p-r-ds'));
        myChart.clear();
        option = {
            title: {
                text: '2020年04月',
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
                data:['计划回款','实际回款'],
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
                data: ['01','02','03','04','05', '06', '07', '08', '09', '10',
                        '11','12','13','14','15', '16', '17', '18', '19', '20',
                        '21','22','23','24','25', '26', '27', '28', '29', '30',],
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
                    name:'计划回款',
                    type:'line',
                    data:[3961.88, 4233.63, 4183.14, 3633.01, 3704.47, 3961.88, 4233.63, 4183.14, 3633.01, 3704.47, 3961.88, 4233.63, 3633.01, 3704.47, 3961.88, 4233.63, 4183.14, 3633.01, 3704.47, 3961.88, 4233.63, 3633.01, 3704.47, 3961.88, 4233.63, 4183.14, 3633.01, 3704.47, 3961.88, 4233.63]
                },
                {
                    name:'实际回款',
                    type:'bar',
                    barWidth: 5,
                    data:[3374.76, 3364.76, 3274.76, 3371.82, 3259.87, 3364.76, 3274.76, 3371.82, 3259.87, 3364.76, 3274.76, 3371.82, 3371.82, 3259.87, 3364.76, 3274.76, 3371.82, 3259.87, 3364.76, 3274.76, 3371.82, 3371.82, 3259.87, 3364.76, 3274.76, 3371.82, 3259.87, 3364.76, 3274.76, 3371.82]
                }
            ]
        };
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });
    }
});
