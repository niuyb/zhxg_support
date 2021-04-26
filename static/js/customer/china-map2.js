
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

function getMap(items, level){
    let map = {};
    for (let item of items){
        let key = level + "_name";
        let loc = item[key];
        if (level == 'province'){
            loc = parseProvince(loc)
        }
        map[loc] = item;
    }
    return map;
}

function getProvinceMap(items){
    return getMap(items, 'province')
}

function getCityMap(items){
    return getMap(items, 'city')
}

function getDistrictMap(items){
    return getMap(items, 'district')
}

function parseProvince(prov){
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
    return prov;
}

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
    
function parseChartData(chartData, level){
    let data = [];
    let key = level + "_name";
    for (let item of chartData){
        let loc = item[key];
        if (level == 'province'){
            loc = parseProvince(loc);
        }
        let fr = (getFormalRate(item) * 100).toFixed(2);
        data.push({name: loc, value: fr});
    }
    return data;
}

function getMaxFr(items){
    let frs = [];
    for (let item of items){
        let fr = getFormalRate(item) * 100;
        frs.push(fr);
    }
    return Math.max(...frs).toFixed(2);
}

function getMaxCr(items){
    crs = [];
    for (let item of items){
        let cr = getCoverageRate(item) * 100;
        crs.push(cr);
    }
    return Math.max(...crs).toFixed(2);
}

function drawChinaMap(Id, title_text, chartData, map){
    if (!map){
        var map = echarts.init(document.getElementById(Id));
    }

    let mapName = 'china';

    // map.showLoading();

    let mapFeatures = echarts.getMap(mapName).geoJson.features;

    // map.hideLoading();

    // let series = [
    //     {
    //         map: 'china',
    //         type: 'map',
    //         maptype: 'china',
    //         roam: true,
    //         data: parseChartData(chartData, 'province')
    //     }
    // ]
    let option = {
        title: {
            text: title_text,
            // subtext: 'Data from www.census.gov',
            // sublink: 'http://www.census.gov/popest/data/datasets.html',
            left: 'center'
        },
        tooltip: {
            trigger: 'item',
            formatter: '{b}'
        },
        visualMap: {
            left: 'right',
            top: 'center',
            min: 0,
            max: getMaxFr(chartData.items),
            inRange: {
                color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
            },
            text: ['高', '低'],           // 文本，默认为数值文本
            calculable: true
        },
        toolbox: {
            show: true,
            //orient: 'vertical',
            left: 'left',
            top: 'top',
            feature: {
                dataView: {readOnly: false},
                restore: {},
                saveAsImage: {}
            }
        },
        series: [
            {
                name: '中国',
                type: 'map',
                mapType: 'china',
                // selectedMode: 'multiple',
                label: {
                    show: true
                },
                data: [
                    {name: '广东', value: 12},
                    {name: '台湾', value: 0}
                ],
                // data: parseChartData(chartData, 'province')
            }
        ]
    };

    map.setOption(option);
    window.addEventListener("resize", function(){
        map.resize();
    });
}

var provCodeMap = {
    '上海': 'shanghai',
	    '河北': 'hebei',
	    '山西': 'shanxi',
	    '内蒙古': 'neimenggu',
	    '辽宁': 'liaoning',
	    '吉林': 'jilin',
	    '黑龙江': 'heilongjiang',
	    '江苏': 'jiangsu',
	    '浙江': 'zhejiang',
	    '安徽': 'anhui',
	    '福建': 'fujian',
	    '江西': 'jiangxi',
	    '山东': 'shandong',
	    '河南': 'henan',
	    '湖北': 'hubei',
	    '湖南': 'hunan',
	    '广东': 'guangdong',
	    '广西': 'guangxi',
	    '海南': 'hainan',
	    '四川': 'sichuan',
	    '贵州': 'guizhou',
	    '云南': 'yunnan',
	    '西藏': 'xizang',
	    '陕西': 'shanxi1',
	    '甘肃': 'gansu',
	    '青海': 'qinghai',
	    '宁夏': 'ningxia',
	    '新疆': 'xinjiang',
	    '北京': 'beijing',
	    '天津': 'tianjin',
	    '重庆': 'chongqing',
	    '香港': 'xianggang',
	    '澳门': 'aomen'
}

function initVue(Id){
    if (Id == "main"){
        return new Vue({
            el: '#' + Id,
            data(){
                return {
                    chartId: Id,
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
                    self.chartData = res.data;
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
                                console.log(params);
                            }
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
    }else if(Id == "police"){
    // var customerVue = new Vue({
        return new Vue({
            el: '#' + Id,
            data(){
                return {
                    elId: Id,
                    title: '公安客户地域覆盖率',
                    chartData: null,
                    provinceData: null,
                    cityData: null,
                    chart: null
                }
            },
            watch: {
                chartData: 'drawChinaMap'
            },
            // created(){
            mounted(){  
                var self = this;
                var chart = echarts.init(document.getElementById(self.elId));
                chart.showLoading();
                self.chart = chart;

                var did = getUrlKey('did', window.location.href);
                var url = "/customer/government/industry/coverage/api?industry2=46";
                // url = "https://geo.datav.aliyun.com/areas_v2/bound/100000_full.json";
                axios.get(url, {}).then(function(res){
                    self.chartData = res.data;
                }).catch(function(err){
                    console.log(err)
                });
            },
            methods: {
                drawChinaMap(){
                    let self = this;
                    var chart = this.chart;
                    if (!chart){
                        chart = echarts.init(document.getElementById(this.elId));
                    }
                    chart.hideLoading();
                    if (!this.chartData){
                        chart.showLoading();
                        return;
                    };
                    chart.clear();
                    let map = getProvinceMap(this.chartData.items);
                    let option = {
                        title: {
                            text: '公安客户地域覆盖率',
                            // subtext: 'Data from www.census.gov',
                            // sublink: 'http://www.census.gov/popest/data/datasets.html',
                            left: 'center'
                        },
                        tooltip: {
                            trigger: 'item',
                            // formatter: '{b}',
                            formatter: function(params){
                                let name = params.name;
                                var val = name + "<br />";
                                let item = map[name];
                                val += "基数：" + item.base_count + "<br />";
                                val += "正式：" + item.formal_count + "<br />";
                                val += "试用：" + item.trial_count + "<br />";
                                val += "占有率：" + (getFormalRate(item) * 100).toFixed(2) + "%<br />";
                                val += "覆盖率：" + (getCoverageRate(item) * 100).toFixed(2) + "%<br />";
                                return val;
                            }
                        },
                        visualMap: {
                            left: 'right',
                            top: 'center',
                            min: 0,
                            max: getMaxFr(this.chartData.items),
                            inRange: {
                                color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
                            },
                            text: ['高', '低'],           // 文本，默认为数值文本
                            calculable: true
                        },
                        toolbox: {
                            show: true,
                            //orient: 'vertical',
                            left: 'left',
                            top: 'top',
                            feature: {
                                dataView: {readOnly: false},
                                restore: {},
                                saveAsImage: {}
                            }
                        },
                        series: [
                            {
                                name: '中国',
                                type: 'map',
                                mapType: 'china',
                                // selectedMode: 'multiple',
                                label: {
                                    show: true
                                },
                                // data: [
                                //     {name: '广东', value: 12},
                                //     {name: '台湾', value: 0}
                                // ],
                                data: parseChartData(self.chartData.items, 'province')
                            }
                        ]
                    };
                
                    chart.setOption(option);
                    window.addEventListener("resize", function(){
                        chart.resize();
                    });

                    chart.on('click', function(params){
                        let prov = params.name;
                        let item = map[prov];

                        if (!item){
                            self.drawChinaMap();
                            return;
                        }

                        self.chart.showLoading();

                        let url = "/customer/government/industry/coverage/api?industry2=46&state=" + item.state_id;
                        
                        axios.get(url, {}).then(function(res){
                            self.provinceData = res.data;
                            self.drawProvinceMap();

                        }).catch(function(err){
                            console.log(err)
                        });
                    });
                },
                drawProvinceMap(){
                    let self = this;
                    let items = this.provinceData.items;
                    let province = items[0].province_name;
                    let prov = parseProvince(province);
                    let provCode = provCodeMap[prov];

                    let chart = this.chart;
                    // chart.clear();
                    let map = getCityMap(items);
                    let option = {
                        title: {
                            text: province + '各市公安客户覆盖率',
                            left: "center"
                        },
                        tooltip: {
                            trigger: 'item',
                            // formatter: '{b}',
                            formatter: function(params){
                                let name = params.name;
                                var val = name + "<br />";
                                let item = map[name];
                                val += "基数：" + item.base_count + "<br />";
                                val += "正式：" + item.formal_count + "<br />";
                                val += "试用：" + item.trial_count + "<br />";
                                val += "占有率：" + (getFormalRate(item) * 100).toFixed(2) + "%<br />";
                                val += "覆盖率：" + (getCoverageRate(item) * 100).toFixed(2) + "%<br />";
                                return val;
                            }
                        },
                        visualMap: {
                            left: 'right',
                            top: 'center',
                            min: 0,
                            max: getMaxFr(items),
                            inRange: {
                                color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
                            },
                            text: ['高', '低'],           // 文本，默认为数值文本
                            calculable: true
                        },
                        toolbox: {
                            show: true,
                            //orient: 'vertical',
                            left: 'left',
                            top: 'top',
                            feature: {
                                dataView: {readOnly: false},
                                restore: {},
                                saveAsImage: {}
                            }
                        },
                        series: [
                            {
                                name: prov,
                                type: 'map',
                                'map': prov,
                                mapType: provCode,
                                // selectedMode: 'multiple',
                                label: {
                                    show: true
                                },
                                // data: [
                                //     {name: '广东', value: 12},
                                //     {name: '台湾', value: 0}
                                // ],
                                data: parseChartData(self.provinceData.items, 'city')
                            }
                        ]
                    };
                
                    chart.setOption(option);
                    chart.hideLoading();
                    // window.addEventListener("resize", function(){
                    //     chart.resize();
                    // });
                    // chart.on('click', self.drawChinaMap);
                }
            }
        });
    }else if(Id == "internet"){
        // var workDailyVue = new Vue({
        return new Vue({
            el: '#' + Id,
            data(){
                return {
                    elId: Id,
                    chartData: {},
                    chart: null
                }
            },
            watch: {
                chartData: 'drawChinaMap'
            },
            // created(){
            mounted(){  
                var self = this;
                var chart = echarts.init(document.getElementById(self.elId));
                chart.showLoading();
                this.chart = chart;
                
                var did = getUrlKey('did', window.location.href);
                var url = "/customer/government/industry/coverage/api?industry2=14";
                axios.get(url, {
                    // params: {
                    //     'did': did
                    // }
                }).then(function(res){
                    self.chartData = res.data;
                }).catch(function(err){
                    console.log(err)
                });
            },
            methods: {
                drawChinaMap(){
                    let self = this;
                    var chart = this.chart;
                    if (!chart){
                        chart = echarts.init(document.getElementById(this.elId));
                    }
                    
                    chart.hideLoading();
                    if (!this.chartData){
                        chart.showLoading();
                    };
                    chart.clear();

                    let map = getProvinceMap(this.chartData.items);
                    let option = {
                        title: {
                            text: '宣传客户地域覆盖率',
                            // subtext: 'Data from www.census.gov',
                            // sublink: 'http://www.census.gov/popest/data/datasets.html',
                            left: 'center'
                        },
                        tooltip: {
                            trigger: 'item',
                            // formatter: '{b}',
                            formatter: function(params){
                                let name = params.name;
                                var val = name + "<br />";
                                let item = map[name];
                                val += "基数：" + item.base_count + "<br />";
                                val += "正式：" + item.formal_count + "<br />";
                                val += "试用：" + item.trial_count + "<br />";
                                val += "占有率：" + (getFormalRate(item) * 100).toFixed(2) + "%<br />";
                                val += "覆盖率：" + (getCoverageRate(item) * 100).toFixed(2) + "%<br />";
                                return val;
                            }
                        },
                        visualMap: {
                            left: 'right',
                            top: 'center',
                            min: 0,
                            max: getMaxFr(this.chartData.items),
                            inRange: {
                                color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
                            },
                            text: ['高', '低'],           // 文本，默认为数值文本
                            calculable: true
                        },
                        toolbox: {
                            show: true,
                            //orient: 'vertical',
                            left: 'left',
                            top: 'top',
                            feature: {
                                dataView: {readOnly: false},
                                restore: {},
                                saveAsImage: {}
                            }
                        },
                        series: [
                            {
                                name: '中国',
                                type: 'map',
                                mapType: 'china',
                                // selectedMode: 'multiple',
                                label: {
                                    show: true
                                },
                                // data: [
                                //     {name: '广东', value: 12},
                                //     {name: '台湾', value: 0}
                                // ],
                                data: parseChartData(self.chartData.items, 'province')
                            }
                        ]
                    };
                    
                    chart.setOption(option);
                    window.addEventListener("resize", function () {
                        chart.resize();
                    });

                    chart.on('click', function(params){
                        let prov = params.name;
                        let item = map[prov];

                        if (!item){
                            self.drawChinaMap();
                            return;
                        }

                        self.chart.showLoading();

                        let url = "/customer/government/industry/coverage/api?industry2=46&state=" + item.state_id;
                        
                        axios.get(url, {}).then(function(res){
                            self.provinceData = res.data;
                            self.drawProvinceMap();

                        }).catch(function(err){
                            console.log(err)
                        });
                    });
                },
                drawProvinceMap(){
                    let self = this;
                    let items = this.provinceData.items;
                    let province = items[0].province_name;
                    let prov = parseProvince(province);
                    let provCode = provCodeMap[prov];

                    let chart = this.chart;
                    // chart.clear();
                    let map = getCityMap(items);
                    let option = {
                        title: {
                            text: province + '各市宣传客户覆盖率',
                            left: "center"
                        },
                        tooltip: {
                            trigger: 'item',
                            // formatter: '{b}',
                            formatter: function(params){
                                let name = params.name;
                                var val = name + "<br />";
                                let item = map[name];
                                val += "基数：" + item.base_count + "<br />";
                                val += "正式：" + item.formal_count + "<br />";
                                val += "试用：" + item.trial_count + "<br />";
                                val += "占有率：" + (getFormalRate(item) * 100).toFixed(2) + "%<br />";
                                val += "覆盖率：" + (getCoverageRate(item) * 100).toFixed(2) + "%<br />";
                                return val;
                            }
                        },
                        visualMap: {
                            left: 'right',
                            top: 'center',
                            min: 0,
                            max: getMaxFr(items),
                            inRange: {
                                color: ['#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf', '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
                            },
                            text: ['高', '低'],           // 文本，默认为数值文本
                            calculable: true
                        },
                        toolbox: {
                            show: true,
                            //orient: 'vertical',
                            left: 'left',
                            top: 'top',
                            feature: {
                                dataView: {readOnly: false},
                                restore: {},
                                saveAsImage: {}
                            }
                        },
                        series: [
                            {
                                name: prov,
                                type: 'map',
                                'map': prov,
                                mapType: provCode,
                                // selectedMode: 'multiple',
                                label: {
                                    show: true
                                },
                                // data: [
                                //     {name: '广东', value: 12},
                                //     {name: '台湾', value: 0}
                                // ],
                                data: parseChartData(self.provinceData.items, 'city')
                            }
                        ]
                    };
                
                    chart.setOption(option);
                    chart.hideLoading();
                    // window.addEventListener("resize", function(){
                    //     chart.resize();
                    // });
                    // chart.on('click', self.drawChinaMap);
                }
            }
        });
    }  
}

$(document).ready(function(){
    // console.log($("ul.nav.nav-tabs li.active a")[0]);
    $($("ul.nav.nav-tabs li.active a")[0]).click();
});
