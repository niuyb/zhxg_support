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
                    title: '??????',
                    titleAlign: 'center',
                    rowspan: 3,
                    // orderBy: '',
                },{
                    fields: ['name'],
                    title: '??????',
                    titleAlign: 'center',
                    rowspan: 3
                },{
                    fields: ['level'],
                    title: '??????',
                    titleAlign: 'center',
                    rowspan: 3,
                    filterMultiple: false,
                    filters: [
                    {
                        label: '????????????',
                        value: '????????????',
                    },
                    {
                        label: '??????',
                        value: '??????',
                    },
                    {
                        label: '???',
                        value: '???',
                    },
                    {
                        label: '??????',
                        value: '??????',
                    },
                    {
                        label: '??????',
                        value: '??????',
                    },
                    {
                        label: '??????',
                        value: '??????',
                    }]
                },{
                    fields: ['department'],
                    title: '??????',
                    titleAlign: 'center',
                    rowspan: 3,
                    filterMultiple: false,
                    filters: [{
                        label: '????????????',
                        value: '????????????',
                    },
                    {
                        label: '?????????',
                        value: '?????????',
                    },
                    {
                        label: '????????????',
                        value: '????????????',
                    },
                    {
                        label: '??????',
                        value: '??????',
                    },
                    {
                        label: '??????',
                        value: '??????',
                    },
                    {
                        label: '???????????????',
                        value: '???????????????',
                    }]
                },
                {
                    fields: ['workCallCount', 'workVisitCount', 'workRecordCount'],
                    title: '????????????',
                    titleAlign: 'center',
                    colspan: 3,
                    rowspan: 2
                },
                {
                    fields: ['opportunityTodayCount', 'opportunityWeekCount', 'opportunityMonthCount', 'opportunityTodaySaleCount'],
                    title: '??????',
                    titleAlign: 'center',
                    colspan: 4,
                    rowspan: 2
                },
                {
                    fields: ['customerFormalCount', 'customerImportantCount', 'customerDevelopingCount'],
                    title: '??????',
                    titleAlign: 'center',
                    colspan: 3,
                    rowspan: 2
                },
                {
                    fields: ['accountYqmsFormalCount', 'accountYqmsTrialCount', 'accountYqmsStopCount',
                            'accountTsgzFormalCount', 'accountTsgzTrialCount', 'accountTsgzStopCount',
                            'accountZhwpFormalCount', 'accountZhwpTrialCount', 'accountZhwpStopCount'],
                    title: '??????',
                    titleAlign: 'center',
                    colspan: 9
                }], [{
                    fields: ['accountYqmsFormalCount', 'accountYqmsTrialCount', 'accountYqmsStopCount'],
                    title: '????????????',
                    titleAlign: 'center',
                    colspan: 3
                },
                {
                    fields: ['accountTsgzFormalCount', 'accountTsgzTrialCount', 'accountTsgzStopCount'],
                    title: '????????????',
                    titleAlign: 'center',
                    colspan: 3
                },
                {
                    fields: ['accountZhwpFormalCount', 'accountZhwpTrialCount', 'accountZhwpStopCount'],
                    title: '????????????',
                    titleAlign: 'center',                    
                    colspan: 3
                }], [{
                    fields: ['workCallCount'],
                    title: '????????????',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['workVisitCount'],
                    title: '????????????',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['workRecordCount'],
                    title: '????????????',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['opportunityTodayCount'],
                    title: '??????????????????',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['opportunityWeekCount'],
                    title: '??????????????????',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['opportunityMonthCount'],
                    title: '??????????????????',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['opportunityTodaySaleCount'],
                    title: '??????????????????????????????',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['customerFormalCount'],
                    title: '??????',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['customerImportantCount'],
                    title: '??????',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['customerDevelopingCount'],
                    title: '??????',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['accountYqmsFormalCount'],
                    title: '??????',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['accountYqmsTrialCount'],
                    title: '??????',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['accountYqmsStopCount'],
                    title: '??????',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['accountTsgzFormalCount'],
                    title: '??????',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['accountTsgzTrialCount'],
                    title: '??????',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['accountTsgzStopCount'],
                    title: '??????',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['accountZhwpFormalCount'],
                    title: '??????',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['accountZhwpTrialCount'],
                    title: '??????',
                    titleAlign: 'center',
                    orderBy: ''
                },{
                    fields: ['accountZhwpStopCount'],
                    title: '??????',
                    titleAlign: 'center',
                    orderBy: ''
                },]],
            }
        }
    },
    methods: {
        // ????????????????????????????????????????????????????????????????????????????????????
        getTableShowData() {
            this.tableConfig.tableData = this.tableData.slice((this.pageIndex - 1) * this.pageSize, (this.pageIndex) * this.pageSize)
        },
        // ??????????????????????????????
        getSourceTableData(){
            // ????????????????????????
            this.sourceTableData = tableData
        },
        // ?????????????????????
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
