Vue.filter('toThousands', toThousands);

function showChangeFormatter(rowData, index, pagingIndex) {
    var field = this.field;
    let html = rowData[field] == 0 ? '<span style="color:red;font-weight: bold;">' + 0 + '</span>': toThousands(rowData[field]);
    if (rowData.day_confirm_money > 0){

        html += '&nbsp;&nbsp;<i style="color: green;" class="fa fa-long-arrow-up"></i>';
    }else if(rowData.day_confirm_money < 0){
        html += '&nbsp;&nbsp;<i style="color: red;" class="fa fa-long-arrow-down"></i>';
    }
    return html;
}

var app = new Vue({
    el: '#saler-kpi-history',
    delimiters: ["[[", "]]"],
    mixins: [ salerKpiMixin ],
    data() {
        return {
            canExport: $("#can-export").text() == 1,
            showSalerSelector: $("#table-source-api").text().indexOf("history") !== -1,
            showDatePicker: true,
            exporting: false,

            istarshine_id: "",
            date: "",

            changedTime: null,

            // istarshine_id: "",
            salers: [],

            salerInfo: {
                user: {}
            },
            userInfo: {},

            // date: "",
            pageSize: 10,
            tableConfig: {
                columnDict: {
                    "saler": "商务", 
                    "level": "级别",
                    "ownerid": "商务销售易ID",
                    "istarshine_id": "商务智慧星光唯一ID",
                    "hiredate": "入职日期", 
                    "join_days": "入职天数",
                    "department_name": "四级部门",
                    "parent_name": "三级部门",
                    "job_name": "职位",

                    "month_new_goal": "当月新签任务",
                    "month_renew_goal": "当月续签任务",
                    "month_goal": "当月任务",
                    "month_new_performance": "当月新签业绩",
                    "month_renew_performance": "当月续签业绩",
                    "month_performance": "当月业绩",

                    "day_new_performance": "当天新签业绩",
                    "day_renew_performance": "当天续签业绩",
                    "day_performance": "当天业绩",

                    "month_head_confirm_money": "月初承诺值",
                    "month_confirm_money": "当月承诺值",
                    "confirm_goal_rate": "承诺值/任务值",
                    "month_fight_money": "当月争取值",
                    "month_complete_money": "当月完成值",

                    "day_complete_money": "当月完成值",

                    "month_call_num": "当月电话数",
                    "week_call_num": "当周电话数",

                    "day_call_num": "当天电话数",

                    "month_visit_num": "当月出差拜访数",
                    "week_visit_num": "当周出差拜访数",

                    "day_visit_num": "当天出差拜访数",

                    "ms_trial_num": "秘书试用账号数",
                    "ms_month_active_num": "秘书月活数",
                    "ms_month_new_num": "秘书当月新建",
                    "ms_week_new_num": "秘书当周新建",

                    "ms_day_new_num": "秘书当天新建",

                    "ts_trial_num": "态势试用账号数",
                    "ts_month_active_num": "态势月活数",
                    "ts_month_new_num": "态势当月新建",
                    "ts_week_new_num": "态势当周新建",

                    "ts_day_new_num": "态势当天新建",

                    "ctime": "统计日期"
                },
                multipleSort: false,
                tableData: [],
                columns: [{
                    field: 'ctime',
                    width: 100,
                    columnAlign: 'center',
                    isSelect: true,
                    isFrozen: true
                },{
                    field: 'month_confirm_money',
                    width: 120,
                    columnAlign: 'center',
                    isResize: true,
                    formatter: showChangeFormatter
                },{
                    field: 'month_fight_money',
                    width: 100,
                    columnAlign: 'center',
                    isResize: true,
                    formatter: zeroRedFormatter
                },{
                    field: 'month_complete_money',
                    width: 100,
                    columnAlign: 'center',
                    isResize: true,
                    formatter: zeroRedFormatter
                },{
                    field: 'day_complete_money',
                    width: 100,
                    columnAlign: 'center',
                    isResize: true,
                    formatter: zeroRedFormatter
                },{
                    field: 'month_call_num',
                    width: 120,
                    columnAlign: 'center',
                    isSelect: true,
                    formatter: zeroRedFormatter
                },{
                    field: 'day_call_num',
                    width: 120,
                    columnAlign: 'center',
                    isSelect: true,
                    formatter: zeroRedFormatter
                },{
                    field: 'month_visit_num',
                    width: 120,
                    columnAlign: 'center',
                    isSelect: true,
                    formatter: zeroRedFormatter
                },{
                    field: 'day_visit_num',
                    width: 120,
                    columnAlign: 'center',
                    isSelect: true,
                    formatter: zeroRedFormatter
                },{
                    field: 'ms_trial_num',
                    width: 120,
                    columnAlign: 'center',
                    isSelect: true,
                    formatter: zeroRedFormatter
                },{
                    field: 'ms_month_active_num',
                    width: 100,
                    columnAlign: 'center',
                    isSelect: true,
                    formatter: zeroRedFormatter
                },{
                    field: 'ms_month_new_num',
                    width: 120,
                    columnAlign: 'center',
                    isSelect: true,
                    formatter: zeroRedFormatter
                },{
                    field: 'ms_day_new_num',
                    width: 120,
                    columnAlign: 'center',
                    isSelect: true,
                    formatter: zeroRedFormatter
                },{
                    field: 'ts_trial_num',
                    width: 120,
                    columnAlign: 'center',
                    isSelect: true,
                    formatter: zeroRedFormatter
                },{
                    field: 'ts_month_active_num',
                    width: 100,
                    columnAlign: 'center',
                    isSelect: true,
                    formatter: zeroRedFormatter
                },{
                    field: 'ts_month_new_num',
                    width: 120,
                    columnAlign: 'center',
                    isSelect: true,
                    formatter: zeroRedFormatter
                },{
                    field: 'ts_day_new_num',
                    width: 120,
                    columnAlign: 'center',
                    isSelect: true,
                    formatter: zeroRedFormatter
                }],
                titleRows: [[{
                    fields: ['ctime'],
                    title: '统计日期',
                    orderBy: '',
                    titleAlign: 'center',
                    rowspan: 2
                },{
                    fields: ['month_confirm_money', 'month_fight_money', 'month_complete_money', 'day_complete_money'],
                    title: '当月/天商机情况',
                    titleAlign: 'center',
                    colspan: 4,
                    // rowspan: 2
                },{
                    fields: ['month_call_num', 'day_call_num', 'month_visit_num', 'day_visit_num'],
                    title: '当月/天电话、出差情况',
                    titleAlign: 'center',
                    colspan: 4,
                    // rowspan: 2
                },{
                    fields: ['ms_trial_num', 'ms_month_active_num', 'ms_month_new_num', 'ms_day_new_num'],
                    title: '当月/天舆情秘书账号情况',
                    titleAlign: 'center',
                    colspan: 4,
                    // rowspan: 2
                },{
                    fields: ['ts_trial_num', 'ts_month_active_num', 'ts_month_new_num', 'ts_day_new_num'],
                    title: '当月/天态势感知账号情况',
                    titleAlign: 'center',
                    colspan: 4
                }],[{
                    fields: ['month_confirm_money'],
                    title: '当前承诺值',
                    titleAlign: 'center',
                    filterMultiple: false,
                    filters: [{label: "0", value: 0}],
                    orderBy: '',
                    isSearchAble: true,
                    searchType: 'numberRange'
                },{
                    fields: ['month_fight_money'],
                    title: '可争取值',
                    titleAlign: 'center',
                    filterMultiple: false,
                    filters: [{label: "0", value: 0}],
                    orderBy: '',
                    isSearchAble: true,
                    searchType: 'numberRange'
                },{
                    fields: ['month_complete_money'],
                    title: '当月归档',
                    titleAlign: 'center',
                    filterMultiple: false,
                    filters: [{label: "0", value: 0}],
                    orderBy: '',
                    isSearchAble: true,
                    searchType: 'numberRange'
                },{
                    fields: ['day_complete_money'],
                    title: '当天归档',
                    titleAlign: 'center',
                    filterMultiple: false,
                    filters: [{label: "0", value: 0}],
                    orderBy: '',
                    isSearchAble: true,
                    searchType: 'numberRange'
                },{
                    fields: ['month_call_num'],
                    title: '当月电话数',
                    titleAlign: 'center',
                    orderBy: '',
                    filterMultiple: false,
                    filters: [{label: "空", value: ""}],
                    isSearchAble: true,
                    searchType: 'numberRange'
                },{
                    fields: ['day_call_num'],
                    title: '当天电话数',
                    titleAlign: 'center',
                    orderBy: '',
                    filterMultiple: false,
                    filters: [{label: "空", value: ""}],
                    isSearchAble: true,
                    searchType: 'numberRange'
                },{
                    fields: ['month_visit_num'],
                    title: '当月出差数',
                    titleAlign: 'center',
                    orderBy: '',
                    filterMultiple: false,
                    filters: [{label: "空", value: ""}],
                    isSearchAble: true,
                    searchType: 'numberRange'
                },{
                    fields: ['day_visit_num'],
                    title: '当天出差数',
                    titleAlign: 'center',
                    orderBy: '',
                    filterMultiple: false,
                    filters: [{label: "空", value: ""}],
                    isSearchAble: true,
                    searchType: 'numberRange'
                },{
                    fields: ['ms_trial_num'],
                    title: '试用账号数',
                    titleAlign: 'center',
                    orderBy: '',
                    filterMultiple: false,
                    filters: [{label: "0", value: 0}],
                    isSearchAble: true,
                    searchType: "numberRange"
                },{
                    fields: ['ms_month_active_num'],
                    title: '月活跃数',
                    titleAlign: 'center',
                    orderBy: '',
                    filterMultiple: false,
                    filters: [{label: "0", value: 0}],
                    isSearchAble: true,
                    searchType: "numberRange"
                },{
                    fields: ['ms_month_new_num'],
                    title: '当月新建数',
                    titleAlign: 'center',
                    orderBy: '',
                    filterMultiple: false,
                    filters: [{label: "0", value: 0}],
                    isSearchAble: true,
                    searchType: "numberRange"
                },{
                    fields: ['ms_day_new_num'],
                    title: '当天新建数',
                    titleAlign: 'center',
                    orderBy: '',
                    filterMultiple: false,
                    filters: [{label: "0", value: 0}],
                    isSearchAble: true,
                    searchType: "numberRange"
                },{
                    fields: ['ts_trial_num'],
                    title: '试用账号数',
                    titleAlign: 'center',
                    orderBy: '',
                    filterMultiple: false,
                    filters: [{label: "0", value: 0}],
                    isSearchAble: true,
                    searchType: "numberRange"
                },{
                    fields: ['ts_month_active_num'],
                    title: '月活跃数',
                    titleAlign: 'center',
                    orderBy: '',
                    filterMultiple: false,
                    filters: [{label: "0", value: 0}],
                    isSearchAble: true,
                    searchType: "numberRange"
                },{
                    fields: ['ts_month_new_num'],
                    title: '当月新建数',
                    titleAlign: 'center',
                    orderBy: '',
                    filterMultiple: false,
                    filters: [{label: "0", value: 0}],
                    isSearchAble: true,
                    searchType: "numberRange"
                },{
                    fields: ['ts_day_new_num'],
                    title: '当天新建数',
                    titleAlign: 'center',
                    orderBy: '',
                    filterMultiple: false,
                    filters: [{label: "0", value: 0}],
                    isSearchAble: true,
                    searchType: "numberRange"
                }]],
            }
        }
    },
    methods: {
        getIstarshineId(){
            let istarshine_id = getUrlKey("istarshine_id", window.location.href);
            this.istarshine_id = istarshine_id;
        },
        getSalers(){
            let self = this;
            let url = "/sale/saler/list/api";
            axios.get(url).then(res => {
                if (res.data.code === 1){
                    self.salers = res.data.data;
                }else{
                    self.$message.error(res.data.error);
                }
            }).catch(err => {
                self.$message.error(err);
            })
        },
        getUserInfo(){
            let self = this;
            let istarshine_id = self.istarshine_id;
            if (!istarshine_id){
                return
            }

            let url = "/sale/saler/info/api?istarshine_id=" + istarshine_id;
            axios.get(url).then(res => {
                if (res.data.code === 1){
                    self.userInfo = res.data.data;
                }else{
                    self.$message.error(res.data.error);
                }
            }).catch(err => {
                self.$message.error(err);
            })
        },
        getSalerInfo(){
            if (this.sourceTableData && this.sourceTableData.length > 0){ 
                this.salerInfo = this.sourceTableData[0]
            }else{
                let salerInfo = {};
                let ks = ["saler", "level", "hiredate", "join_days", "department_name", "parent_name", "job_name"];
                for (let k of ks){
                    salerInfo[k] = this.salerInfo[k];
                }
                this.salerInfo = salerInfo;
            }
        },
        expt(){
            let self = this;
            self.exporting = true;

            let url = "";
            if (self.showDatePicker){
                url = "/sale/saler/kpi/month/export";
            }
            if (self.showSalerSelector){
                url = "/sale/saler/kpi/history/export";
            }
            
            let params = self.getParams();
            params.fields = "fields=saler,level,ownerid,istarshine_id,hiredate,join_days,department_name,parent_name,job_name," +
            "month_head_confirm_money,month_confirm_money,month_fight_money,month_complete_money,day_complete_money," +
            "month_new_goal,month_renew_goal,month_goal,month_new_performance,month_renew_performance,month_performance," + 
            "day_new_performance,day_renew_performance,day_performance," + 
            "month_call_num,day_call_num,month_visit_num,day_visit_num," + 
            "ms_trial_num,ms_month_active_num,ms_month_new_num,ms_day_new_num," + 
            "ts_trial_num,ts_ month_active_num,ts_month_new_num,ts_day_new_num,ctime";

            url = url + "?" + Qs.stringify(params)
            window.open(url);
            // bg.exporting = false;
            self.exporting = false;
        }
    },
    created() {
        this.getDate();
        this.getIstarshineId();
        if (this.showSalerSelector){
            this.getSalers();
        }
    },
    computed: {
        toGetUserInfo(){
            return this.istarshine_id;
        },
        toGetSourceTableData(){
            if (this.istarshine_id && this.date){
                return this.istarshine_id + "-" + this.date;
            }
            return null
        },
        toInitTable(){
            return this.sourceTableData;
        },
        toGetSalerInfo(){
            return this.sourceTableData;
        }
    },
    watch: {
        "toGetSourceTableData": "getSourceTableData",
        "toGetUserInfo": "getUserInfo",
        "toInitTable": "initTable",
        "toGetSalerInfo": "getSalerInfo",
        // "date": "getSourceTableData",

        // "istarshine_id": "getSourceTableData",
        // "istarshine_id": "getUserInfo",
        // "date": "getSourceTableData",
        // "sourceTableData": "initTable",
        // "sourceTableData": "getSalerInfo"
        // // "customerLevelFilters": "setCustomerLevelFilters",
    }
});

