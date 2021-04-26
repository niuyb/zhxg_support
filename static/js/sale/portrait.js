// 政务事业部 - 销售中心
var departmentPortraitUrl = "/sale/portrait/fuzzy";
var accountActivityUrl = "/sale/account/activity";

Vue.prototype.$echarts = echarts;

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
    if (Id == "g-center-tree"){
        return new Vue({
            el: '#tab-g-center-tree',
            data(){
                return {
                    chartId: "g-center-tree",
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
                    var chart = echarts.init(document.getElementById(this.chartId));
                    chart.on("click", clickFun);
                    chart.hideLoading();
                    if (!this.chartData){
                        chart.showLoading();
                    };
                    chart.setOption(option = {
                        tooltip: {
                            trigger: 'item',
                            triggerOn: 'mousemove',
                            formatter: function(params){
                                return params.data.name;
                            }
                        },
                        series: [
                            {
                                type: 'tree',
                
                                data: [this.chartData],
                
                                top: '10%',
                                left: '1%',
                                bottom: '30%',
                                right: '1%',
                
                                symbolSize: 10,
        
                                orient: 'vertical',
                
                                label: {
                                    position: 'top',
                                    verticalAlign: 'middle',
                                    align: 'center',
                                    // fontSize: 9,
                                    fontSize: 12,
                                    // rotate: -90,
                                },
                
                                leaves: {
                                    label: {
                                        position: 'bottom',
                                        verticalAlign: 'middle',
                                        // align: 'left',
                                        align: 'right',
                                        fontSize: 12,
                                        rotate: 45
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
    }else if (Id == "region-tree"){
        return new Vue({
            el: '#tab-region-tree',
            data(){
                return {
                    chartId: "region-tree",
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
                var url = '/sale/dingding/region/frame/members/api';
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
                    var chart = echarts.init(document.getElementById(this.chartId));
                    chart.on("click", clickFun);
                    chart.hideLoading();
                    if (!this.chartData){
                        chart.showLoading();
                    };
                    chart.setOption(option = {
                        tooltip: {
                            trigger: 'item',
                            triggerOn: 'mousemove',
                            formatter: function(params){
                                return params.data.name;
                            }
                        },
                        series: [
                            {
                                type: 'tree',
                
                                data: [this.chartData],
                
                                top: '10%',
                                left: '1%',
                                bottom: '30%',
                                right: '1%',
                
                                symbolSize: 10,
        
                                orient: 'vertical',
                
                                label: {
                                    position: 'top',
                                    verticalAlign: 'middle',
                                    align: 'center',
                                    // fontSize: 9,
                                    fontSize: 12,
                                    // rotate: -90,
                                },
                
                                leaves: {
                                    label: {
                                        position: 'bottom',
                                        verticalAlign: 'middle',
                                        // align: 'left',
                                        align: 'right',
                                        fontSize: 12,
                                        rotate: 45
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
    }else if (Id == "dpt-tree"){
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
                var url = '/sale/dingding/department/frame/members/api';
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
                    var chart = echarts.init(document.getElementById(this.chartId));
                    chart.on("click", clickFun);
                    chart.hideLoading();
                    if (!this.chartData){
                        chart.showLoading();
                    };
                    chart.setOption(option = {
                        tooltip: {
                            trigger: 'item',
                            triggerOn: 'mousemove',
                            formatter: function(params){
                                return params.data.name;
                            }
                        },
                        series: [
                            {
                                type: 'tree',
                
                                data: [this.chartData],
                
                                top: '10%',
                                left: '1%',
                                bottom: '30%',
                                right: '1%',
                
                                symbolSize: 10,
        
                                orient: 'vertical',
                
                                label: {
                                    position: 'top',
                                    verticalAlign: 'middle',
                                    align: 'center',
                                    // fontSize: 9,
                                    fontSize: 12,
                                    // rotate: -90,
                                },
                
                                leaves: {
                                    label: {
                                        position: 'bottom',
                                        verticalAlign: 'middle',
                                        // align: 'left',
                                        align: 'right',
                                        fontSize: 12,
                                        rotate: 45
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
            data() {
                return {
                    elId: "about-customer",
                    tableData: [],
                    columns: ["total", "formal", "important", "new"],
                    loading: true
                }
            },
            created(){  
                var self = this;
                var did = getUrlKey('did', window.location.href);
                var url = '/sale/customer/count/sale/center/api';
                axios.get(url, {
                    params: {
                        'cid': did
                    }
                }).then(function(res){
                    var columns = self.columns;
                    var item = {};
                    for (var i in columns){
                        item[columns[i]] = res.data.data.data[i];
                    }
                    self.tableData = [item];
                    self.loading = false;
                }).catch(function(err){
                    console.log(err)
                });
            }
        });
    }else if(Id == "work-daily"){
        // var workDailyVue = new Vue({
        return new Vue({
            el: '#work-daily',
            data(){
                return {
                    disabled: false,
                    month: toYearMonthString(),
                    chartId: 'work-daily-chart',
                    chartData: {}
                }
            },
            watch: {
                chartData: 'drawChart',
                month: 'getChartData'
            },
            // created(){
            mounted(){ 
                this.getChartData();
            },
            methods: {
                getChartData(){ 
                    var self = this;
                    var chart = echarts.init(document.getElementById(self.chartId));
                    chart.showLoading();
                    self.disabled = true;
                    var did = getUrlKey('did', window.location.href);
                    var url = '/sale/work/daily/department/api';
                    axios.get(url, {
                        params: {
                            'did': did,
                            date_str: self.month
                        }
                    }).then(function(res){
                        self.chartData = res.data.data;
                        self.disabled = false;
                    }).catch(function(err){
                        console.log(err);
                        self.disabled = false;
                    });
                },
                drawChart(){
                    var chart = echarts.init(document.getElementById(this.chartId));
                    chart.hideLoading();
                    if (!this.chartData){
                        chart.showLoading();
                    };
                    chart.clear();
                    option = {
                        title: {
                            text: "",//this.chartData.title.text,
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
    }else if(Id == "work-daily-saler"){
        // var workDailyVue = new Vue({
        return new Vue({
            el: '#work-daily-saler',
            data(){
                return {
                    elId: 'work-daily-saler',
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
                var uid = getUrlKey('uid', window.location.href);
                var url = '/sale/work/daily/saler/api';
                axios.get(url, {
                    params: {
                        'uid': uid
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
            el: '#goal-regions-month',
            data(){
                return {
                    disabled: false,
                    month: toYearMonthString(),
                    chartId: 'goal-regions-month-chart',
                    chartData: {}
                }
            },
            watch: {
                chartData: 'drawChart',
                month: 'getChartData'
            },
            // created(){
            mounted(){  
                this.getChartData();
            },
            methods: {
                getChartData(){
                    var self = this;
                    var chart = echarts.init(document.getElementById(self.chartId));
                    chart.showLoading();
                    self.disabled = true;
                    var did = getUrlKey('did', window.location.href);
                    var url = "/sale/goal/regions/month/api";
                    axios.get(url, {
                        params: {
                            'did': did,
                            'start': self.month
                        }
                    }).then(function(res){
                        self.chartData = res.data.data;
                        self.disabled = false;
                    }).catch(function(err){
                        console.log(err);
                        self.disabled = false;
                    });
                },
                drawChart(){
                    var chart = echarts.init(document.getElementById(this.chartId));
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
    }else if(Id == "goal-departments-month"){
        // var goalRegionsMonthVue = new Vue({
        return new Vue({
            el: '#tab-goal-departments-month',
            data(){
                return {
                    elId: 'goal-departments-month',
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
                var url = "/sale/goal/departments/month/api";
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
    }else if(Id == "goal-salers-month"){
        // var goalRegionsMonthVue = new Vue({
        return new Vue({
            el: '#tab-goal-salers-month',
            data(){
                return {
                    elId: 'goal-salers-month',
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
                var url = "/sale/goal/salers/month/api";
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
    }else if(Id == "goal-saler-month"){
        // var goalRegionsMonthVue = new Vue({
        return new Vue({
            el: '#goal-saler-month',
            data(){
                return {
                    elId: 'goal-saler-month',
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
                var uid = getUrlKey('uid', window.location.href);
                var url = "/sale/goal/saler/month/api";
                axios.get(url, {
                    params: {
                        'uid': uid
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
    }else if(Id == "about-salers-work-daily"){
        // var accountYqmsVue = new Vue({
        return new Vue({
            el: "#about-salers-work-daily",
            data() {
                return {
                    elId: "about-salers-work-daily",
                    tableData: [],
                    departFilters: [],
                    columns: [
                        {field: 'saler', title: '商务', width: '80', titleAlign: 'center', columnAlign: 'center',isResize:true},
                        {field: 'depart', title: '部门', width: '80', titleAlign: 'center', columnAlign: 'center',isResize:true},
                        {field: 'call', title: '电话拜访', width: '80', titleAlign: 'center', columnAlign: 'center',isResize:true},
                        {field: 'visit', title: '签到拜访', width: '80', titleAlign: 'center', columnAlign: 'center',isResize:true},
                        {field: 'record', title: '快速记录', width: '80', titleAlign: 'center', columnAlign: 'left',isResize:true},
                        {field: 'total', title: '拜访总数', width: '80', titleAlign: 'center', columnAlign: 'left', isResize:true}
                    ],
                    loading: true
                }
            },
            created(){  
                var self = this;
                var did = getUrlKey('did', window.location.href);
                var url = '/sale/work/daily/department/salers/api';
                axios.get(url, {
                    params: {
                        'did': did
                    }
                }).then(function(res){
                    self.tableData = res.data.data;
                    self.departFilters = self.getDepartFilters();
                    self.loading = false;
                }).catch(function(err){
                    console.log(err)
                });
            },
            methods: {
                rowStyle({row, rowIndex}){
                    return 'height: 8px';
                },
                filterHandler(value, row, column) {
                    const property = column['property'];
                    return row[property] === value;
                },
                filterDepart(value, row) {
                    return row.departId === value;
                },
                getDepartFilters(){
                    var departFilters = [];
                    var departs = [];
                    var js = {};
                    for (var i in this.tableData){
                        var c = this.tableData[i];
                        js[c.depart] = c.departId;
                    }
                    for (var k in js){
                        departs.push(k);
                    }
                    departs.sort();
                    for (var i in departs){
                        k = departs[i];
                        departFilters.push({text: k, value: js[k]});
                    }
                    return departFilters;
                }
            }
        });
    }else if(Id == "about-account"){
        // var accountYqmsVue = new Vue({
        return new Vue({
            el: "#about-account",
            data() {
                return {
                    elId: "about-account",
                    tableData: [],
                    // {"total": total, "formal": formal, "trial": trial, "stop": stop, "drop": drop,
                    // "week_twice": week_twice, "week": week, "month": month, 
                    // "three_months": three_months, "dead": dead, "trial_three_months_high": trial_three_months_high}
                    // ['总数', '正式', '试用', '停用', '弃用', '周双活', '周活跃', '月活跃', '三月活跃', '零活跃', '试用高活三个月']
                    columns: [
                        {field: 'product', title: '产品', width: '80', titleAlign: 'center', columnAlign: 'center',isResize:true},
                        {field: 'total', title: '总数', width: '80', titleAlign: 'center', columnAlign: 'center',isResize:true},
                        {field: 'formal', title: '正式', width: '80', titleAlign: 'center', columnAlign: 'center',isResize:true},
                        {field: 'trial', title: '试用', width: '80', titleAlign: 'center', columnAlign: 'left',isResize:true},
                        {field: 'stop', title: '停用', width: '80', titleAlign: 'center', columnAlign: 'center',isResize:true},
                        {field: 'drop', title: '弃用', width: '80', titleAlign: 'center', columnAlign: 'center',isResize:true},
                        {field: 'week_twice', title: '周双活', width: '80', titleAlign: 'center', columnAlign: 'center',isResize:true},
                        {field: 'week', title: '周活跃', width: '80', titleAlign: 'center', columnAlign: 'center',isResize:true},
                        {field: 'month', title: '月活跃', width: '80', titleAlign: 'center', columnAlign: 'center',isResize:true},
                        {field: 'three_months', title: '三月活跃', width: '80', titleAlign: 'center', columnAlign: 'center',isResize:true},
                        {field: 'dead', title: '零活跃', width: '80', titleAlign: 'center', columnAlign: 'center',isResize:true},
                        {field: 'trial_three_months_high', title: '试用高活三个月', width: '80', titleAlign: 'center', columnAlign: 'center',isResize:true}
                    ],
                    loading: true
                }
            },
            created(){  
                var self = this;
                var did = getUrlKey('did', window.location.href);
                var url = '/sale/products/account/count/api';
                axios.get(url, {
                    params: {
                        'did': did
                    }
                }).then(function(res){
                    self.tableData = res.data.data.data;
                    self.loading = false;
                }).catch(function(err){
                    console.log(err)
                });
            },
            methods: {
                rowStyle({row, rowIndex}){
                    return {'height': '8px'};
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
        return new Vue({
            el: '#about-opportunity',
            data() {
                return {
                    elId: "about-opportunity",
                    tableData: [],
                    columns: ["total", "new", "no_account", "stop_three_months"],
                    loading: true
                }
            },
            created(){  
                var self = this;
                var did = getUrlKey('did', window.location.href);
                var url = '/sale/opportunity/count/api';
                axios.get(url, {
                    params: {
                        'did': did
                    }
                }).then(function(res){
                    var columns = self.columns;
                    var item = {};
                    for (var i in columns){
                        item[columns[i]] = res.data.data.data[i];
                    }
                    self.tableData = [item];
                    self.loading = false;
                }).catch(function(err){
                    console.log(err)
                });
            }
        });
    }else if(Id == "region-info"){
        return new Vue({
            delimiters: ['[[', ']]'],
            el: '#region-info',
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
            }
        });
    }else if(Id == "saler-info"){
        return new Vue({
            delimiters: ['[[', ']]'],
            el: '#saler-info',
            data(){
                return {
                    "user": {},
                    "saler": {},
                    "depart": {}
                }
            },
            created(){
                var self = this;
                var uid = getUrlKey('uid', window.location.href);
                var url = '/sale/saler/info/api';
                axios.get(url, {
                    params: {
                        'uid': uid
                    }
                }).then(function(res){
                    self.user = res.data.data.user;
                    self.saler = res.data.data.saler;
                    self.depart = res.data.data.depart;
                }).catch(function(err){
                    console.log(err)
                });
            }
        });
    }else if(Id == "department-info"){
        return new Vue({
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
            }
        });
    }else if(Id == "opportunity"){
        // var columns = [
        //     "opportunity_name",
        //     "customer_name", 
        //     "opportunity_money",
        //     "saler_name",
        //     "quzong_ok",
        //     "last_visit"
        // ];
        // return new Vue({
        //     delimiters: ['[[', ']]'],
        //     el: "#tab-opportunity",
        //     data() {
        //         return {
        //             elId: "opportunity",
        //             tableData: [],
        //             departFilters: [],
        //             columns: [
        //                 {field: 'opportunity_name', title: '商机名称', width: '80', titleAlign: 'center', columnAlign: 'center', isResize:true},
        //                 {field: 'customer_name', title: '客户名称', width: '80', titleAlign: 'center', columnAlign: 'center', isResize:true},
        //                 {field: 'opportunity_money', title: '商机金额', width: '80', titleAlign: 'center', columnAlign: 'center', isResize:true},
        //                 {field: 'win_rate', title: '嬴率', width: '80', titleAlign: 'center', columnAlign: 'center', isResize:true},
        //                 {field: 'quzong_ok', title: '区总确认归档', width: '80', titleAlign: 'center', columnAlign: 'center', isResize:true},
        //                 {field: 'last_visit', title: '最近拜访', width: '80', titleAlign: 'center', columnAlign: 'center', isResize:true},
        //                 {field: 'saler_name', title: '商务', width: '80', titleAlign: 'center', columnAlign: 'center', isResize:true}
        //             ],
        //             loading: true
        //         }
        //     },
        //     created(){  
        //         var self = this;
        //         // var did = getUrlKey('did', window.location.href);
        //         // var url = '/sale/opportunity/list/api';
        //         // axios.get(url, {
        //         //     params: {
        //         //         'did': did
        //         //     }
        //         // }).then(function(res){
        //         //     self.tableData = res.data.data;
        //         //     self.departFilters = self.getDepartFilters();
        //         //     self.loading = false;
        //         // }).catch(function(err){
        //         //     console.log(err)
        //         // });
        //         self.tableData = initOpportunities(45);
        //         // self.departFilters = self.getDepartFilters();
        //         self.loading = false;
        //     },
        //     methods: {
        //         rowStyle({row, rowIndex}){
        //             return 'height: 8px';
        //         },
        //         filterHandler(value, row, column) {
        //             const property = column['property'];
        //             return row[property] === value;
        //         },
        //         filterDepart(value, row) {
        //             return row.departId === value;
        //         },
        //         formatNum(row, column){
        //             return toThousands(row.opportunity_money);
        //         },
        //         getDepartFilters(){
        //             var departFilters = [];
        //             var departs = [];
        //             var js = {};
        //             for (var i in this.tableData){
        //                 var c = this.tableData[i];
        //                 js[c.depart] = c.departId;
        //             }
        //             for (var k in js){
        //                 departs.push(k);
        //             }
        //             departs.sort();
        //             for (var i in departs){
        //                 k = departs[i];
        //                 departFilters.push({text: k, value: js[k]});
        //             }
        //             return departFilters;
        //         }
        //     }
        // });
        return initOpportunityVue();
    }else if(Id == "customer"){
        // return new Vue({
        //     delimiters: ['[[', ']]'],
        //     el: "#tab-customer",
        //     data() {
        //         return {
        //             elId: "customer",
        //             tableData: [],
        //             departFilters: [],
        //             columns: [
        //                 {field: 'customer_name', title: '客户名称', width: '80', titleAlign: 'center', columnAlign: 'center', isResize:true},
        //                 {field: 'customer_level', title: '客户级别', width: '80', titleAlign: 'center', columnAlign: 'center', isResize:true},
        //                 {field: 'account_num', title: '账号数量', width: '80', titleAlign: 'center', columnAlign: 'left', isResize:true},
        //                 {field: 'saler_name', title: '商务', width: '80', titleAlign: 'center', columnAlign: 'center', isResize:true},
        //                 {field: 'days_left', title: '服务截止剩余天数', width: '80', titleAlign: 'center', columnAlign: 'left', isResize:true},
        //                 {field: 'last_visit', title: '最近拜访', width: '80', titleAlign: 'center', columnAlign: 'center', isResize:true}
        //             ],
        //             loading: true
        //         }
        //     },
        //     created(){  
        //         var self = this;
        //         var did = getUrlKey('did', window.location.href);
        //         var url = '/sale/customer/list/api';
        //         axios.get(url, {
        //             params: {
        //                 'did': did,
        //                 'page': 1,
        //                 "num": 20
        //             }
        //         }).then(function(res){
        //             self.tableData = res.data.data.data;
        //             self.departFilters = self.getDepartFilters();
        //             self.loading = false;
        //         }).catch(function(err){
        //             console.log(err)
        //         });
        //         // self.tableData = initCustomers(53);
        //         // self.departFilters = self.getDepartFilters();
        //         // self.loading = false;
        //     },
        //     methods: {
        //         rowStyle({row, rowIndex}){
        //             return 'height: 8px';
        //         },
        //         filterHandler(value, row, column) {
        //             const property = column['property'];
        //             return row[property] === value;
        //         },
        //         filterDepart(value, row) {
        //             return row.departId === value;
        //         },
        //         formatNum(row, column){
        //             return toThousands(row.opportunity_money);
        //         },
        //         getDepartFilters(){
        //             var departFilters = [];
        //             var departs = [];
        //             var js = {};
        //             for (var i in this.tableData){
        //                 var c = this.tableData[i];
        //                 js[c.depart] = c.departId;
        //             }
        //             for (var k in js){
        //                 departs.push(k);
        //             }
        //             departs.sort();
        //             for (var i in departs){
        //                 k = departs[i];
        //                 departFilters.push({text: k, value: js[k]});
        //             }
        //             return departFilters;
        //         }
        //     }
        // });
        return initCustomerVue();
    }else if(Id === "saler"){
        return initSalerVue();
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
