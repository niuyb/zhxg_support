new Vue({
    el: '#data-all',
    data() {
        return {
            total: 0,
            pageIndex: 1,
            pageSize: 20,
            sourceTableData: [],
            tableData: [],
            tableConfig: {
                multipleSort: false,
                tableData: [],
                columns: [{
                    field: 'custome',
                    width: 50,
                    titleAlign: 'center',
                    columnAlign: 'center',
                    formatter: function(rowData, index, pagingIndex) {
                        var currentIndex = index + pagingIndex;
                        return currentIndex + 1
                        // return currentIndex < 3 ? '<span style="color:red;font-weight: bold;">' + (currentIndex + 1) + '</span>': currentIndex + 1
                    },
                    isFrozen: true
                },
                {
                    field: 'name',
                    width: 100,
                    columnAlign: 'center',
                    isFrozen: true
                },
                {
                    field: 'level',
                    width: 100,
                    columnAlign: 'center',
                    isFrozen: false,
                    isResize: true
                },
                {
                    field: 'department',
                    width: 90,
                    columnAlign: 'center',
                    isFrozen: false,
                    isResize: true
                },
                {
                    field: 'workCallCount',
                    width: 90,
                    columnAlign: 'left',
                    isResize: true
                },
                {
                    field: 'workVisitCount',
                    width: 90,
                    columnAlign: 'center',
                    isResize: true
                },
                {
                    field: 'workRecordCount',
                    width: 90,
                    columnAlign: 'center',
                    isFrozen: false,
                    isResize: true
                },
                {
                    field: 'opportunityTodayCount',
                    width: 90,
                    columnAlign: 'center',
                    isFrozen: false,
                    isResize: true
                },
                {
                    field: 'opportunityWeekCount',
                    width: 90,
                    columnAlign: 'center',
                    isFrozen: false,
                    isResize: true
                },
                {
                    field: 'opportunityMonthCount',
                    width: 90,
                    columnAlign: 'center',
                    isFrozen: false,
                    isResize: true
                },
                {
                    field: 'opportunityTodaySaleCount',
                    width: 90,
                    columnAlign: 'center',
                    isFrozen: false,
                    isResize: true
                },
                {
                    field: 'customerFormalCount',
                    width: 90,
                    columnAlign: 'center',
                    isFrozen: false,
                    isResize: true
                },
                {
                    field: 'customerImportantCount',
                    width: 90,
                    columnAlign: 'center',
                    isFrozen: false,
                    isResize: true
                },
                {
                    field: 'customerDevelopingCount',
                    width: 90,
                    columnAlign: 'center',
                    isFrozen: false,
                    isResize: true
                },
                {
                    field: 'accountYqmsFormalCount',
                    width: 90,
                    columnAlign: 'center',
                    isFrozen: false,
                    isResize: true
                },
                {
                    field: 'accountYqmsTrialCount',
                    width: 90,
                    columnAlign: 'center',
                    isFrozen: false,
                    isResize: true
                },
                {
                    field: 'accountYqmsStopCount',
                    width: 90,
                    columnAlign: 'center',
                    isFrozen: false,
                    isResize: true
                },
                {
                    field: 'accountTsgzFormalCount',
                    width: 90,
                    columnAlign: 'center',
                    isFrozen: false,
                    isResize: true
                },
                {
                    field: 'accountTsgzTrialCount',
                    width: 90,
                    columnAlign: 'center',
                    isFrozen: false,
                    isResize: true
                },
                {
                    field: 'accountTsgzStopCount',
                    width: 90,
                    columnAlign: 'center',
                    isFrozen: false,
                    isResize: true
                },
                {
                    field: 'accountZhwpFormalCount',
                    width: 90,
                    columnAlign: 'center',
                    isFrozen: false,
                    isResize: true
                },
                {
                    field: 'accountZhwpTrialCount',
                    width: 90,
                    columnAlign: 'center',
                    isFrozen: false,
                    isResize: true
                },
                {
                    field: 'accountZhwpStopCount',
                    width: 90,
                    columnAlign: 'center',
                    isFrozen: false,
                    isResize: true
                }],
                titleRows: [[{
                    fields: ['custome'],
                    title: '排序',
                    titleAlign: 'center',
                    rowspan: 3,
                    // orderBy: '',
                },{
                    fields: ['name'],
                    title: '名称',
                    titleAlign: 'center',
                    rowspan: 3
                },{
                    fields: ['level'],
                    title: '级别',
                    titleAlign: 'center',
                    rowspan: 3,
                    filterMultiple: false,
                    filters: [
                    {
                        label: '销售中心',
                        value: '销售中心',
                    },
                    {
                        label: '大区',
                        value: '大区',
                    },
                    {
                        label: '省',
                        value: '省',
                    },
                    {
                        label: '区总',
                        value: '区总',
                    },
                    {
                        label: '省总',
                        value: '省总',
                    },
                    {
                        label: '商务',
                        value: '商务',
                    }]
                },{
                    fields: ['department'],
                    title: '部门',
                    titleAlign: 'center',
                    rowspan: 3,
                    filterMultiple: false,
                    filters: [{
                        label: '销售中心',
                        value: '销售中心',
                    },
                    {
                        label: '一大区',
                        value: '一大区',
                    },
                    {
                        label: '上海特区',
                        value: '上海特区',
                    },
                    {
                        label: '安徽',
                        value: '安徽',
                    },
                    {
                        label: '上海',
                        value: '上海',
                    },
                    {
                        label: '政务事业部',
                        value: '政务事业部',
                    }]
                },
                {
                    fields: ['workCallCount', 'workVisitCount', 'workRecordCount'],
                    title: '日常工作',
                    titleAlign: 'center',
                    colspan: 3,
                    rowspan: 2
                },
                {
                    fields: ['opportunityTodayCount', 'opportunityWeekCount', 'opportunityMonthCount', 'opportunityTodaySaleCount'],
                    title: '商机',
                    titleAlign: 'center',
                    colspan: 4,
                    rowspan: 2
                },
                {
                    fields: ['customerFormalCount', 'customerImportantCount', 'customerDevelopingCount'],
                    title: '客户',
                    titleAlign: 'center',
                    colspan: 3,
                    rowspan: 2
                },
                {
                    fields: ['accountYqmsFormalCount', 'accountYqmsTrialCount', 'accountYqmsStopCount',
                            'accountTsgzFormalCount', 'accountTsgzTrialCount', 'accountTsgzStopCount',
                            'accountZhwpFormalCount', 'accountZhwpTrialCount', 'accountZhwpStopCount'],
                    title: '账号',
                    titleAlign: 'center',
                    colspan: 9
                }], [{
                    fields: ['accountYqmsFormalCount', 'accountYqmsTrialCount', 'accountYqmsStopCount'],
                    title: '舆情秘书',
                    titleAlign: 'center',
                    colspan: 3
                },
                {
                    fields: ['accountTsgzFormalCount', 'accountTsgzTrialCount', 'accountTsgzStopCount'],
                    title: '态势感知',
                    titleAlign: 'center',
                    colspan: 3
                },
                {
                    fields: ['accountZhwpFormalCount', 'accountZhwpTrialCount', 'accountZhwpStopCount'],
                    title: '智慧网评',
                    titleAlign: 'center',                    
                    colspan: 3
                }], [{
                    fields: ['workCallCount'],
                    title: '电话拜访',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['workVisitCount'],
                    title: '签到拜访',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['workRecordCount'],
                    title: '快速记录',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['opportunityTodayCount'],
                    title: '今日创建商机',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['opportunityWeekCount'],
                    title: '本周创建商机',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['opportunityMonthCount'],
                    title: '本月创建商机',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['opportunityTodaySaleCount'],
                    title: '今日销售商机推动个数',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['customerFormalCount'],
                    title: '正式',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['customerImportantCount'],
                    title: '重点',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['customerDevelopingCount'],
                    title: '开发',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['accountYqmsFormalCount'],
                    title: '正式',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['accountYqmsTrialCount'],
                    title: '试用',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['accountYqmsStopCount'],
                    title: '停用',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['accountTsgzFormalCount'],
                    title: '正式',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['accountTsgzTrialCount'],
                    title: '试用',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['accountTsgzStopCount'],
                    title: '停用',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['accountZhwpFormalCount'],
                    title: '正式',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['accountZhwpTrialCount'],
                    title: '试用',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['accountZhwpStopCount'],
                    title: '停用',
                    titleAlign: 'center',
                    orderBy: ''
                },]],
            }
        }
    },
    methods: {
        // 根据各筛选条件、和排序条件，获取当前页面的数据，进行展示
        getTableShowData() {
            this.tableConfig.tableData = this.tableData.slice((this.pageIndex - 1) * this.pageSize, (this.pageIndex) * this.pageSize)
        },
        // 从服务器获取原始数据
        getSourceTableData(){
            // 暂时用假数据代替
            this.sourceTableData = tableData
        },
        // 深拷贝原始数据
        getTableData(){
            return JSON.parse(JSON.stringify(this.sourceTableData));
        },
        pageChange(pageIndex) {
            this.pageIndex = pageIndex;
            this.getTableShowData();
            console.log(pageIndex)
        },
        pageSizeChange(pageSize) {
            this.pageIndex = 1;
            this.pageSize = pageSize;
            this.getTableShowData()
        },
        sortChange(params) {
            for (var k in params){
                if ((params[k]).length > 0) {
                    this.tableData.sort(function(a, b) {
                        if (params[k] === 'asc') {
                            return a[k] - b[k]
                        } else if (params[k] === 'desc') {
                            return b[k] - a[k]
                        } else {
                            return 0
                        }
                    });
                    this.pageChange(1);
                }
            }
            // if (params.custome.length > 0) {
            //     this.tableData.sort(function(a, b) {
            //         if (params.height === 'asc') {
            //             return a.height - b.height
            //         } else if (params.height === 'desc') {
            //             return b.height - a.height
            //         } else {
            //             return 0
            //         }
            //     });
            //     this.pageChange(1);
            // }
        },
        filterMethod(filters) {
            console.log(filters);
            let tableData = this.getTableData();
            // if (Array.isArray(filters.gender)) {
            //     tableData = tableData.filter(item => item.gender === filters.gender[0])
            // }
            // if (Array.isArray(filters.name)) {
            //     tableData = tableData.filter(item => filters.name.indexOf(item.name) > -1)
            // }
            for (var k in filters){
                if (Array.isArray(filters[k])) {
                    tableData = tableData.filter(item => item[k] === filters[k][0])
                }
            }
            this.tableData = tableData;
            this.total = this.tableData.length;
            this.pageChange(1);
        },
    },
    created() {
        this.getSourceTableData();
        this.tableData = this.getTableData();
        this.total = this.tableData.length;
        this.getTableShowData();
    }
});
