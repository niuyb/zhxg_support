function initOpportunityVue(){
    new Vue({
        el: '#opportunity',
        data() {
            return {
                loading: true,
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
                        field: 'opportunity_name',
                        width: 200,
                        columnAlign: 'center',
                        isFrozen: true,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            return "<a href='#" + 22222222222222 + "'>" + rowData['opportunity_name'] + "</a>"
                        }
                    },
                    {
                        field: 'customer_name',
                        width: 100,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            return "<a href='#" + 22222222222222 + "'>" + rowData['customer_name'] + "</a>"
                        }
                    },
                    {
                        field: 'opportunity_money',
                        width: 90,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            return toThousands(rowData["opportunity_money"])
                        }
                    },
                    {
                        field: 'win_rate',
                        width: 10,
                        columnAlign: 'center',
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['win_rate'];
                            // if (!value || value == 0 || value == "----"){
                            //     return "0";
                            // }else{
                            //     return value + "%";
                            // }
                            if (!value || value == "----"){
                                value = 0;
                            }
                            return parseInt(value);
                        }
                    },
                    {
                        field: 'quzong_ok',
                        width: 90,
                        columnAlign: 'center',
                        isResize: true,
                        isSelect: true,
                        isInput: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['quzong_ok'];
                            if (!value){
                                return "----";
                            }else{
                                return value.split(" ")[0];
                            }
                        }
                    },
                    {
                        field: 'last_visit',
                        width: 90,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true
                    },
                    {
                        field: 'saler_name',
                        width: 90,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            return "<a href='#" + 22222222222222 + "'>" + rowData['saler_name'] + "</a>"
                        }
                    }],
                    titleRows: [[{
                        fields: ['custome'],
                        title: '序号',
                        titleAlign: 'center',
                        // orderBy: '',
                    },{
                        fields: ['opportunity_name'],
                        title: '商机名称',
                        titleAlign: 'center',
                    },{
                        fields: ['customer_name'],
                        title: '最终客户',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: []
                    },{
                        fields: ['opportunity_money'],
                        title: '商机金额',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [],
                        orderBy: ''
                    },
                    {
                        fields: ['win_rate'],
                        title: '赢率',
                        titleAlign: 'center',
                        orderBy: ''
                    },
                    {
                        fields: ['quzong_ok'],
                        title: '区总确认归档日期',
                        titleAlign: 'center',
                        filterMultiple: true,
                        filters: [{lable: "空", value: "----"}],
                        isSearchAble: true,
                        searchType: 'dateRange'
                    },
                    {
                        fields: ['last_visit'],
                        title: '最近拜访时间',
                        titleAlign: 'center'
                    },
                    {
                        fields: ['saler_name'],
                        title: '商务',
                        titleAlign: 'center'
                    }]],
                }
            }
        },
        methods: {
            getCommonFilters(field){
                var filters = [];
                var js = {};
                for (var row of this.sourceTableData){
                    var value = row[field];
                    if (!(js[value])){
                        js[value] = true;
                        var item = {
                            label: value,
                            value: value
                        };
                        filters.push(item);
                    }
                }
                return filters;
            },
            getSalerNameFilters(){
                return this.getCommonFilters("saler_name");
            },
            // 根据各筛选条件、和排序条件，获取当前页面的数据，进行展示
            getTableShowData() {
                this.tableConfig.tableData = this.tableData.slice((this.pageIndex - 1) * this.pageSize, (this.pageIndex) * this.pageSize)
            },
            // 从服务器获取原始数据
            getSourceTableData(){
                // 暂时用假数据代替
                // this.sourceTableData = initOpportunities(45000);
                var self = this;
                var did = getUrlKey('did', window.location.href);
                var url = '/sale/opportunity/list/api';
                axios.get(url, {
                    params: {
                        'did': did,
                        'page': 1,
                        "num": 0
                    }
                }).then(function(res){
                    self.sourceTableData = res.data.data.data;
                }).catch(function(err){
                    console.log(err)
                });
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
            setFilters(){
                for (var row of this.tableConfig.titleRows){
                    for (var item of row){
                        var field = item["fields"][0];
                        if(field == 'saler_name'){
                            var filters = this.getSalerNameFilters();
                            item["filters"] = filters;
                        }
                        if (field == 'quzong_ok'){
                            item["filters"] = this.getCommonFilters(field)
                        }
                        ////////////////
                    }                    
                }
            },
            initTable(){
                this.tableData = this.getTableData();
                this.total = this.tableData.length;
                this.getTableShowData();
                this.setFilters();
                this.loading = false;
            }
        },
        created() {
            this.getSourceTableData();
        },
        watch: {
            "sourceTableData": "initTable",
            // "customerLevelFilters": "setCustomerLevelFilters",
        }
    });
}

// initOpportunityVue();
