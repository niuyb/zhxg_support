$(function () {

    echartChinaMap();

    // echart_map中国地图
    function echartChinaMap() {
        // 基于准备好的dom，初始化echarts实例
        var myChart = echarts.init(document.getElementById('china-map'));

        var mapName = 'china'
        var data = []
        var toolTipData = [];

        /*获取地图数据*/
        myChart.showLoading();
        var mapFeatures = echarts.getMap(mapName).geoJson.features;
        myChart.hideLoading();
        var color = ['#c5f80e'];
        var series = [
            {
                map: 'china', 
                type: 'map',
                maptype: 'china',
                roam: true,   
                // label: {
                //     normal: {
                //         show: true
                //     },
                //     emphasis: {
                //         show: false
                //     }
                // },            
                // itemStyle:{                    
                //     emphasis:{
                //         label:{
                //             show:true
                //         }
                //     }
                // },                // 文本位置修正
                // textFixed: {                   
                //     Alaska: [20, -20]
                // },                
                data:[
                    {
                        name: '北京', value: 4822023, selected: false, itemStyle: { 
                            color: "green"
                        }
                    },
                    {name: '天津', value: 731449, selected: false, itemStyle: {color: "green"}},
                    // {name: '河北', value: 19317568, selected: false, itemStyle: {color: "green"}}
                ]
            }
        ];

        option = {
            // title: {
            //     text: "京津大区",
            // },
            // tooltip: {
            //     trigger: 'item'
            // },
            geo: {
                map: 'china',
                label: {
                    emphasis: {
                        show: false
                    }
                },
                roam: true,
                // itemStyle: {
                //     normal: {
                //         borderColor: 'rgba(147, 235, 248, 1)',
                //         borderWidth: 1,
                //         areaColor: {
                //             type: 'radial',
                //             x: 0.5,
                //             y: 0.5,
                //             r: 0.8,
                //             colorStops: [{
                //                 offset: 0,
                //                 color: 'rgba(175,238,238, 0)' // 0% 处的颜色
                //             }, {
                //                 offset: 1,
                //                 color: 'rgba(47,79,79, .1)' // 100% 处的颜色
                //             }],
                //             globalCoord: false // 缺省为 false
                //         },
                //         shadowColor: 'rgba(128, 217, 248, 1)',
                //         // shadowColor: 'rgba(255, 255, 255, 1)',
                //         shadowOffsetX: -2,
                //         shadowOffsetY: 2,
                //         shadowBlur: 10
                //     },
                //     emphasis: {
                //         areaColor: '#389BB7',
                //         borderWidth: 0
                //     }
                // }
            },
            series: series,
        };

        // 使用刚指定的配置项和数据显示图表。
        myChart.setOption(option);
        window.addEventListener("resize", function () {
            myChart.resize();
        });

    }
    //点击跳转
    // $('#china-map').click(function(){
    //     window.location.href = './page/index.html';
    // });
});
