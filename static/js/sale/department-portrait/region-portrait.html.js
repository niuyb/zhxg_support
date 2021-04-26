
var departmentPortraitUrl = "/sale/portrait/department";
var accountActivityUrl = "/sale/account/activity";

Vue.prototype.$echarts = echarts;

function getUrlKey(name,url){
    return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(url) || [, ""])[1].replace(/\+/g, '%20')) || null
}

var cmp = new Vue({
    el: '#china-map',
    data() {
        return {seriesData: []}
    },
    watch: {
        seriesData: 'drawChinaMap'
    },
    methods: {
        drawChinaMap(){
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
                    data: this.seriesData
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
                },
                series: series,
            };
            // 使用刚指定的配置项和数据显示图表。
            myChart.setOption(option);
            window.addEventListener("resize", function () {
                myChart.resize();
            });
        }
    }
})

var dpt = new Vue({
    delimiters: ['[[', ']]'],
    el: '#department-info',
    data(){
        return {
            "department": {
                "name": "",
                "level": null,
                "manager": {},
                "children": []
            }
        }
    },
    watch: {
        department: 'drawChinaMap'
    },
    created(){
        var self = this;
        var did = getUrlKey('did', window.location.href);
        var url = '/sale/department/info/api';
        axios.get(url, {
            params: {
                'did': did
            }
        }).then(function(res){
            self.department = res.data.data.department;
        }).catch(function(err){
            console.log(err)
        });
    },
    methods: {
        drawChinaMap(){
            var seriesData = [];
            for (i in this.department.children){
                var child = this.department.children[i];
                sery = {name: child.name, value: child.value, selected: false, itemStyle: {color: "green"}};
                seriesData.push(sery);
            }
            cmp.seriesData = seriesData;
        }
    }
})

function clickFun(param) {
    if (typeof param.seriesIndex == 'undefined') {
        return;
    }
    if (typeof param.value == 'undefined') {
        return;
    }
    if (param.type == 'click') {
        var url = departmentPortraitUrl + "?did=" + param.value;
        window.open(url);
    }
}

var customerVue = new Vue({
    el: '#about-customer',
    data(){
        return {
            elId: 'about-customer',
            chartData: {}
        }
    },
    watch: {
        chartData: 'drawChart'
    },
    // created(){
    mounted(){  
        var self = this;
        var chart = echarts.init(document.getElementById(self.elId));
        chart.showLoading();
        var did = getUrlKey('did', window.location.href);
        var url = '/sale/customer/count/sale/center/api';
        axios.get(url, {
            params: {
                'cid': did
            }
        }).then(function(res){
            self.chartData = res.data.data;
        }).catch(function(err){
            console.log(err)
        });
    },
    methods: {
        drawChart(){
            var chart = echarts.init(document.getElementById(this.elId));
            chart.hideLoading();
            if (!this.chartData){
                chart.showLoading();
            };
            chart.clear();
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
                    // data: ['总数', '正式', '重点', '新开发', '周双活', '周活跃', '月活跃', '三月活跃', '试用高活三个月', '公海池活跃', '零活跃'],
                    data: ['总数', '正式', '重点', '新开发'], //'公海池活跃'],
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
                        "label": {
                            "normal": {
                                "show": true,
                                "position": "top"
                            }
                        },
                        name:'数量',
                        type:'bar',
                        barWidth: 10,
                        data: this.chartData.data
                    }
                ]
            };
            chart.setOption(option);
            window.addEventListener("resize", function () {
                chart.resize();
            });
        }
    }
});

var workDailyVue = new Vue({
    el: '#work-daily',
    data(){
        return {
            elId: 'work-daily',
            chartData: {}
        }
    },
    watch: {
        chartData: 'drawChart'
    },
    // created(){
    mounted(){  
        var self = this;
        var chart = echarts.init(document.getElementById(self.elId));
        chart.showLoading();
        var did = getUrlKey('did', window.location.href);
        var url = '/sale/work/daily/department/api';
        axios.get(url, {
            params: {
                'did': did
            }
        }).then(function(res){
            self.chartData = res.data.data;
        }).catch(function(err){
            console.log(err)
        });
    },
    methods: {
        drawChart(){
            var chart = echarts.init(document.getElementById(this.elId));
            chart.hideLoading();
            if (!this.chartData){
                chart.showLoading();
            };
            chart.clear();
            option = {
                title: {
                    text: this.chartData.title.text,
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
                    data:['电话拜访', '签到拜访', '快速记录'],
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
                    data: this.chartData.date_str_list,
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
                        "label": {
                            "normal": {
                                "show": true,
                                "position": "top"
                            }
                        },
                        name:'电话拜访',
                        type:'line',
                        data: this.chartData.series.a
                    },
                    {
                        "label": {
                            "normal": {
                                "show": true,
                                "position": "top"
                            }
                        },
                        name:'签到拜访',
                        type:'line',
                        data: this.chartData.series.b
                    },
                    {
                        "label": {
                            "normal": {
                                "show": true,
                                "position": "top"
                            }
                        },
                        name:'快速记录',
                        type:'line',
                        data: this.chartData.series.c
                    }
                ]
            };
            chart.setOption(option);
            window.addEventListener("resize", function () {
                chart.resize();
            });
        }
    }
});

var paymentVue = new Vue({
    el: '#p-r-ds',
    data(){
        return {
            elId: 'p-r-ds',
            chartData: {}
        }
    },
    watch: {
        chartData: 'drawChart'
    },
    // created(){
    mounted(){  
        var self = this;
        var chart = echarts.init(document.getElementById(self.elId));
        chart.showLoading();
        var did = getUrlKey('did', window.location.href);
        var url = '/sale/payment/department/days/api';
        axios.get(url, {
            params: {
                'did': did
            }
        }).then(function(res){
            self.chartData = res.data.data;
        }).catch(function(err){
            console.log(err)
        });
    },
    methods: {
        drawChart(){
            var chart = echarts.init(document.getElementById(this.elId));
            chart.hideLoading();
            if (!this.chartData){
                chart.showLoading();
            };
            chart.clear();
            var option = this.chartData;
            chart.setOption(option);
            window.addEventListener("resize", function () {
                chart.resize();
            });
        }
    }
});

var goalRegionsMonthVue = new Vue({
    el: '#goal-regions-month',
    data(){
        return {
            elId: 'goal-regions-month',
            chartData: {}
        }
    },
    watch: {
        chartData: 'drawChart'
    },
    // created(){
    mounted(){  
        var self = this;
        var chart = echarts.init(document.getElementById(self.elId));
        chart.showLoading();
        var did = getUrlKey('did', window.location.href);
        var url = "/sale/goal/regions/month/api";
        axios.get(url, {
            params: {
                'did': did
            }
        }).then(function(res){
            self.chartData = res.data.data;
        }).catch(function(err){
            console.log(err)
        });
    },
    methods: {
        drawChart(){
            var chart = echarts.init(document.getElementById(this.elId));
            chart.hideLoading();
            if (!this.chartData){
                chart.showLoading();
            };
            chart.clear();
            var option = this.chartData;
            chart.setOption(option);
            window.addEventListener("resize", function () {
                chart.resize();
            });
        }
    }
});

// 舆情秘书点击跳转账号活跃度统计函数
function clickFuncAcountYqms(param) {
    if (param.type == 'click') {
        var did = getUrlKey('did', window.location.href);
        var url = acountActivityUrl + "?pro=1&type=" + encodeURI(param.name) + "&did=" + did;
        window.open(url);
    }
}

var accountYqmsVue = new Vue({
    el: "#about-account-yqms",
    data (){
        return {
            elId: "about-account-yqms",
            chartData: {}
        }
    },
    watch: {
        chartData: "drawChart"
    },
    // created(){
    mounted(){  
        var self = this;
        var chart = echarts.init(document.getElementById(self.elId));
        chart.showLoading();
        var did = getUrlKey('did', window.location.href);
        var url = '/sale/account/count/api';
        axios.get(url, {
            params: {
                'did': did,
                'pro': 'yqms'
            }
        }).then(function(res){
            self.chartData = res.data.data;
        }).catch(function(err){
            console.log(err)
        });
    },
    methods: {
        drawChart(){
            var chart = echarts.init(document.getElementById(this.elId));
            chart.on("click", clickFuncAcountYqms);
            chart.hideLoading();
            if (!this.chartData){
                chart.showLoading();
            };
            chart.clear();
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
                    data: ['总数', '正式', '试用', '停用', '弃用', '周双活', '周活跃', '月活跃', '三月活跃', '零活跃', '试用高活三个月'],
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
                        "label": {
                            "normal": {
                                "show": true,
                                "position": "top"
                            }
                        },
                        name:'数量',
                        type:'bar',
                        barWidth: 10,
                        // data:[541, 213, 8, 12, 20, 30, 198, 320, 500, 41, 200]
                        data: this.chartData.data
                    }
                ]
            };
            chart.setOption(option);
            window.addEventListener("resize", function () {
                chart.resize();
            });
        }
    }
});

var opportunityVue = new Vue({
    el: "#about-opportunity",
    data (){
        return {
            elId: "about-opportunity",
            chartData: {}
        }
    },
    watch: {
        chartData: "drawChart"
    },
    // created(){
    mounted(){  
        var self = this;
        var chart = echarts.init(document.getElementById(self.elId));
        chart.showLoading();
        var did = getUrlKey('did', window.location.href);
        var url = '/sale/opportunity/count/api';
        axios.get(url, {
            params: {
                'did': did
            }
        }).then(function(res){
            self.chartData = res.data.data;
        }).catch(function(err){
            console.log(err)
        });
    },
    methods: {
        drawChart(){
            var chart = echarts.init(document.getElementById(this.elId));
            chart.hideLoading();
            if (!this.chartData){
                chart.showLoading();
            };
            chart.clear();
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
                        "label": {
                            "normal": {
                                "show": true,
                                "position": "top"
                            }
                        },
                        name:'数量',
                        type:'bar',
                        barWidth: 10,
                        data: this.chartData.data
                    }
                ]
            };
            chart.setOption(option);
            window.addEventListener("resize", function () {
                chart.resize();
            });
        }
    }
});
