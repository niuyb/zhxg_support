function initCustomerVue(){
    new Vue({
        el: '#customer',
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
                        field: 'customer_name',
                        width: 200,
                        columnAlign: 'center',
                        isFrozen: true,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            return "<a href='#" + 22222222222222 + "'>" + rowData['customer_name'] + "</a>"
                        }
                    },
                    {
                        field: 'customer_level',
                        width: 100,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true
                    },
                    {
                        field: 'account_num',
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
                    },
                    {
                        field: 'days_left',
                        width: 90,
                        columnAlign: 'center',
                        isResize: true,
                    },
                    {
                        field: 'last_visit',
                        width: 90,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true
                    }],
                    titleRows: [[{
                        fields: ['custome'],
                        title: '序号',
                        titleAlign: 'center',
                        // orderBy: '',
                    },{
                        fields: ['customer_name'],
                        title: '客户名称',
                        titleAlign: 'center',
                    },{
                        fields: ['customer_level'],
                        title: '客户级别',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [],
                        isInput: true
                    },{
                        fields: ['account_num'],
                        title: '账号数量',
                        titleAlign: 'center',
                        filterMultiple: false,
                        orderBy: ''
                    },
                    {
                        fields: ['saler_name'],
                        title: '商务',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [],
                        isSearchAble: true,
                        searchType: 'string'
                    },
                    {
                        fields: ['days_left'],
                        title: '合同截止剩余天数',
                        titleAlign: 'center',
                        orderBy: ''
                    },
                    {
                        fields: ['last_visit'],
                        title: '最近拜访时间',
                        titleAlign: 'center',
                        orderBy: ''
                    }]],
                }
            }
        },
        methods: {
            // 根据各筛选条件、和排序条件，获取当前页面的数据，进行展示
            getTableShowData() {
                this.tableConfig.tableData = this.tableData.slice((this.pageIndex - 1) * this.pageSize, (this.pageIndex) * this.pageSize)
            },
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
            getCustomerLevelFilters(){
                // var filters = [];
                // var js = {};
                // for (var row of this.sourceTableData){
                //     var level = row["customer_level"];
                //     if (!(js[level])){
                //         js[level] = true;
                //         var item = {
                //             label: level,
                //             value: level
                //         };
                //         filters.push(item);
                //     }
                // }
                // return filters;
                return this.getCommonFilters("customer_level");
            },
            getSalerNameFilters(){
                return this.getCommonFilters("saler_name");
            },
            // 从服务器获取原始数据
            getSourceTableData(){
                // 暂时用假数据代替
                // this.sourceTableData = initCustomers(45000); 
                var self = this;
                var did = getUrlKey('did', window.location.href);
                var url = '/sale/customer/list/api';
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
                        if (field == 'customer_level'){
                            var filters = this.getCustomerLevelFilters();
                            item["filters"] = filters;
                        }else if(field == 'saler_name'){
                            var filters = this.getSalerNameFilters();
                            item["filters"] = filters;
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
