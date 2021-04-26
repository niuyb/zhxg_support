// 政务事业部 - 销售中心
var departmentPortraitUrl = "/sale/portrait/fuzzy";
var accountActivityUrl = "/sale/account/activity";

Vue.prototype.$echarts = echarts;

function getUrlKey(name,url){
    return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(url) || [, ""])[1].replace(/\+/g, '%20')) || null
}

function clickFun(param) {
    if (typeof param.seriesIndex == 'undefined') {
        return;
    }
    if (typeof param.value == 'undefined') {
        return;
    }
    if (param.type == 'click') {
        console.log(param);
        var url = departmentPortraitUrl + "?did=" + param.value;
        window.open(url);
    }
}

function toggleFunc(that){
    var h = $(that).attr("href");
    var h = h.replace("#tab-", "");
    setTimeout(function(){
        var chart = echarts.getInstanceByDom(document.getElementById(h));
        if (chart){
            chart.resize();
        }else{
            initVue(h);
        }
    }, 100);
}

function initVue(Id){
    // var dptTree = new Vue({
    if (Id == "dpt-tree"){
        return new Vue({
            el: '#tab-dpt-tree',
            data(){
                return {
                    chartId: "dpt-tree",
                    chartData: {}
                }
            },
            watch: {
                chartData: 'drawChart',
            },
            // created(){
            mounted(){  
                var chart = echarts.init(document.getElementById(this.chartId));
                chart.showLoading();
                var self = this;
                var did = getUrlKey('did', window.location.href);
                // var url = '/sale/crm/department/frame/api';
                var url = '/sale/dingding/department/frame/api';
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
                    var chart = echarts.init(document.getElementById("dpt-tree"));
                    chart.on("click", clickFun);
                    chart.hideLoading();
                    if (!this.chartData){
                        chart.showLoading();
                    };
                    chart.setOption(option = {
                        tooltip: {
                            trigger: 'item',
                            triggerOn: 'mousemove'
                        },
                        series: [
                            {
                                type: 'tree',
                
                                data: [this.chartData],
                
                                top: '20%',
                                left: '1%',
                                bottom: '20%',
                                right: '1%',
                
                                symbolSize: 7,
        
                                orient: 'vertical',
                
                                label: {
                                    position: 'top',
                                    verticalAlign: 'middle',
                                    align: 'right',
                                    fontSize: 15,
                                    rotate: -90
                                },
                
                                leaves: {
                                    label: {
                                        position: 'bottom',
                                        verticalAlign: 'middle',
                                        align: 'left',
                                        rotate: -90
                                    }
                                },
                
                                expandAndCollapse: false,
                                animationDuration: 550,
                                animationDurationUpdate: 750
                            }
                        ]
                    });
                    window.addEventListener("resize", function () {
                        chart.resize();
                    });
                }
            }
        });
    }else if(Id == "about-customer"){
    // var customerVue = new Vue({
        return new Vue({
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
    }else if(Id == "work-daily"){
        // var workDailyVue = new Vue({
        return new Vue({
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
    }else if(Id == "p-r-ds"){
        // var paymentVue = new Vue({
        return new Vue({
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
    }else if(Id == "goal-regions-month"){
        // var goalRegionsMonthVue = new Vue({
        return new Vue({
            el: '#tab-goal-regions-month',
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
    }else if(Id == "about-account-yqms"){
        // var accountYqmsVue = new Vue({
        return new Vue({
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
    }else if(Id == "about-opportunity"){
        // var opportunityVue = new Vue({
        return new Vue({
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
    }    
    
    
    // 舆情秘书点击跳转账号活跃度统计函数
    function clickFuncAcountYqms(param) {
        if (param.type == 'click') {
            var did = getUrlKey('did', window.location.href);
            var url = acountActivityUrl + "?pro=1&type=" + encodeURI(param.name) + "&did=" + did;
            window.open(url);
        }
    }    
}

$(document).ready(function(){
    console.log($("ul.nav.nav-tabs li.active a")[0]);
    $($("ul.nav.nav-tabs li.active a")[0]).click();
});
