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
    }
}

$(document).ready(function(){
    // console.log($("ul.nav.nav-tabs li.active a")[0]);
    // $($("ul.nav.nav-tabs li.active a")[0]).click();
    initVue("dpt-tree");
    // initVue("goal-regions-month");
    // initVue("work-daily");
    // initVue("about-account");
    // initVue("about-opportunity");
    // initVue("about-customer");
    // initVue("about-account-yqms");
});
