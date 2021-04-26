function arrowFormatter(rowData, index, pagingIndex) {
    let a = rowData["month_head_confirm_money"];
    let b = rowData["month_confirm_money"];
    let html = b == 0 ? '<span style="color:red;font-weight: bold;">' + 0 + '</span>': toThousands(b);
    if (b < a){
        html += "&nbsp;&nbsp;<i class='fa fa-long-arrow-down' style='color: red;'></i>";
    }else if(b > a){
        html += "&nbsp;&nbsp;<i class='fa fa-long-arrow-up' style='color: green;'></i>";
    }
    return html;
}

var app = new Vue({
    el: '#saler-kpi-month',
    delimiters: ["[[", "]]"],
    mixins: [ salerKpiMixin ],
    data() {
        return {
            canExport: $("#can-export").text() == 1,
            showDatePicker: $("#table-source-api").text().indexOf("month") !== -1,

            istarshine_id: "",
            salers: [],

            date: "",
            pickerOptions: {
              disabledDate(time) {
                return time.getTime() > Date.now();
              },
              shortcuts: [{
                text: '今天',
                onClick(picker) {
                  picker.$emit('pick', new Date());
                }
              }, {
                text: '昨天',
                onClick(picker) {
                  const date = new Date();
                  date.setTime(date.getTime() - 3600 * 1000 * 24);
                  picker.$emit('pick', date);
                }
              }, {
                text: '一周前',
                onClick(picker) {
                  const date = new Date();
                  date.setTime(date.getTime() - 3600 * 1000 * 24 * 7);
                  picker.$emit('pick', date);
                }
              }]
            },

            conditions: {},

            filters: {},
            searchers: {},

            loading: true,
            needRetry: false,
            total: 0,
            pageIndex: 1,
            pageSize: 20,
            sourceTableData: [],
            tableData: [],
            footer: [],
            tableConfig: {
                columnDict: {
                    "saler": "商务", 
                    "ownerid": "商务销售易ID",
                    "istarshine_id": "商务智慧星光唯一ID",
                    "hiredate": "入职日期", 
                    "join_days": "入职天数",
                    "department_name": "四级部门",
                    "parent_name": "三级部门",
                    "job_name": "职位",

                    "month_new_goal": "当月新签任务",
                    "month_new_performance": "当月新签业绩",
                    "month_new_rate": "当月新签完成率",

                    "month_renew_goal": "当月续签任务",
                    "month_renew_performance": "当月续签业绩",
                    "month_renew_rate": "当月续签完成率",

                    "month_goal": "当月任务",
                    "month_performance": "当月业绩",
                    "month_rate": "当月完成率",

                    "month_head_confirm_money": "月初承诺值",
                    "month_confirm_money": "当月承诺值",
                    "confirm_goal_rate": "承诺值/任务值",
                    "month_fight_money": "当月争取值",
                    "month_complete_money": "当月完成值",

                    "month_call_num": "当月电话数",
                    "week_call_num": "当周电话数",

                    "month_visit_num": "当月出差拜访数",
                    "week_visit_num": "当周出差拜访数",

                    "ms_trial_num": "秘书试用账号数",
                    "ms_month_active_num": "秘书月活数",
                    "ms_month_new_num": "秘书当月新建",
                    "ms_week_new_num": "秘书当周新建",

                    "ts_trial_num": "态势试用账号数",
                    "ts_month_active_num": "态势月活数",
                    "ts_month_new_num": "态势当月新建",
                    "ts_week_new_num": "态势当周新建",

                    "ctime": "统计日期"
                },
                multipleSort: false,
                tableData: [],
                columns: [{
                    field: 'custome',
                    width: 80,
                    titleAlign: 'center',
                    columnAlign: 'center',
                    formatter: function(rowData, index, pagingIndex) {
                        var currentIndex = index + pagingIndex;
                        return currentIndex + 1
                        // return currentIndex < 3 ? '<span style="color:red;font-weight: bold;">' + (currentIndex + 1) + '</span>': currentIndex + 1
                    },
                    isFrozen: true
                },{
                    field: 'saler',
                    width: 100,
                    columnAlign: 'center',
                    isFrozen: true,
                    isResize: true,
                    formatter: function(rowData, index, pagingIndex){
                        let field = this.field;
                        return '<a href="/sale/saler/kpi/history?istarshine_id=' 
                                + rowData["istarshine_id"] 
                                + '">' 
                                + rowData[field]
                                + '</a>'
                    }
                },{
                    field: 'level',
                    width: 100,
                    columnAlign: 'center',
                    isResize: true
                },{
                    field: 'hiredate',
                    width: 100,
                    columnAlign: 'center',
                    isResize: true
                },{
                    field: 'join_days',
                    width: 100,
                    columnAlign: 'center',
                    isResize: true
                },{
                    field: 'parent_name',
                    width: 100,
                    columnAlign: 'center',
                    isResize: true
                },{
                    field: 'department_name',
                    width: 100,
                    columnAlign: 'center',
                    isResize: true
                },{
                    field: 'month_new_goal',
                    width: 100,
                    columnAlign: 'center',
                    isResize: true,
                    formatter: zeroRedFormatter
                },{
                    field: 'month_new_performance',
                    width: 100,
                    columnAlign: 'center',
                    isResize: true,
                    formatter: zeroRedFormatter
                },{
                    field: 'month_new_rate',
                    width: 120,
                    columnAlign: 'center',
                    isResize: true,
                    formatter: simpleRateFormatter
                },{
                    field: 'month_renew_goal',
                    width: 100,
                    columnAlign: 'center',
                    isResize: true,
                    formatter: zeroRedFormatter
                },{
                    field: 'month_renew_performance',
                    width: 100,
                    columnAlign: 'center',
                    isResize: true,
                    formatter: zeroRedFormatter
                },{
                    field: 'month_renew_rate',
                    width: 120,
                    columnAlign: 'center',
                    isResize: true,
                    formatter: simpleRateFormatter
                },{
                    field: 'month_goal',
                    width: 100,
                    columnAlign: 'center',
                    isResize: true,
                    formatter: zeroRedFormatter
                },{
                    field: 'month_performance',
                    width: 100,
                    columnAlign: 'center',
                    isResize: true,
                    formatter: zeroRedFormatter
                },{
                    field: 'month_rate',
                    width: 150,
                    columnAlign: 'center',
                    isResize: true,
                    formatter: simpleRateFormatter
                },{
                    field: 'month_head_confirm_money',
                    width: 120,
                    columnAlign: 'center',
                    isResize: true,
                    formatter: zeroRedFormatter
                },{
                    field: 'month_confirm_money',
                    width: 120,
                    columnAlign: 'center',
                    isResize: true,
                    formatter: arrowFormatter
                },{
                    field: 'confirm_goal_rate',
                    width: 150,
                    columnAlign: 'center',
                    isResize: true,
                    // formatter: confirmGoalRateFormatter,
                    formatter: simpleRateFormatter
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
                    field: 'month_call_num',
                    width: 100,
                    columnAlign: 'center',
                    isSelect: true,
                    formatter: zeroRedFormatter
                },{
                    field: 'month_visit_num',
                    width: 100,
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
                    width: 100,
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
                    width: 100,
                    columnAlign: 'center',
                    isSelect: true,
                    formatter: zeroRedFormatter
                },{
                    field: 'ctime',
                    width: 100,
                    columnAlign: 'center',
                    isSelect: true
                }],
                titleRows: [[{
                    fields: ['custome'],
                    title: '序号',
                    titleAlign: 'center',
                    rowspan: 2
                },{
                    fields: ['saler'],
                    title: '商务',
                    titleAlign: 'center',
                    filterMultiple: true,
                    filters: [{label: "空", value: ""}],
                    isSearchAble: true,
                    searchType: "string",
                    rowspan: 2
                },{
                    fields: ['level', 'hiredate', 'join_days', 'parent_name', 'department_name'],
                    title: '基本信息',
                    titleAlign: 'center',
                    colspan: 5,
                    // rowspan: 2
                },{
                    fields: ['month_new_goal', 'month_new_performance', 'month_new_rate', 
                            'month_renew_goal', 'month_renew_performance', 'month_renew_rate', 
                            'month_goal', 'month_performance', 'month_rate'],
                    title: '当月任务、业绩情况',
                    titleAlign: 'center',
                    colspan: 9,
                    // rowspan: 2
                },{
                    fields: ['month_head_confirm_money', 'month_confirm_money', 'confirm_goal_rate', 'month_fight_money', 'month_complete_money'],
                    title: '当月商机情况',
                    titleAlign: 'center',
                    colspan: 5,
                    // rowspan: 2
                },{
                    fields: ['month_call_num', 'month_visit_num'],
                    title: '当月电话、出差情况',
                    titleAlign: 'center',
                    colspan: 2,
                    // rowspan: 2
                },{
                    fields: ['ms_trial_num', 'ms_month_active_num', 'ms_month_new_num'],
                    title: '当月舆情秘书账号情况',
                    titleAlign: 'center',
                    colspan: 3,
                    // rowspan: 2
                },{
                    fields: ['ts_trial_num', 'ts_month_active_num', 'ts_month_new_num'],
                    title: '当月态势感知账号情况',
                    titleAlign: 'center',
                    colspan: 3
                },{
                    fields: ['ctime'],
                    title: '统计日期',
                    orderBy: '',
                    titleAlign: 'center',
                    rowspan: 2
                }],[{
                    fields: ['level'],
                    title: '级别',
                    titleAlign: 'center',
                    orderBy: '',
                    filterMultiple: true,
                    filters: [{label: "空", value: ""}],
                    isSearchAble: true,
                    searchType: "number"
                },{
                    fields: ['hiredate'],
                    title: '入职日期',
                    titleAlign: 'center',
                    orderBy: '',
                    filterMultiple: true,
                    filters: [{label: "空", value: ""}],
                    isSearchAble: true,
                    searchType: "dateRange"
                },{
                    fields: ['join_days'],
                    title: '入职天数',
                    titleAlign: 'center',
                    orderBy: '',
                    filterMultiple: true,
                    filters: [{label: "0", value: 0}],
                    isSearchAble: true,
                    searchType: "numberRange"
                },{
                    fields: ['parent_name'],
                    title: '三级部门',
                    titleAlign: 'center',
                    filterMultiple: true,
                    filters: [{label: "空", value: ""}],
                    isSearchAble: true,
                    searchType: "string"
                },{
                    fields: ['department_name'],
                    title: '四级部门',
                    titleAlign: 'center',
                    filterMultiple: true,
                    filters: [{label: "空", value: ""}],
                    isSearchAble: true,
                    searchType: "string"
                },{
                    fields: ['month_new_goal'],
                    title: '新签任务',
                    titleAlign: 'center',
                    orderBy: '',
                    filterMultiple: false,
                    filters: [{label: "0", value: 0}],
                    isSearchAble: true,
                    searchType: "numberRange"
                },{
                    fields: ['month_new_performance'],
                    title: '新签业绩',
                    titleAlign: 'center',
                    filterMultiple: false,
                    filters: [{label: "0", value: 0}],
                    orderBy: '',
                    isSearchAble: true,
                    searchType: 'numberRange'
                },{
                    fields: ['month_new_rate'],
                    title: '新签完成率',
                    titleAlign: 'center',
                    filterMultiple: false,
                    filters: [{label: "0", value: 0}],
                    orderBy: '',
                    isSearchAble: true,
                    searchType: 'numberRange'
                },{
                    fields: ['month_renew_goal'],
                    title: '续签任务',
                    titleAlign: 'center',
                    orderBy: '',
                    filterMultiple: false,
                    filters: [{label: "0", value: 0}],
                    isSearchAble: true,
                    searchType: "numberRange"
                },{
                    fields: ['month_renew_performance'],
                    title: '续签业绩',
                    titleAlign: 'center',
                    filterMultiple: false,
                    filters: [{label: "0", value: 0}],
                    orderBy: '',
                    isSearchAble: true,
                    searchType: 'numberRange'
                },{
                    fields: ['month_renew_rate'],
                    title: '续签完成率',
                    titleAlign: 'center',
                    filterMultiple: false,
                    filters: [{label: "0", value: 0}],
                    orderBy: '',
                    isSearchAble: true,
                    searchType: 'numberRange'
                },{
                    fields: ['month_goal'],
                    title: '当月任务',
                    titleAlign: 'center',
                    orderBy: '',
                    filterMultiple: false,
                    filters: [{label: "0", value: 0}],
                    isSearchAble: true,
                    searchType: "numberRange"
                },{
                    fields: ['month_performance'],
                    title: '当月业绩',
                    titleAlign: 'center',
                    filterMultiple: false,
                    filters: [{label: "0", value: 0}],
                    orderBy: '',
                    isSearchAble: true,
                    searchType: 'numberRange'
                },{
                    fields: ['month_rate'],
                    title: '当月业绩完成率',
                    titleAlign: 'center',
                    filterMultiple: false,
                    filters: [{label: "0", value: 0}],
                    orderBy: '',
                    isSearchAble: true,
                    searchType: 'numberRange'
                },{
                    fields: ['month_head_confirm_money'],
                    title: '月初承诺值',
                    titleAlign: 'center',
                    filterMultiple: false,
                    filters: [{label: "0", value: 0}],
                    orderBy: '',
                    isSearchAble: true,
                    searchType: 'numberRange'
                },{
                    fields: ['month_confirm_money'],
                    title: '当前承诺值',
                    titleAlign: 'center',
                    filterMultiple: false,
                    filters: [{label: "0", value: 0}],
                    orderBy: '',
                    isSearchAble: true,
                    searchType: 'numberRange'
                },{
                    fields: ['confirm_goal_rate'],
                    title: '承诺值/任务值',
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
                    title: '已归档',
                    titleAlign: 'center',
                    filterMultiple: false,
                    filters: [{label: "0", value: 0}],
                    orderBy: '',
                    isSearchAble: true,
                    searchType: 'numberRange'
                },{
                    fields: ['month_call_num'],
                    title: '电话数',
                    titleAlign: 'center',
                    orderBy: '',
                    filterMultiple: false,
                    filters: [{label: "空", value: ""}],
                    isSearchAble: true,
                    searchType: 'numberRange'
                },{
                    fields: ['month_visit_num'],
                    title: '出差数',
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
                    title: '活跃数',
                    titleAlign: 'center',
                    orderBy: '',
                    filterMultiple: false,
                    filters: [{label: "0", value: 0}],
                    isSearchAble: true,
                    searchType: "numberRange"
                },{
                    fields: ['ms_month_new_num'],
                    title: '新建数',
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
                    title: '活跃数',
                    titleAlign: 'center',
                    orderBy: '',
                    filterMultiple: false,
                    filters: [{label: "0", value: 0}],
                    isSearchAble: true,
                    searchType: "numberRange"
                },{
                    fields: ['ts_month_new_num'],
                    title: '新建数',
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
    },
    created() {
        // this.getSourceTableData();
        this.getDate();
    },
    watch: {
        "date": "getSourceTableData",
        "sourceTableData": "initTable"
    }
});

