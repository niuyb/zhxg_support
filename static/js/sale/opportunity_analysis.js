function initOpportunityVue(){
    new Vue({
        el: '#opportunity',
        delimiters: ["[[", "]]"],
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
                opportunity_moneys: 0,
                conditions: {},
                tableConfig: {
                    columnDict: {
                        "opportunity_name":"商机名称",
                        "saler":"商务",
                        "department":"部门",
                        "archive_rate":"评价",
                        "label":"有无堵点",
                        "badlabel":"堵点标签",
                        "goodlabel":"利好标签",
                        "win_rate":"赢率",
                        "promise":"销售承诺",
                        "close_date":"结单日期",
                        "update_time":"更新日期",
                        "money":"商机金额",
                        "sale_stage":"销售阶段",
                        "customer":"最终客户",
                        "level":"客户级别",
                        "approvalstatus":"报价单状态",
                    },
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
                        field: 'opportunity_name',
                        width: 140,
                        columnAlign: 'center',
                        isFrozen: true,
                        // isFrozen: false,
                        // isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['opportunity_name'];
                            let oid = rowData["oid"];
                            if (!value){
                                return "----";
                            }else{
                                return "<a target='_blank' href='https://crm.xiaoshouyi.com/final/opportunity.action?id=" + oid + "' title='"+value+"'>" + value + "</a>";
                            }
                        }
                    },{
                        field: 'saler',
                        width: 80,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true
                    },{
                        field: 'department',
                        width: 80,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true
                    },{
                        field: 'archive_rate',
                        width: 80,
                        columnAlign: 'center',
                        isResize: true,
                        formatter: function(rowData){
                            var value = rowData['archive_rate'];
                            if (value == "高"){
                                return "<strong style='color: #32CD32' >" + value + "</strong>";
                            }
                            else if(value == "中上"){
                                return "<strong style='color: blue'>" + value + "</strong>";
                            }
                            else if(value == "中"){
                                return "<strong style='color: orange'>" + value + "</strong>";
                            }
                            else {
                                return "<strong style='color: red'>" + value + "</strong>";
                            }
                        }
                    },
                    //     {
                    //     field: 'label',
                    //     width: 80,
                    //     columnAlign: 'center',
                    //     isResize: true,
                    //     isSelect: true,
                    //     formatter: function(rowData){
                    //         var value = rowData['label'];
                    //         if (value != "无"){
                    //             return "<strong style='color: #FF0000' >有</strong>";
                    //         }else{
                    //             return "<strong style='color: #32CD32' >无</strong>";
                    //         }
                    //     }
                    // },
                    {
                        field: 'badlabel',
                        width: 220,
                        columnAlign: 'center',
                        isResize: true,
                        isSelect: true,
                        formatter: function(rowData){
                            var value =  rowData['label'];
                            if(value != "无"){
                            return "<strong style='color: #FF0000' title="+value+">" + value + "</strong>";
                            }else{
                            return "<strong style='color: #32CD32' title="+ "无"+">无</strong>";
                            }

                        }
                    },{
                        field: 'goodlabel',
                        width: 200,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData){
                            var value = rowData['good_label'];
                            if (value != "无"){
                                return "<strong style='color: #32CD32' title="+value+">" + value + "</strong>";

                            }else{
                            return "<strong style='color: #FF0000' title="+"无"+">无</strong>";
                            }
                        }
                    },{
                        field: 'approvalstatus',
                        width: 80,
                        columnAlign: 'center',
                        isResize: true,
                        isSelect: true,
                        formatter: function(rowData){
                            var value = rowData['approvalstatus'];
                            if(value  == "审批未通过"){
                               return  "<strong style='color: red' >" + value + "</strong>";
                            }
                            return value
                        }
                    },{
                        field: 'win_rate',
                        width: 80,
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
                    },{
                        field: 'promise',
                        width: 80,
                        columnAlign: 'center',
                        isResize: true,
                        isSelect: true,
                        formatter: function(rowData){
                            var value = rowData['promise'];
                            if(value  == "未填写"){
                               return  "<strong style='color: red' >" + value + "</strong>";
                            }
                            return value
                        }
                    },{
                        field: 'close_date',
                        width: 120,
                        columnAlign: 'center',
                        isResize: true,
                        isSelect: true,
                        formatter: function(rowData){
                            var value = rowData['close_date'].split(" ")[0];
                            var Date_now = new Date();
                            var today = Date_now.toLocaleDateString( );
                            value_day = value.replace("-","/");
                            value_day = value.replace("-","/");

                            if (new Date(today) > (new Date(value_day))) {
                                return "<strong style='color: red' >" + value + "</strong>";
                            }else{
                                return value
                            }
                        }
                    },{
                        field: 'update_time',
                        width: 120,
                        columnAlign: 'center',
                        isResize: true,
                        isSelect: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['update_time'];
                            if (!value){
                                return "----";
                            }else{
                                return value.split(" ")[0];
                            }
                        }
                    },{
                        field: 'money',
                        width: 120,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            return toThousands(rowData["money"])
                        }
                    },{
                        field: 'sale_stage',
                        width: 180,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true
                    },{
                        field: 'customer',
                        width: 200,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['customer'];
                            let cid = rowData['customer_id'];
                            if (!value){
                                return "----";
                            }else{
                                return "<a target='_blank' href='http://crm.xiaoshouyi.com/final/account.action?id=" + cid + "' title='"+value+"'>" + value + "</a>";
                            }
                        }
                    },{
                        field: 'level',
                        width: 90,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true
                    },
                    //     {
                    //     field: 'last_visit',
                    //     width: 140,
                    //     columnAlign: 'center',
                    //     isFrozen: false,
                    //     isResize: true,
                    //     formatter: function(rowData, index, pagingIndex){
                    //         var value = rowData['last_visit'];
                    //         if (!value){
                    //             return "----";
                    //         }else{
                    //             return value;
                    //         }
                    //     }
                    // },
                        {
                        field: 'operation',
                        width: 50,
                        columnAlign: 'center',
                        isFrozen: true,
                        isResize: true,
                        componentName:'table-operation-opp'
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
                        filterMultiple: false,
                        filters: [{label: "空", value: ""}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['saler'],
                        title: '商务',
                        titleAlign: 'center',
                        filterMultiple: true,
                        filters: [{label: "空", value: ""}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['department'],
                        title: '部门',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{label: "空", value: ""}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['archive_rate'],
                        title: '评价',
                        titleAlign: 'center',
                        // orderBy: '',
                        filterMultiple: true,
                        filters: [{label: "高", value: "高"}, {label: "中上", value: "中上"},{label: "中", value: "中"},{label: "低", value: "低"}],
                        isSearchAble: true,
                        searchType: "string"
                    },
                    //     {
                    //     fields: ['label'],
                    //     title: '有无堵点',
                    //     titleAlign: 'center',
                    //     // orderBy: '',
                    //     filterMultiple: false,
                    //     filters: [{label: "有", value: "有"}, {label: "无", value: "无"}],
                    //     isSearchAble: true,
                    //     searchType: 'string'
                    // },
                        {
                        fields: ['badlabel'],
                        title: '堵点标签',
                        titleAlign: 'center',
                        filterMultiple: true,
                        filters: [{label: "无", value: "无"},{label: "赢率低", value: "赢率低"},{label: "拜访少", value: "拜访少"},{label: "拜访记录差", value: "拜访记录差"},{label: "账号不活跃", value: "账号不活跃"},{label: "报价未通过", value: "报价未通过"},{label: "承诺差", value: "承诺差"},],
                        isSearchAble: true,
                        searchType: "string"

                    },{
                        fields: ['goodlabel'],
                        title: '利好标签',
                        titleAlign: 'center',
                        filterMultiple: true,
                        filters: [{label: "无", value: "无"},{label: "高赢率", value: "高赢率"},{label: "近期有拜访记录", value: "近期有拜访记录"},{label: "近期有电话记录", value: "近期有电话记录"},{label: "近期有多个记录", value: "近期有多个记录"},{label: "账号高活跃", value: "账号高活跃"},{label: "报价单已通过", value: "报价单已通过"},{label: "销售已承诺", value: "销售已承诺"}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['approvalstatus'],
                        title: '报价单',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{label: "审批通过", value: "审批通过"},{label: "审批未通过", value: "审批未通过"}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['win_rate'],
                        title: '赢率',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{label: "0", value: "0"}],
                        isSearchAble: true,
                        searchType: "numberRange"
                    },{
                        fields: ['promise'],
                        title: '销售承诺',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{label: "承诺", value: "承诺"},{label: "争取", value: "争取"},{label: "跟进", value: "跟进"},{label: "未填写", value: "未填写"}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['close_date'],
                        title: '结单日期',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{label: "空", value: ""}],
                        isSearchAble: true,
                        searchType: 'dateRange'
                    },{
                        fields: ['update_time'],
                        title: '更新日期',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{label: "空", value: ""}],
                        isSearchAble: true,
                        searchType: 'dateRange'
                    },{
                        fields: ['money'],
                        title: '商机金额',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{label: "0", value: 0}],
                        orderBy: '',
                        isSearchAble: true,
                        searchType: 'numberRange'
                    },{
                        fields: ['sale_stage'],
                        title: '销售阶段',
                        titleAlign: 'center',
                        filterMultiple: true,
                        filters: [{label: "空", value: ""}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['customer'],
                        title: '最终客户',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{label: "空", value: ""}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['level'],
                        title: '客户级别',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{label: "空", value: ""}],
                        isSearchAble: true,
                        searchType: "string"
                    },
                    //     {
                    //     fields: ['last_visit'],
                    //     title: '最近拜访时间',
                    //     titleAlign: 'center',
                    //     orderBy: '',
                    //     // filterMultiple: false,
                    //     // filters: [{label: "空", value: ""}],
                    //     // isSearchAble: true,
                    //     // searchType: 'dateRange'
                    // },
                        {
                        fields: ['operation'],
                        title: '操作',
                        titleAlign: 'center'
                    }]]
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
                    if (field == "quzong_ok"){
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
                // 暂时用假数据代替
                // this.sourceTableData = initOpportunities(45000);
                var self = this;
                var did = getUrlKey('did', window.location.href);
                // var url = '/sale/opportunity/list/api';
                var url = '/sale/analysis/allapi';
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
                        if ("quzong_ok" === k || "last_visit" === k || "createdat" === k || "closedate" === k){
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
                        if (field == "label"){
                            if(values[0] == "有"){
                                tableData = tableData.filter(item => item[field].length > 0);
                            }else{
                            tableData = tableData.filter(item => item[field].length == 0);
                            }
                        }else if(field == "goodlabel" || field == "badlabel"){
                            tableData = this._searchMethod(tableData,values,field);
                            // return tableData;
                        }
                        else{
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
                // tableData = this._searchMethod(tableData);

                this.tableData = tableData;
                this.total = this.tableData.length;
                this.pageChange(1);
                this.setFooterData();
                this.resetConditions();
            },
            _searchOnce(tableData, searcher="",field="",label){
                var searchType = searcher.searchType;
                var columnName = searcher.columnName;
                var start = searcher.start;
                var end = searcher.end;

                if (searchType == "string" || searchType == String){
                    if (start){
                        if(columnName == "badlabel"){
                            columnName = "label"
                        }else if(columnName == "goodlabel"){
                            columnName = "good_label"
                        }
                        var re = new RegExp(start, "i");
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

                if(field != ""){
                    if(label == "badlabel"){
                        label="label"
                    }else if(label == "goodlabel"){
                        label="good_label"
                    }
                    var re = new RegExp(field, "i");
                    tableData = tableData.filter(item => re.test(item[label]))
                }

                return tableData;
            },

            _searchMethod(tableData,field="",label=""){
                var searchers = this.searchers;
                if(field !=""){
                    for(single in field){
                        tableData = this._searchOnce(tableData,"",field[single],label);
                    }
                    return tableData;
                }else {
                    for (let key in searchers) {
                        // console.log("key",key)
                        let searcher = searchers[key];
                        tableData = this._searchOnce(tableData, searcher, field);
                    }
                    return tableData;
                }
            },

            // 关键字、数字、数字范围、时间范围搜索
            searchMethod(searcher){
                let tableData = this.getTableData();

                let columnName = searcher.columnName;

                this.searchers[columnName] = searcher;

                tableData = this._filterMethod(tableData);

                tableData = this._searchMethod(tableData);

                this.tableData = tableData;
                this.total = this.tableData.length;
                this.pageChange(1);
                this.setFooterData();
                this.resetConditions();
            },
            resetConditions(){
                let self = this;
                self.conditions = {};
                for (let k in self.searchers){
                    let searcher = self.searchers[k];
                    if (searcher.start || searcher.end){
                        if (!(self.conditions[k])){
                            let name = self.tableConfig.columnDict[k];
                            let desc = "";
                            let searchType = searcher.searchType;
                            if (searchType === "string" || searchType === "number"){
                                desc = searcher.start;
                            }else if(searchType === "numberRange" || searchType === "dateRange"){
                                desc = searcher.start + "~" + searcher.end;
                            }
                            if (desc.length > 10){
                                desc = desc.substr(0, 7) + "...";
                            }
                            self.conditions[k] = name + ":" + desc;
                        }
                    }
                }
                for (let k in self.filters){
                    let filter = self.filters[k];
                    if (filter && filter.length > 0){
                        if (!(self.conditions[k])){
                            let name = self.tableConfig.columnDict[k];
                            let desc = filter.join(",");
                            if (desc.length > 10){
                                desc = desc.substr(0, 7) + "...";
                            }
                            self.conditions[k] = name + ":" + desc;
                            console.log("FFFFFFFFFFF",self.conditions[k])
                        }
                    }
                }
            },
            // 清空某一列的筛选条件
            removeCondition(k){
                console.log(this.searchers[k]);
                if (this.searchers[k]){
                    delete(this.searchers[k]);
                }
                console.log(this.filters[k]);
                if (this.filters[k]){
                    delete(this.filters[k]);
                }
                // console.log(this.searchers, this.filters);
                // this.resetConditions()
                if("undefined" == typeof filters){
                    this.filterMethod();
                }else if("undefined" == typeof searchers){
                    this.searchMethod();
                }
                let dropdown = this.getDropdown(k);
                // 重置dropdown里面的筛选条件
                dropdown.rest();
            },
            getDropdown(k){
                let dropdown = this.$refs["table1"].$refs["dropdown"].find(x => x.columnName === k);
                return dropdown;
            },
            setFilters(){
                var commonFields = ["win_rate","opportunity_name","customer", "saler", "department", "sale_stage", "level"];
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
                    }
                }
            },
            // setFooterData(){
            //     let result = [],
            //         opportunity_moneys = this.tableData.map(item => {
            //             return item.opportunity_money;
            //         });
            //     let sumVal = ["汇总"];
            //     for (let i=1; i < this.tableConfig.columns.length; i++){
            //         let col = this.tableConfig.columns[i];
            //         if ("opportunity_money" === col.field){
            //             sumVal.push(
            //                 toThousands(opportunity_moneys.reduce((prev, curr) => {
            //                     return parseInt(prev) + parseInt(curr);
            //                 }, 0))
            //             );
            //         }else{
            //             sumVal.push("-");
            //         }
            //     }
            //     result.push(sumVal);
            //     this.footer = result;
            // },
            setFooterData(){
                let opportunity_moneys = this.tableData.map(item => {
                    return item.opportunity_money;
                });
                this.opportunity_moneys = toThousands(opportunity_moneys.reduce((prev, curr) => {
                    return parseInt(prev) + parseInt(curr);
                }, 0));
            },
            setFooterCellClass(rowIndex, colIndex, value){
                if (colIndex === 0){
                    return 'footer-cell-class-name-title'
                }else{
                    return 'footer-cell-class-name-normal'
                }
            },
            get_csv(){
                url =  "/sale/analysis/csv_api"
                window.open(url);
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

// 自定义列组件
Vue.component('table-operation-opp', {
    // template:`<span>
    // <a href="" @click.stop.prevent="update(rowData, index)">编辑</a>&nbsp;
    // <a href="" @click.stop.prevent="deleteRow(rowData, index)">删除</a>
    // </span>`,
    template:`<span>
    <a href="" @click.stop.prevent="showDetail(rowData, index)">详情</a>
    </span>`,
    props:{
        rowData:{
            type:Object
        },
        field:{
            type:String
        },
        index:{
            type:Number
        }
    },
    methods:{
        showDetail(){
            let oppId = this.rowData.oid;
            oppDetailVue.showDetail(oppId,this.rowData);
        },
        update(){
            let uid = this.rowData.id;
            let url = "/sale/opportunity?id=" + uid;
            window.open(url);
        },

    }
});

var oppDetailVue = new Vue({
    el: "#drawerOpp",
    delimiters: ["[[", "]]"],
    data(){
        return {
            drawer: false,
            accountActivityLoading: true,
            salerActivityLoading :false,
            accountActivityData: {
                items: []
            },
            detail: {
                opportunity_id: "",
                opportunity_name: "",
                customer_id: "",
                customer_name: "",
            },
            analysis:{
                data:[]
            },
        }
    },
    updated:function () {


        var link = document.getElementById("opp_name_link");
        if(opp_name_link.innerHTML){
            link.href ="https://crm.xiaoshouyi.com/final/opportunity.action?id="+this.detail.opportunity_id;
            var account_link = document.getElementById("account_name_link");
            account_link.href ="http://crm.xiaoshouyi.com/final/account.action?id="+this.detail.customer_id;
            return true;
        }

        this.get_black();
        this.get_red();

    },
    methods: {

        get_red(){
            var class_name_list = ["winrate","activity","record","ms","approvalstatus","permise"];
            for (class_name_index in class_name_list){
                var class_name = class_name_list[class_name_index] + "_score";
                var wight_name =class_name_list[class_name_index] + "_wight";
                var data_str = "this.analysis."+class_name;
                // console.log("this.analysis."+class_name,)
                if(eval(data_str) || eval(data_str) == "" || eval(data_str) == 0){
                    // console.log(eval(data_str),eval("this.analysis."+wight_name)*0.6)
                    if (eval(data_str) < eval("this.analysis."+wight_name)*0.6 ){
                        //权重为0 不变色
                        // console.log(data_str,eval(data_str),data_str=="this.analysis.approvalstatus_score",eval("this.analysis."+wight_name) == 0,eval("this.analysis."+wight_name))
                        // if(data_str=="this.analysis.approvalstatus_score" && eval("this.analysis."+wight_name) == 0){}
                        // else{
                            //改变边框颜色
                            var div_str = class_name + "_div";
                            for (div_index in document.getElementsByClassName(div_str)){
                                if (isNaN(div_index)){
                                }else{
                                    // console.log(div_index)
                                    var class_value = document.getElementsByClassName(div_str)[div_index].getAttribute("class");
                                    class_value = class_value + " red_bor";
                                    document.getElementsByClassName(div_str)[div_index].setAttribute("class",class_value);
                                    }
                                }
                           //改变字体颜色
                            var el_class = document.getElementsByClassName(class_name);
                            for (index in el_class){
                                el_class[index].style="color: red";
                            }
                            // if(class_name == "permise_score"){
                            //     return true;
                            // }
                        // }
                    }else{
                            //改变边框颜色
                            var div_str = class_name + "_div";
                            for (div_index in document.getElementsByClassName(div_str)){
                                if (isNaN(div_index)){
                                }else{
                                    // console.log(div_index)
                                    var class_value = document.getElementsByClassName(div_str)[div_index].getAttribute("class");
                                    class_value = " grid-content "+ div_str + " bor ";
                                    document.getElementsByClassName(div_str)[div_index].setAttribute("class",class_value);
                                    }
                                }
                           //改变字体颜色
                            var el_class = document.getElementsByClassName(class_name);
                            for (index in el_class){
                                el_class[index].style=" ";
                            }
                    }
                }
            }
        },

        get_black(){
            var class_name_list = ["winrate","activity","record","ms","approvalstatus","permise"];
            for (class_name_index in class_name_list){
                var class_name = class_name_list[class_name_index] + "_score";
                // var wight_name =class_name_list[class_name_index] + "_wight";
                var data_str = "this.analysis."+class_name;
                if(eval(data_str|| eval(data_str) == "" || eval(data_str) == 0)){
                        //改变边框颜色
                        var div_str = class_name + "_div";
                        for (div_index in document.getElementsByClassName(div_str)){
                            if (isNaN(div_index)){
                            }else{
                                // console.log(div_index)
                                var class_value = document.getElementsByClassName(div_str)[div_index].getAttribute("class");
                                class_value = " grid-content "+ div_str + " bor ";
                                document.getElementsByClassName(div_str)[div_index].setAttribute("class",class_value);
                                }
                            }
                       //改变字体颜色
                        var el_class = document.getElementsByClassName(class_name);
                        for (index in el_class){
                            el_class[index].style=" ";
                        }
                        // //四次update只执行一次
                        // if(class_name == "permise_score"){
                        //     return true;
                        // }
                }
            }
        },

        showDetail(oppId){
            this.drawer = true;
            if (oppId != this.detail.opportunity_id){
                this._clear();
                this.getOpportunityDetail(oppId);
                this.getAccountActivityData(oppId);
                this.getAnalysisData(oppId);
            }
        },
        getOpportunityDetail(oppId){
            let url = "/sale/opportunity?id=" + oppId;
            let self = this;
            axios.get(url).then(res => {
                if (res.data.code == 1){
                    self.detail = res.data.data;
                }else{
                    this.$message.error(res.data.error);
                }

            });
        },
        getAccountActivityData(oppId){
            // let url = "/statistical/api/opp_act_info?date=30&id=" + oppId;
            let url = "/sale/analysis/tableapi?oid=" + oppId;
            let self = this;
            axios.get(url).then(res => {
                if (res.data.items && res.data.items.length > 0){
                    self.accountActivityData = res.data.items[0];
                }
                self.accountActivityLoading = false;
                // if (res.data.code == 1){
                //     console.log(res.data.data)
                //     this.detail = res.data.data;
                // }else{
                //     this.$message.error(res.data.error);
                // }
            }).catch(err => {
                console.log(err);
            });
        },
        getAnalysisData(oppId){
            let url = "analysis/api?oid=" + oppId;
            let self = this;
            axios.get(url).then(res => {
                self.analysis = res.data.data.data[0];
            }).catch(err => {
                console.log(err);
            });
        },
        _clear(){
            this.detail = {};
            this.accountActivityData = {items: []};
            this.salerActivityData = {items: []};
            this.salerRecordData = {
                visit_createdAt: "",
                call_createdAt: "",
                record_createdAt: "",
            };
        },
        toShow(){
            this.drawer = true;
        }
    }
});

// initOpportunityVue();
