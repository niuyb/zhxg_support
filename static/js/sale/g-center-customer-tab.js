function initCustomerVue(){
    new Vue({
        el: '#customer',
        data() {
            return {
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
                    },{
                        field: 'customer_name',
                        width: 200,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['customer_name'];
                            let cid = rowData['customer_id'];
                            if (!value){
                                return "----";
                            }else{
                                return "<a target='_blank' href='http://crm.xiaoshouyi.com/final/account.action?id=" + cid + "'>" + value + "</a>";
                            }
                        }
                    },{
                        field: 'saler_name',
                        width: 90,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true
                    },{
                        field: 'department_name',
                        width: 90,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true
                    },{
                        field: 'customer_level',
                        width: 100,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true
                    },{
                        field: 'account_num',
                        width: 90,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true
                    },{
                        field: 'days_left',
                        width: 90,
                        columnAlign: 'center',
                        isResize: true,
                    // },{
                    //     field: 'last_visit',
                    //     width: 90,
                    //     columnAlign: 'center',
                    //     isFrozen: false,
                    //     isResize: true,
                    //     formatter: function(rowData, index, pagingIndex){
                    //         var value = rowData['last_visit'];
                    //         if (!value){
                    //             return "----"
                    //         }else{
                    //             return value
                    //         }                            
                    //     }                
                    // },{
                    //     field: 'last_call',
                    //     width: 90,
                    //     columnAlign: 'center',
                    //     isFrozen: false,
                    //     isResize: true,
                    //     formatter: function(rowData, index, pagingIndex){
                    //         var value = rowData['last_call'];
                    //         if (!value){
                    //             return "----"
                    //         }else{
                    //             return value
                    //         }                            
                    //     }                
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
                        filterMultiple: false,
                        filters: [{label: "空", value: ""}],
                        isSearchAble: true,
                        searchType: 'string'
                    },{
                        fields: ['saler_name'],
                        title: '商务',
                        titleAlign: 'center',
                        filterMultiple: true,
                        filters: [],
                        isSearchAble: true,
                        searchType: 'string'
                    },{
                        fields: ['department_name'],
                        title: '部门',
                        titleAlign: 'center',
                        filterMultiple: true,
                        filters: [],
                        isSearchAble: true,
                        searchType: 'string'
                    },{
                        fields: ['customer_level'],
                        title: '客户级别',
                        titleAlign: 'center',
                        filterMultiple: true,
                        filters: []
                    },{
                        fields: ['account_num'],
                        title: '账号数量',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{label: "0", value: 0}],
                        isSearchAble: true,
                        searchType: 'numberRange'
                    },{
                        fields: ['days_left'],
                        title: '合同截止剩余天数',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{label: "0", value: 0}],
                        isSearchAble: true,
                        searchType: 'numberRange'
                    // },{
                    //     fields: ['last_visit'],
                    //     title: '最近签到拜访时间',
                    //     titleAlign: 'center',
                    //     orderBy: ''
                    // },{
                    //     fields: ['last_call'],
                    //     title: '最近电话拜访时间',
                    //     titleAlign: 'center',
                    //     orderBy: ''
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
                    var label = value;
                    if (value == ""){
                        label = "空";
                    }
                    if (!(js[value])){
                        js[value] = true;
                        var item = {
                            label: label,
                            value: value
                        };
                        filters.push(item);
                    }
                }
                return filters;
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
                    console.log(err);
                    self.$message.error("网络错误，请点击重试按钮");
                    self.loading = false;
                    self.needRetry = true;
                });
            },
            retry(){
                this.needRetry = false;
                this.loading = true;
                this.getSourceTableData();
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
                
                function commonHandler(x){
                    return x;
                }
                
                var changed = false;

                for (var k in params){
                    if ((params[k]).length > 0) {
                        var handler = commonHandler;
                        if ("quzong_ok" === k || "last_visit" === k){
                            handler = stringToDateTime;
                        }

                        this.tableData.sort(function(a, b) {
                            var x = handler(a[k]);
                            var y = handler(b[k]);

                            if (x === null || x === undefined || x === ""){
                                return -1;
                            }
                            if (y === null || y === undefined || y === ""){
                                return 1;
                            }

                            if (params[k] === 'asc') {
                                return x - y
                            } else if (params[k] === 'desc') {
                                return y - x
                            } else {
                                return 0
                            }
                        });
                        changed = true;
                    }
                }

                if (changed){  
                    this.pageChange(1);
                }
            },
            _filterMethod(tableData){
                let filters = this.filters;
                for (let field in filters){
                    let values = filters[field];
                    if (Array.isArray(values)){
                        if (field == "XXXXXXXXXXXXXXXXXXX"){
                            tableData = tableData.filter(item => item[field] == values[0]);
                        }else{
                            tableData = tableData.filter(item => values.indexOf(item[field]) > -1);
                        }
                    }
                }
                return tableData;
            },
            filterMethod(filters) {

                this.filters = filters;
                
                let tableData = this.getTableData();
                
                tableData = this._filterMethod(tableData);
                tableData = this._searchMethod(tableData);
                
                this.tableData = tableData;
                this.total = this.tableData.length;
                this.pageChange(1);
                this.setFooterData();
            },
            _searchOnce(tableData, searcher){

                var searchType = searcher.searchType;
                var columnName = searcher.columnName;
                var start = searcher.start;
                var end = searcher.end;

                if (searchType == "string" || searchType == String){
                    if (start){
                        var re = new RegExp(start, "i");
                        console.log(start);
                        console.log(re);
                        tableData = tableData.filter(item => re.test(item[columnName]))
                    }
                }

                if (searchType == "number" || searchType == Number){

                    tableData = tableData.filter(item => item[columnName] == start)
                }

                if (searchType == "numberRange" || searchType == NumberRange){

                    if (start != null && start != undefined && start != ""){
                        tableData = tableData.filter(item => item[columnName] >= start)
                    }

                    if (end != null && end != undefined && end != ""){
                        tableData = tableData.filter(item => item[columnName] <= end)
                    }
                }

                if (searchType == "dateRange" || searchType == DateRange){

                    if (start != null && start != undefined && start != ""){
                        var startDate = stringToDate(start);
                        tableData = tableData.filter(item => stringToDate(item[columnName]) >= startDate) 
                    }

                    if (end != null && end != undefined && end != ""){
                        var endDate = stringToDate(end);
                        tableData = tableData.filter(item => stringToDate(item[columnName]) <= endDate)
                    }
                }

                return tableData;
            },

            _searchMethod(tableData){

                var searchers = this.searchers;
                for (let key in searchers){
                    let searcher = searchers[key];
                    tableData = this._searchOnce(tableData, searcher);
                }
                return tableData;
            },

            // 关键字、数字、数字范围、时间范围搜索
            searchMethod(searcher){
                console.log(searcher);
                let tableData = this.getTableData();

                let columnName = searcher.columnName;
                
                this.searchers[columnName] = searcher;

                tableData = this._filterMethod(tableData);

                tableData = this._searchMethod(tableData);

                this.tableData = tableData;

                this.total = this.tableData.length;
                this.pageChange(1);
                this.setFooterData();
            },
            setFilters(){
                var commonFields = ["customer_level", "saler_name", "department_name"];
                for (var row of this.tableConfig.titleRows){
                    for (var item of row){
                        var field = item["fields"][0];
                        if (commonFields.indexOf(field) > -1){
                            var filters = this.getCommonFilters(field)
                            if ("win_rate" == field){
                                filters.sort(function(a, b){
                                    return a.value - b.value
                                })
                            }
                            item["filters"] = filters;
                        }
                        ////////////////
                    }                    
                }
            },
            setFooterData(){
                let result = [],
                    account_nums = this.tableData.map(item => {
                        return item.account_num;
                    });
                let sumVal = ["汇总"];
                for (let i=1; i < this.tableConfig.columns.length; i++){
                    let col = this.tableConfig.columns[i];
                    if ("account_num" === col.field){
                        sumVal.push(
                            toThousands(account_nums.reduce((prev, curr) => {
                                return parseInt(prev) + parseInt(curr);
                            }, 0))
                        );
                    }else{
                        sumVal.push("-");
                    }
                }
                result.push(sumVal);
                this.footer = result;
            },
            setFooterCellClass(rowIndex, colIndex, value){
                if (colIndex === 0){
                    return 'footer-cell-class-name-title'
                }else{
                    return 'footer-cell-class-name-normal'
                }
            },
            initTable(){
                this.tableData = this.getTableData();
                this.total = this.tableData.length;
                this.getTableShowData();
                this.setFooterData();
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
