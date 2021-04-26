function initSalerVue(){
    new Vue({
        el: '#saler',
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
                        field: 'saler_name',
                        width: 80,
                        columnAlign: 'center',
                        isFrozen: true,
                        isResize: true
                    },{
                        field: 'department_name',
                        width: 80,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true
                    },{
                        field: 'date_joined',
                        width: 100,
                        columnAlign: 'center',
                        isResize: true,
                        isSelect: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['date_joined'];
                            if (!value){
                                return "----";
                            }else{
                                return value.split(" ")[0];
                            }
                        }
                    },{
                        field: 'days_joined',
                        width: 100,
                        columnAlign: 'center',
                        isResize: true,
                        isSelect: true
                    // },{
                    //     field: 'customer_count',
                    //     width: 100,
                    //     columnAlign: 'center',
                    //     isFrozen: false,
                    //     isResize: true,
                    //     formatter: function(rowData, index, pagingIndex){
                    //         var value = rowData['customer_count'];
                    //         if (!value){
                    //             return "0";
                    //         }else{
                    //             return value;
                    //         }
                    //     }
                    // },{
                    //     field: 'account_count',
                    //     width: 80,
                    //     columnAlign: 'center',
                    //     isFrozen: false,
                    //     isResize: true,
                    //     formatter: function(rowData, index, pagingIndex){
                    //         var value = rowData['account_count'];
                    //         if (!value){
                    //             return "0";
                    //         }else{
                    //             return value;
                    //         }
                    //     }
                    // },{
                    //     field: 'opportunity_count',
                    //     width: 80,
                    //     columnAlign: 'center',
                    //     isFrozen: false,
                    //     isResize: true,
                    //     formatter: function(rowData, index, pagingIndex){
                    //         var value = rowData['opportunity_count'];
                    //         if (!value){
                    //             return "0";
                    //         }else{
                    //             return value;
                    //         }
                    //     }
                    // },{
                    //     field: 'sale_money',
                    //     width: 90,
                    //     columnAlign: 'center',
                    //     isFrozen: false,
                    //     isResize: true,
                    //     formatter: function(rowData, index, pagingIndex){
                    //         return toThousands(rowData["sale_money"])
                    //     }
                    },{
                        field: 'date_first_order',
                        width: 130,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['date_first_order'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'money_first_order',
                        width: 100,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            return toThousands(rowData["money_first_order"])
                        }
                    },{
                        field: 'customer_first_order',
                        width: 180,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['customer_first_order'];
                            if (!value){
                                value = "----";
                            }
                            return value;
                        }
                    },{
                        field: 'cycle_first_order',
                        width: 130,
                        columnAlign: 'center',
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['cycle_first_order'];
                            if (!value || value == "----"){
                                value = 0;
                            }
                            return parseInt(value);
                        }
                    },{
                        field: 'date_last_order',
                        width: 130,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['date_last_order'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'money_last_order',
                        width: 150,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            return toThousands(rowData["money_last_order"])
                        }
                    },{
                        field: 'customer_last_order',
                        width: 180,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['customer_last_order'];
                            if (!value){
                                value = "----";
                            }
                            return value;
                        }
                    },{
                        field: 'days_last_order_to_today',
                        width: 150,
                        columnAlign: 'center',
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['days_last_order_to_today'];
                            if (!value || value == "----"){
                                value = 0;
                            }
                            return parseInt(value);
                        }
                    },{
                        field: 'date_last_order_2',
                        width: 150,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['date_last_order_2'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'money_last_order_2',
                        width: 150,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            return toThousands(rowData["money_last_order_2"])
                        }
                    },{
                        field: 'customer_last_order_2',
                        width: 180,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['customer_last_order_2'];
                            if (!value){
                                value = "----";
                            }
                            return value;
                        }
                    },{
                        field: 'days_last_order_2_to_today',
                        width: 150,
                        columnAlign: 'center',
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['days_last_order_2_to_today'];
                            if (!value || value == "----"){
                                value = 0;
                            }
                            return parseInt(value);
                        }
                    },{
                        field: 'count_orders',
                        width: 120,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            return toThousands(rowData["count_orders"])
                        }
                    },{
                        field: 'money_orders',
                        width: 120,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            return toThousands(rowData["money_orders"])
                        }
                    },{
                        field: 'count_orders_2020',
                        width: 150,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            return toThousands(rowData["count_orders_2020"])
                        }
                    },{
                        field: 'money_orders_2020',
                        width: 150,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            return toThousands(rowData["money_orders_2020"])
                        }
                    },{
                        field: 'date_last_visit',
                        width: 150,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['date_last_visit'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'count_customers',
                        width: 120,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            return toThousands(rowData["count_customers"])
                        }
                    },{
                        field: 'count_formal_customers',
                        width: 150,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            return toThousands(rowData["count_formal_customers"])
                        }
                    },{
                        field: 'count_important_customers',
                        width: 150,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            return toThousands(rowData["count_important_customers"])
                        }
                    },{
                        field: 'count_developing_customers',
                        width: 150,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            return toThousands(rowData["count_developing_customers"])
                        }
                    },{
                        field: 'operation',
                        width: 120,
                        columnAlign: 'center',
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['operation'];
                            if (!value || value == "----"){
                                value = "";
                            }
                            return value;
                        }
                    }],
                    titleRows: [[{
                        fields: ['custome'],
                        title: '序号',
                        titleAlign: 'center',
                        // orderBy: '',
                    },{
                        fields: ['saler_name'],
                        title: '商务',
                        titleAlign: 'center',
                        filterMultiple: true,
                        filters: [{label: "空", value: ""}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['department_name'],
                        title: '部门',
                        titleAlign: 'center',
                        filterMultiple: true,
                        filters: [],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['date_joined'],
                        title: '入职日期',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{label: "空", value: ""}],
                        isSearchAble: true,
                        searchType: 'dateRange'
                    },{
                        fields: ['days_joined'],
                        title: '入职天数',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{label: "空", value: ""}],
                        isSearchAble: true,
                        searchType: 'numberRange'
                    // },{
                    //     fields: ['customer_count'],
                    //     title: '客户数量',
                    //     titleAlign: 'center',
                    //     orderBy: '',
                    //     filterMultiple: false,
                    //     filters: [{label: "0", value: 0}],
                    //     isSearchAble: true,
                    //     searchType: "numberRange"
                    // },{
                    //     fields: ['account_count'],
                    //     title: '账号数量',
                    //     titleAlign: 'center',
                    //     orderBy: '',
                    //     filterMultiple: false,
                    //     filters: [{label: "0", value: 0}],
                    //     isSearchAble: true,
                    //     searchType: "numberRange"
                    // },{
                    //     fields: ['opportunity_count'],
                    //     title: '商机数量',
                    //     titleAlign: 'center',
                    //     orderBy: '',
                    //     filterMultiple: false,
                    //     filters: [{label: "0", value: 0}],
                    //     isSearchAble: true,
                    //     searchType: "numberRange"
                    // },{
                    //     fields: ['sale_money'],
                    //     title: '销售额',
                    //     titleAlign: 'center',
                    //     filterMultiple: false,
                    //     filters: [{label: "0", value: 0}],
                    //     orderBy: '',
                    //     isSearchAble: true,
                    //     searchType: 'numberRange'
                    },{
                        fields: ['date_first_order'],
                        title: '首单签单日期',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{label: "空", value: ""}],
                        isSearchAble: true,
                        searchType: 'dateRange'
                    },{
                        fields: ['money_first_order'],
                        title: '首单金额',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{label: "0", value: 0}],
                        orderBy: '',
                        isSearchAble: true,
                        searchType: 'numberRange'
                    },{
                        fields: ['customer_first_order'],
                        title: '首单客户',
                        filters: [{label: "空", value: ""}],
                        isSearchAble: true,
                        searchType: "string",
                        filterMultiple: false,
                        titleAlign: 'center'
                    },{
                        fields: ['cycle_first_order'],
                        title: '首单签单周期',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{label: "0", value: 0}],
                        isSearchAble: true,
                        searchType: "numberRange"
                    },{
                        fields: ['date_last_order'],
                        title: '最近新签日期',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{label: "空", value: ""}],
                        isSearchAble: true,
                        searchType: 'dateRange'
                    },{
                        fields: ['money_last_order'],
                        title: '最近新签金额',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{label: "0", value: 0}],
                        orderBy: '',
                        isSearchAble: true,
                        searchType: 'numberRange'
                    },{
                        fields: ['customer_last_order'],
                        title: '最近新签客户',
                        filters: [{label: "空", value: ""}],
                        isSearchAble: true,
                        searchType: "string",
                        titleAlign: 'center'
                    },{
                        fields: ['days_last_order_to_today'],
                        title: '最近新签距今天数',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{label: "0", value: 0}],
                        isSearchAble: true,
                        searchType: "numberRange"
                    },{
                        fields: ['date_last_order_2'],
                        title: '最近续签日期',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{label: "空", value: ""}],
                        isSearchAble: true,
                        searchType: 'dateRange'
                    },{
                        fields: ['money_last_order_2'],
                        title: '最近续签金额',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{label: "0", value: 0}],
                        orderBy: '',
                        isSearchAble: true,
                        searchType: 'numberRange'
                    },{
                        fields: ['customer_last_order_2'],
                        title: '最近续签客户',
                        filters: [{label: "空", value: ""}],
                        isSearchAble: true,
                        searchType: "string",
                        titleAlign: 'center'
                    },{
                        fields: ['days_last_order_2_to_today'],
                        title: '最近续签距今天数',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{label: "0", value: 0}],
                        isSearchAble: true,
                        searchType: "numberRange"
                    },{
                        fields: ['count_orders'],
                        title: '订单总数量',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{label: "0", value: 0}],
                        isSearchAble: true,
                        searchType: "numberRange"
                    },{
                        fields: ['money_orders'],
                        title: '订单总金额',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{label: "0", value: 0}],
                        isSearchAble: true,
                        searchType: "numberRange"
                    },{
                        fields: ['count_orders_2020'],
                        title: '2020年订单总量',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{label: "0", value: 0}],
                        isSearchAble: true,
                        searchType: "numberRange"
                    },{
                        fields: ['money_orders_2020'],
                        title: '2020年订单总金额',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{label: "0", value: 0}],
                        isSearchAble: true,
                        searchType: "numberRange"
                    },{
                        fields: ['date_last_visit'],
                        title: '最近拜访日期',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{label: "空", value: ""}],
                        isSearchAble: true,
                        searchType: 'dateRange'
                    },{
                        fields: ['count_customers'],
                        title: '客户总数量',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{label: "0", value: 0}],
                        isSearchAble: true,
                        searchType: "numberRange"
                    },{
                        fields: ['count_formal_customers'],
                        title: '正式客户数量',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{label: "0", value: 0}],
                        isSearchAble: true,
                        searchType: "numberRange"
                    },{
                        fields: ['count_important_customers'],
                        title: '重点客户数量',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{label: "0", value: 0}],
                        isSearchAble: true,
                        searchType: "numberRange"
                    },{
                        fields: ['count_developing_customers'],
                        title: '开发客户数量',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{label: "0", value: 0}],
                        isSearchAble: true,
                        searchType: "numberRange"
                    },{
                        fields: ['operation'],
                        title: '操作',
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
                    var label = value;
                    if (field === "date_joined" || field === "date_first_order"){
                        if (value){
                            value = value.split(" ")[0];
                            label = value;
                        }
                    }
                    if (value === ""){
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
            // 根据各筛选条件、和排序条件，获取当前页面的数据，进行展示
            getTableShowData() {
                this.tableConfig.tableData = this.tableData.slice((this.pageIndex - 1) * this.pageSize, (this.pageIndex) * this.pageSize)
            },
            // 从服务器获取原始数据
            getSourceTableData(){
                var self = this;
                var did = getUrlKey('did', window.location.href);
                var url = '/sale/saler/info/list/api';
                axios.get(url, {
                    params: {
                        'did': did,
                        'page': 1,
                        "num": 0
                    }
                }).then(function(res){
                    self.sourceTableData = res.data.data;
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
                console.log(pageIndex)
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
                        if ("date_joined" === k || "date_first_order" === k || "date_last_order" === k || "date_last_order_2" === k || "date_last_visit" === k){
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
                // this.setFooterData();
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
                // this.setFooterData();
            },
            setFilters(){
                var commonFields = ["saler_name", "department_name"];
                for (var row of this.tableConfig.titleRows){
                    for (var item of row){
                        var field = item["fields"][0];
                        if (commonFields.indexOf(field) > -1){
                            var filters = this.getCommonFilters(field)
                            if ("xxxxxxxxxxxxxxx" == field){
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
                    sale_moneys = this.tableData.map(item => {
                        return item.sale_money;
                    });
                let sumVal = ["汇总"];
                for (let i=1; i < this.tableConfig.columns.length; i++){
                    let col = this.tableConfig.columns[i];
                    if ("sale_money" === col.field){
                        sumVal.push(
                            toThousands(sale_moneys.reduce((prev, curr) => {
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
                // this.setFooterData();
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
