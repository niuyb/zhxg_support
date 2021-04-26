layui.use('layer', function(){ //独立版的layer无需执行这一句
    var $ = layui.jquery, layer = layui.layer; //独立版的layer无需执行这一句
  
    var myChart = echarts.init(document.getElementById('china-map'));
    // 省坐标，因为全国34个省固定不变，写死即可
    var geoCoordMap = {
        '西藏' : [ 91.11, 30.97 ],
        '上海' : [ 121.48, 31.22 ],
        '福建' : [ 118.1, 27.46 ],
        '浙江' : [ 119.96, 29.86 ],
        '广东' : [ 113.23, 24.16 ],
        '山西' : [ 112.03, 38.87 ],
        '云南' : [ 101.73, 25.04 ],
        '辽宁' : [ 123.38, 42.8 ],
        '吉林' : [ 125.35, 44.88 ],
        '江西' : [ 115.89, 28.68 ],
        '海南' : [ 109.51, 20.25 ],
        '广西' : [ 108.74, 24.16 ],
        '内蒙古' : [ 111.65, 42.42 ],
        '四川' : [ 104.06, 31.67 ],
        '陕西' : [ 108.95, 35.27 ],
        '江苏' : [ 119.78, 33.04 ],
        '贵州' : [ 106.71, 27.57 ],
        '北京' : [ 116.46, 41.72 ],
        '新疆' : [ 86.68, 41.77 ],
        '山东' : [ 119, 36.05 ],
        '甘肃' : [ 103.73, 37.03 ],
        '天津' : [ 118, 39.73 ],
        '河南' : [ 113.65, 34.76 ],
        '黑龙江' : [ 127.63, 47.75 ],
        '河北' : [ 115.48, 38.03 ],
        '湖南' : [ 112, 28.21 ],
        '安徽' : [ 117.27, 32.86 ],
        '湖北' : [ 112.31, 31.52 ],
        '青海' : [ 97.31, 37.03 ],
        '重庆' : [ 107.31, 30.52 ],
        '宁夏' : [ 106.31, 38.52 ],
        '香港' : [ 114.31, 23.02 ],
        '澳门' : [ 114.01, 22.52 ],
        '台湾' : [ 120.81, 25.02 ]
    };

    function getRate(a, b){
        if (!a || !b){
            return 0
        }
        return a / b
    }
    function getFormalRate(item){
        return getRate(item.formal_count, item.base_count)
    }
    function getCoverageRate(item){
        return getRate(item.formal_count + item.trial_count, item.base_count)
    }
    var dataDict = {};
    var rawData = [];
    var max1 = 0;
    //后台获取公宣客户基数、正式、试用客户数量
    $.get("/customer/government/industry/coverage/api", function(data) {
        //console.info(data.loginAfternoon[0]);
        //alert(data.province[i]);
        for (let item of data.items) {
            let prov = item.province_name;
            for (let end of ["省", "市", "特别行政区"]){
                if (prov.endsWith(end)){
                    prov = prov.replace(end, "");
                    break
                }
            }
            if (prov.endsWith("自治区")){
                let len = 2;
                if (prov.startsWith("内蒙古")){
                    len = 3;
                }
                prov = prov.substr(0, len);
            }
            if (!dataDict[prov]){
                dataDict[prov] = {}
            }
            if (item.industry2_name == "公安"){
                dataDict[prov]["公安"] = item
            }else if (item.industry2_name == "宣传"){
                dataDict[prov]["宣传"] = item
            }
        }
        // console.log(dataDict);

        for (let prov in geoCoordMap){  
            let row = [];          
            row.push(prov);
            let item = dataDict[prov] || {};
            let g = item["公安"] || {};
            let x = item["宣传"] || {};
            let gr = getFormalRate(g);
            let xr = getFormalRate(x);
            row.push(gr);
            row.push(xr);

            console.log(row);

            rawData.push(row);
        }
        //console.info(rawData);

        //找出数组中的最大值，用来设置柱状图Y轴的最大值
        //新建一个数组，将各个数据都放进去，然后查找最大值
        var arr = [];
        for (i = 0; i < 34; i++) {
            arr.push(rawData[i][1]);
            arr.push(rawData[i][2]);
            // arr.push(rawData[i][3]);
        }
        ;
        //查找数组中最大值

        for (i = 0; i < arr.length; i++) {
            if (max1 < arr[i]) {
                max1 = arr[i];
            }
        }
        ;

    
        //alert(rawData);

        /* ['西藏',91,11,29],
            ['上海',91,11,29],
            ]; */


        //产生地图数据
        function makeMapData(rawData) {
            var mapData = [];
            for (var i = 0; i < rawData.length; i++) {
                var geoCoord = geoCoordMap[rawData[i][0]];
                if (geoCoord) {
                    mapData.push({
                        name : rawData[i][0],
                        value : geoCoord.concat(rawData[i].slice(1))
                    });
                }
            }
            return mapData;
        }
        ;

        option = {
            animation : false,
            tooltip : {
                trigger : 'axis'
            },
            geo : {
                map : 'china',
                roam : true,
                zoom : 1.0, // 地图初始大小
                center : [ 110.366794, 35.400309 ], // 初始中心位置
                label : {
                    emphasis : {
                        show : false,
                        areaColor : '#eee'
                    }
                },
                // 地区块儿颜色
                itemStyle : {
                    normal : {
                        areaColor : '#55C3FC',
                        borderColor : '#fff'
                    },
                    emphasis : {
                        areaColor : '#21AEF8'
                    }
                }
            },
            series : []
        };

        function renderEachCity() {
            var option = {
                xAxis : [],
                yAxis : [],
                grid : [],
                series : [],
                tooltip : {
                    trigger: 'item',
                    axisPointer: {
                        type: 'none'
                    }
                }
            };
            

            echarts.util.each(rawData, function(dataItem, idx) {
                //console.info(idx);
                var geoCoord = geoCoordMap[dataItem[0]];
                var coord = myChart.convertToPixel('geo', geoCoord);
                idx += '';

                inflationData = [];
                for (var k = 1; k < 4; k++) {
                    inflationData.push(dataItem[k])
                }
                ;

                option.xAxis.push({
                    id : idx,
                    gridId : idx,
                    type : 'category',
                    name : dataItem[0],
                    nameLocation : 'middle',
                    nameGap : 3,
                    splitLine : {
                        show : false
                    },
                    axisTick : {
                        show : false
                    },
                    axisLabel : {
                        show : false
                    },
                    axisLine : {
                        onZero : false,
                        lineStyle : {
                            color : '#666'
                        }
                    },
                    // data: xAxisCategory,
                    data : [ '公安', '宣传'],//, '试用' ]
                    z : 100
                });
                option.yAxis.push({
                    id : idx,
                    gridId : idx,
                    splitLine : {
                        show : false
                    },
                    axisTick : {
                        show : false
                    },
                    axisLabel : {
                        show : false
                    },
                    axisLine : {
                        show : false,
                        lineStyle : {
                            color : '#1C70B6'
                        }
                    },
                    splitLine : {
                        show : false
                    },
                    min : 0,
                    max : max1,
                    z : 100
                });
                option.grid.push({
                    id : idx,
                    width : 30,
                    height : 40,
                    left : coord[0] - 15,
                    top : coord[1] - 15,
                    z : 100
                });
                option.series.push({
                    id : idx,
                    type : 'bar',
                    xAxisId : idx,
                    yAxisId : idx,
                    barGap : 0,
                    barCategoryGap : 0,
                    // data: inflationData,
                    data : inflationData,
                    z : 100,
                    itemStyle : {
                        normal : {
                            color : function(params) {
                                // 柱状图每根柱子颜色
                                var colorList = [ 'red', 'yellow' ];//'green', 
                                return colorList[params.dataIndex];
                            }
                        },
                        emphasis : {
                            label : {
                                show : false
                            }
                        }
                    }
                });
                
                
            });
            //console.time('a');
            myChart.setOption(option);
        //console.timeEnd('a');
        }

        setTimeout(renderEachCity, 0);
        // 缩放和拖拽
        function throttle(fn, delay, debounce) {
            var currCall;
            var lastCall = 0;
            var lastExec = 0;
            var timer = null;
            var diff;
            var scope;
            var args;

            delay = delay || 0;

            function exec() {
                lastExec = (new Date()).getTime();
                timer = null;
                fn.apply(scope, args || []);
            }

            var cb = function() {
                currCall = (new Date()).getTime();
                scope = this;
                args = arguments;
                diff = currCall - (debounce ? lastCall : lastExec) - delay;

                clearTimeout(timer);
                if (debounce) {
                    timer = setTimeout(exec, delay);
                }
                else {
                    if (diff >= 0) {
                        exec();
                    }
                    else {
                        timer = setTimeout(exec, -diff);
                    }
                }

                lastCall = currCall;
            };

            return cb;
        }

        var throttledRenderEachCity = throttle(renderEachCity, 0);
        myChart.on('geoRoam', throttledRenderEachCity);
        myChart.setOption(option);

        var divObj;
        
        // 点击显示柱状图
        var index;
        myChart.on('click', function(e) {
            if (e.componentSubType == "bar") {//如果选中柱状图，再弹出
                //多窗口模式，层叠置顶	
                if(!divObj){
                    divObj = document.createElement('div');
                    divObj.id = 'zhuzhuang';
                    $(divObj).css({
                        'width' : 250,
                        'height' : 180
                    }).appendTo('.wrap');
                }
                console.log(divObj);
                zhuZhuangTu(e);
                
                var tanchuTitle;
                //看弹出的是哪个省，获取这个省份名
                for (i = 0; i < 34; i++) {
                    if (e.seriesIndex == i) {
                        tanchuTitle = rawData[i][0];
                    }
                };

            console.log(tanchuTitle);

            //判断index是否存在，如果存在就不用open一个新的，直接更改原有的内容和标题就行
            if(!index){
                    index = layer.open({
                    type: 1, 
                    title: tanchuTitle,
                    id:'lid1',
                    anim: 1,
                    //area: ['250px', '180px'],
                    shade: 0,//遮罩
                    content:$('#zhuzhuang'),
                    //右上角关闭事件
                    cancel: function(){ 
                    
                        $('#zhuzhuang').remove();
                        $('.layui-layer').remove();
                        divObj=null;
                        index=null;
                    }
                });
            }
            
            
            layer.title(tanchuTitle, index);//更改标题
            
                //设置背景透明
                layer.style(index, {
                    backgroundColor: 'rgba(255, 255, 255, 0.5)'
                });
            }
        });
        /* if (e.componentSubType == "bar") {
                // 先清除所有柱状图
                $('.tongJiTu').remove();

                
                // 创建遮挡层
                //creatWrap();
                // 创建柱状图容器
                var divObj = document.createElement('div');
                $(divObj).addClass('tongJiTu');
                divObj.id = 'zhuzhuang';
                var divX = getMousePos()['x'];
                var divY = getMousePos()['y'];
                $(divObj).css({
                    'width' : 250,
                    'height' : 180,
                    'border' : '1px solid #ccc',
                    'position' : 'absolute',
                    'top' : divY,
                    'left' : divX
                }).appendTo('.wrap');
                // 创建柱状图
                zhuZhuangTu(e);
                
            
                // 点击遮挡层消失
                //clearWrap('.zhuzhuang');
            } */ 
        // 获取横纵坐标
        function getMousePos(e) {
            var e = event || window.event;
            var scrollX = document.documentElement.scrollLeft || document.body.scrollLeft;
            var scrollY = document.documentElement.scrollTop || document.body.scrollTop;
            var x = e.pageX || e.clientX + scrollX;
            var y = e.pageY || e.clientY + scrollY;
            // console.log(x,y)
            return {
                'x' : x,
                'y' : y
            };
        }
        // 点击弹出生成柱状图
        function zhuZhuangTu(e) {
            var zhuzhuang = echarts.init(document.getElementById('zhuzhuang'));
            var option = {
                backgroundColor : 'rgba(255,255,255,.5)',
                legend : {
                    data : [ '基数', '正式']//, '试用' ]
                },
                xAxis : [
                    {
                        type : 'category',
                        data : [ '基数', '正式']//, '试用' ]
                    }
                ],
                yAxis : [
                    {
                        splitLine : {
                            show : false
                        },
                        //type: 'value',
                        min : 0,
                        max : max1 + 20
                    }
                ],
                series : [
                    {
                        type : 'bar',
                        itemStyle : {
                            normal : {
                                color : function(params) {
                                    var colorList = [ '#F75D5D', 'yellow' ];//'#59ED4F', 
                                    return colorList[params.dataIndex];
                                },
                                label : {
                                    show : true,
                                    position : 'top',
                                    textStyle : {
                                        color : '#000'
                                    }
                                }
                            }
                        },
                        data : []
                    }
                ]
            };
            zhuzhuang.setOption(option);

            //实时获取后台数据，使每个省点击弹出的都是该省的数据
            var op = zhuzhuang.getOption(); //getOption: 返回内部持有的当前显示option克隆
            for (i = 0; i < 34; i++) {
                if (e.seriesIndex == i) {
                    //alert(e.seriesIndex);
                    op.series[0].data.push(rawData[i][1]);
                    op.series[0].data.push(rawData[i][2]);
                    // op.series[0].data.push(rawData[i][3]);
                }
                zhuzhuang.setOption(op, true);
            };

        }
        // 生成遮挡层
        function creatWrap() {
            var zheDang = document.createElement('div');
            $(zheDang).addClass('zhedang').css({
                width : '100%',
                height : '100%',
                position : 'absolute',
                top : 0,
                left : 0,
                close : true,
                backgroundColor : 'rgba(0,0,0,.2)'
            }).appendTo('.wrap');
        }
        // 去掉遮挡层
        function clearWrap(id) {
            $(id).click(function(e) {
                // console.log(this);
                this.remove();
                $('.zhuzhuang').remove();
                return false;
            });
        }
    });	    
});
