function initYqmsVue(){
    new Vue({
        el: '#yqms',
        delimiters: ["[[", "]]"],
        data() {
            return {
                filters: {},
                searchers: {},
                loading: false,
                needRetry: false,
                total: 0,
                pageIndex: 1,
                pageSize: 20,
                sourceTableData: [],
                tableData: [],
                footer: [],
                conditions: {},
                tableConfig: {
                    columnDict: {
                        "account_name":"账号名称",
                        "customer_name":"最终客户",
                        "opportunity_name":"商机名称",
                        "saler_confirm":"销售确认",
                        "close_date":"结单日期",
                        "account_status":"账号状态",
                        "account_type":"账号类型",
                        "regdate":"注册日期",
                        "due_date":"到期日期",
                        "last_login_date":"最后登录",
                        "save_days":"保存天数",
                        "customer_province":"所属地域",
                        "saler":"商务",
                        "maintainer":"维护",
                        "ms_version":"账号版本",
                        "if_active":"是否活跃",
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
                        field: 'account_name',
                        width: 200,
                        columnAlign: 'center',
                        isFrozen: true,
                        // isFrozen: false,
                        // isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['account_name'];
                            let password = rowData['password'];
                            let domain_yqms = rowData['domain_yqms'];
                            if (!value){
                                return "----";
                            }else{
                                let username = $('#username').val()
                                // return "<a target='_blank' href='http://yqms-beta-g3.istarshine.com/Login/doLogin?userid=" + value + "&password=" + password + "&type=logintype" + "'>" + value + "</a>";
                                return "<a target='_blank' href='http://" + domain_yqms +".istarshine.com/Login/doLogin?userid=" + value + "&password=" + password + "&type=logintype&loguser=" + username + "'>" + value + "</a>";
                            }
                        }
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
                        field: 'opportunity_name',
                        width: 200,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['opportunity_name'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'saler_confirm',
                        width: 80,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['saler_confirm'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'close_date',
                        width: 120,
                        columnAlign: 'center',
                        isResize: true,
                        isSelect: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['close_date'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'account_status',
                        width: 80,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['account_status'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'account_type',
                        width: 120,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['account_type'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'if_active',
                        width: 80,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['if_active'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'regdate',
                        width: 120,
                        columnAlign: 'center',
                        isResize: true,
                        isSelect: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['regdate'];
                            if (!value){
                                return "----";
                            }else{
                               //var dateformate = value.substring(0,8);
                                //dateformate = dateformate.substring(0,4) + '-'+dateformate.substring(4,6)+'-'+dateformate.substring(6,8);
                                return value;
                            }
                        }
                    },{
                        field: 'due_date',
                        width: 120,
                        columnAlign: 'center',
                        isResize: true,
                        isSelect: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['due_date'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'last_login_date',
                        width: 120,
                        columnAlign: 'center',
                        isResize: true,
                        isSelect: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['last_login_date'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'save_days',
                        width: 80,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['save_days'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'customer_province',
                        width: 80,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['customer_province'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'saler',
                        width: 80,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['saler'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'maintainer',
                        width: 80,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['maintainer'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'ms_version',
                        width: 80,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['ms_version'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'operation',
                        width: 120,
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
                        fields: ['account_name'],
                        title: '账号名称',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['customer_name'],
                        title: '最终客户',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['opportunity_name'],
                        title: '商机名称',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['saler_confirm'],
                        title: '销售确认',
                        titleAlign: 'center',
                        filterMultiple: true,
                        filters: [{label: "承诺", value: "承诺"},{label: "争取", value: "争取"},{label: "跟进", value: "跟进"}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['close_date'],
                        title: '结单日期',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        isSearchAble: true,
                        searchType: 'dateRange'
                    },{
                        fields: ['account_status'],
                        title: '账号状态',
                        titleAlign: 'center',
                        filterMultiple: true,
                        filters: [{label: "正式", value: "正式"},{label: "试用", value: "试用"},{label: "停用", value: "停用"},{label: "弃用", value: "弃用"},{label: "其他", value: "其他"}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['account_type'],
                        title: '账号类型',
                        titleAlign: 'center',
                        filterMultiple: true,
                        filters: [{label: "用户", value: "用户"},{label: "员工", value: "员工"},{label: "测试", value: "测试"},{label: "系统用户", value: "系统用户"},{label: "代理商", value: "代理商"},{label: "预警用户", value: "预警用户"},{label: "项目用户", value: "项目用户"},{label: "模版用户", value: "模版用户"},{label: "态势感知创建秘书", value: "态势感知创建秘书"},{label: "其他", value: "其他"}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['if_active'],
                        title: '是否活跃',
                        titleAlign: 'center',
                        filterMultiple: true,
                        filters: [{label: "活跃", value: "活跃"},{label: "不活跃", value: "不活跃"}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['regdate'],
                        title: '注册日期',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{ value: ""}],
                        isSearchAble: true,
                        searchType: 'dateRange'
                    },{
                        fields: ['due_date'],
                        title: '到期日期',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        isSearchAble: true,
                        searchType: 'dateRange'
                    },{
                        fields: ['last_login_date'],
                        title: '最后登录',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        isSearchAble: true,
                        searchType: 'dateRange'
                    },{
                        fields: ['save_days'],
                        title: '保存天数',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        isSearchAble: true,
                        searchType: "numberRange"
                    },{
                        fields: ['customer_province'],
                        title: '所属地域',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['saler'],
                        title: '商务',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['maintainer'],
                        title: '维护',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['ms_version'],
                        title: '账号版本',
                        titleAlign: 'center',
                        filterMultiple: true,
                        filters: [{label: "秘书4.0", value: "秘书4.0"},{label: "秘书3.0", value: "秘书3.0"},{label: "秘书2.4", value: "秘书2.4"}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['operation'],
                        title: '操作',
                        titleAlign: 'center'
                    }]],
                },
                hoverClass:'1',
            }
        },
        methods: {
            getCommonFilters(field){
                var filters = [];
                var js = {};
                for (var row of this.sourceTableData){
                    var value = row[field];
                    var label = value;
                    // if (field == "quzong_ok"){
                    //     if (value){
                    //         value = value.split(" ")[0];
                    //         label = value;
                    //     }
                    // }
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
            getSourceTableData(i){
                if((i<4&&this.hoverClass<4) || (i>3&&this.hoverClass>3)){
                    this.hoverClass = i;
                    this.initTable();
                    return
                }
                this.hoverClass = i;
                var self = this;
                var did = getUrlKey('did', window.location.href);
                var url = '/product/yqms_accounts/list/api';
                var isAll = i > 3?1:0
                var index = parent.layer.load(0, {shade: false});
                axios.get(url, {
                    params: {
                        'did': did,
                        'page': 1,
                        "num": 0,
                        "all": isAll
                    }
                }).then(function(res){
                    self.sourceTableData = res.data.data.data;
                    self.initTable()
                    parent.layer.close(index);
                }).catch(function(err){
                    console.log(err);
                    self.$message.error("网络错误，请点击重试按钮");
                    // self.loading = false;
                    self.needRetry = true;
                    parent.layer.close(index);
                });
            },
            retry(){
                this.needRetry = false;
                // this.loading = true;
                this.getSourceTableData(4);
            },
            // 深拷贝原始数据
            getTableData(){
                return JSON.parse(JSON.stringify(this.sourceTableData));
            },
            pageChange(pageIndex) {
                this.pageIndex = pageIndex;
                this.getTableShowData();
                // console.log(pageIndex)
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
                        // if ("quzong_ok" === k || "last_visit" === k || "createdat" === k || "closedate" === k){
                        //     handler = stringToDateTime;
                        // }

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
                this.resetConditions();
            },
            _searchOnce(tableData, searcher){

                var searchType = searcher.searchType;
                var columnName = searcher.columnName;
                var start = searcher.start;
                var end = searcher.end;

                if (searchType == "string" || searchType == String){
                    if (start){
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
                let tableData = this.getTableData();
                // console.log("searcher",this.searchers)
                let columnName = searcher.columnName;
                
                this.searchers[columnName] = searcher;

                tableData = this._filterMethod(tableData);

                tableData = this._searchMethod(tableData);

                this.tableData = tableData;

                this.total = this.tableData.length;
                this.pageChange(1);
                this.resetConditions();
            },
            // 默认筛选条件
            defaultSearchMethod(x){
                let i = this.hoverClass
                if(x){i = 0}
                let _this = this;
                let tableData = this.getTableData();
                // 清空条件
                if (i == 0){
                    this.filters = {};
                    this.searchers = {};
                }
                // 第一个条件标签：全部用户
                else if (i == 1){
                    this.filters = {account_status:["正式", "试用"], account_type:[ "用户", "代理商", "项目用户", "态势感知创建秘书" ],};
                    this.searchers = {};
                }
                // 第二个条件标签：活跃用户
                else if (i == 2){
                    this.filters = {if_active:["活跃"], account_type:[ "用户", "代理商", "项目用户", "态势感知创建秘书" ],};
                    this.searchers = {};
                }
                // 第三个条件标签：昨日登录
                else if (i == 3){
                    var _yesterday = new Date();
                    _yesterday.setDate(_yesterday.getDate() - 1);
                    _yesterday = _yesterday.toLocaleDateString().split('/').join('-');
                    this.filters = {account_type:[ "用户", "代理商", "项目用户", "态势感知创建秘书" ],};
                    this.searchers = {last_login_date:{start: _yesterday, end: "", searchType: "dateRange", columnName: "last_login_date"},};
                }
                else if (i == 4){
                    this.filters = {account_type:[ "用户", "代理商", "项目用户", "态势感知创建秘书" ],};
                    this.searchers = {};
                }
                tableData = this._filterMethod(tableData);
                tableData = this._searchMethod(tableData);

                this.tableData = tableData;
                this.total = this.tableData.length;
                this.pageChange(1);
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
                            if (desc.length > 30){
                                desc = desc.substr(0, 27) + "...";
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
                            if (desc.length > 30){
                                desc = desc.substr(0, 27) + "...";
                            }
                            self.conditions[k] = name + ":" + desc;
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
            // setFilters(){
            //     var commonFields = ["win_rate", "saler_name", "department_name", "sale_stage_name", "level"];
            //     for (var row of this.tableConfig.titleRows){
            //         for (var item of row){
            //             var field = item["fields"][0];
            //             if (commonFields.indexOf(field) > -1){
            //                 var filters = this.getCommonFilters(field)
            //                 if ("win_rate" == field){
            //                     filters.sort(function(a, b){
            //                         return a.value - b.value
            //                     })
            //                 }
            //                 item["filters"] = filters;
            //             }
            //         }
            //     }
            // },
            setFooterCellClass(rowIndex, colIndex, value){
                if (colIndex === 0){
                    return 'footer-cell-class-name-title'
                }else{
                    return 'footer-cell-class-name-normal'
                }
            },
            initTable(){
                this.tableData = this.getTableData();
                this.defaultSearchMethod();
                this.total = this.tableData.length;
                this.getTableShowData();
                // this.setFilters();
                this.loading = false;


            }
        },
        created() {
            this.getSourceTableData(4);
        },
        watch: {
            // "sourceTableData": "initTable",
            // "customerLevelFilters": "setCustomerLevelFilters",
        }
    });
}

// 自定义列组件
// 操作列
Vue.component('table-operation-opp', {
    // template:`<span>
    // <a href="" @click.stop.prevent="update(rowData, index)">编辑</a>&nbsp;
    // <a href="" @click.stop.prevent="deleteRow(rowData, index)">删除</a>
    // </span>`,
    template:`<span>
    <a title="清除手机" href="" @click.stop.prevent="reset_phonelock(rowData, index)"><i class="iconfont icon-shouji2"></i></a>
    <a title="清除访问限制" href="" @click.stop.prevent="reset_loginlock(rowData, index)"><i class="iconfont icon-qingchu2"></i></a>
    <a title="修改账号" href="" @click.stop.prevent="reset_userinfo(rowData, index)"><i class="iconfont icon-bianji"></i></a>
    <a title="操作日志" href="" @click.stop.prevent="yqms_log(rowData, index)"><i class="iconfont icon-icon-test"></i></a>
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
            let oppId = this.rowData.opportunity_id;
            oppDetailVue.showDetail(oppId, this.rowData);
        },
        //调用清除手机接口
        reset_phonelock(){
            let uid = this.rowData.user_id;
            // console.log(uid);
            let url = '/product/yqms_accounts/clear_phone';
            // $.get(url, {
            //     clerid: uid
            // }, function(re) {
            //     var result = JSON.parse(re);
            //     layer.msg(result.msg, {
            //         icon: result.status,
            //         time: 1000
            //         })
            //     })
            $.get(url,{uid:uid},function(res){
                alert(res.message)
            })
        },
        //调用清除访问接口
        reset_loginlock(){
            let uid = this.rowData.user_id;
            // let uid = '81918';
            // console.log(uid);
            let url = '/product/yqms_accounts/reset_access_frequencylock';
            $.get(url,{uid:uid},function(res){
                // console.log(res.message);
                alert(res.message)
            })
        },

        //修改账号:新标签页打开老后台修改账号页面
        reset_userinfo(){
            let uid = this.rowData.user_id;
            let domain_support = this.rowData.domain_support;
            // let url = 'http://support-beta.istarshine.com/Upuser/editors/id/'+uid;
            let url = 'http://' + domain_support + '.istarshine.com/Upuser/editors/id/'+uid;
            window.open(url);
        },

        //新标签页打开相应账号的操作日志页面
        yqms_log(){
            let uid = this.rowData.user_id;
            let account_name = this.rowData.account_name;
            let url = '/product/yqms_accounts/yqms_log_overview?uid='+uid+'&account_name='+account_name;
            window.open(url);
        },
    }
});



$("#submitBtn").click(function(){
    reloadTable();
});
// 访问接口，并将获取到的数据重新加载到表格中
function reloadTable(url){
    if (!url){
        var query = $("#customer-list-filter-form").serialize();
        currentQuery = query;
        url = $("#customer-list-api").text().trim() +"?" + query;
    }
    // 核验表单中数据是否合法
    if (!checkForm()){
        return false;
    }
    $("#submitBtn").attr("disabled", "disabled");
    $("#submitBtn").text("加载中...");

    // 弹出层 —— 加载中特效
    var index = parent.layer.load(0, {shade: false});

    $.get(url, function(data, status){

        tableData = [];
        selectedData = [];

        if (data.status == null || data.status == undefined){
            // window.location.reload();
            return;
        }

        if (data.status < 1){
            alert(data.message);
        }

        tableData = data.items;

        function reloaded(items){
            $("#table_list_1").jqGrid('clearGridData');
            $("#table_list_1").jqGrid('setGridParam', {
                datatype: 'local',
                data: items,
                page: 1
            }).trigger("reloadGrid");
        };
        // 关闭弹出层
        parent.layer.close(index);

        reloaded(data.items);
        $("#submitBtn").attr("disabled", null);
        $("#submitBtn").text("搜索");
    });
}
// 检测表单中是否含有非法的值
function checkForm(){
    var $o = $("#login-days-input");
    var loginDays = $o.val();
    if (loginDays == null || loginDays == undefined || loginDays == ""){
        $o.val(0);
    }
    var loginDays = parseInt($o.val());
    var minNum = $o.attr("min");
    var maxNum = $o.attr("max");
    if (minNum && (loginDays < parseInt(minNum))){
        return false;
    }
    if (maxNum && (loginDays > parseInt(maxNum))){
        return false;
    }
    return true;
}
