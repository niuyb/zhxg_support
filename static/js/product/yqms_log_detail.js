function initYqms4LogVue(){
    new Vue({
        el: '#yqms4_log',
        delimiters: ["[[", "]]"],
        data() {
            return {
                filters: {},
                searchers: {},
                loading: true,
                needRetry: false,
                total: 0,
                pageIndex: 1,
                pageSize: 10,
                sourceTableData: [],
                tableData: [],
                footer: [],
                conditions: {},
                tableConfig: {
                    columnDict: {
                        "operate_time":"操作时间",
                        "platform":"操作平台",
                        "phone":"手机号",
                        "mod1_name":"一级模块",
                        "mod2_name":"二级模块",
                        "request_body":"请求体",
                        "ip":"ip",
                        "ip_location": "ip地域信息",
                    },
                    multipleSort: false,
                    tableData: [],
                    columns: [{
                        field: 'custome',
                        width: 60,
                        titleAlign: 'center',
                        columnAlign: 'center',
                        formatter: function(rowData, index, pagingIndex) {
                            var currentIndex = index + pagingIndex;
                            return currentIndex + 1
                        },
                        isFrozen: true
                    },{
                        field: 'operate_time',
                        width: 120,
                        columnAlign: 'center',
                        isResize: true,
                        isSelect: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['operate_time'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'platform',
                        width: 30,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['platform'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'phone',
                        width: 60,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['phone'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'mod1_name',
                        width: 40,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['mod1_name'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'mod2_name',
                        width: 80,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['mod2_name'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'request_body',
                        width: 80,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['request_body'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'ip',
                        width: 60,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['ip'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'ip_location',
                        width: 60,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['ip_location'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    }],
                    titleRows: [[{
                        fields: ['custome'],
                        title: '序号',
                        titleAlign: 'center',
                        // orderBy: '',
                    },{
                        fields: ['operate_time'],
                        title: '操作时间',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        orderBy: '',
                        isSearchAble: true,
                        searchType: "dateRange"
                    },{
                        fields: ['platform'],
                        title: '操作平台',
                        titleAlign: 'center',
                        filterMultiple: true,
                        filters: [{label: "PC", value: "PC"},{label: "APP", value: "APP"}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['phone'],
                        title: '手机号',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['mod1_name'],
                        title: '一级模块',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['mod2_name'],
                        title: '二级模块',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['request_body'],
                        title: '请求体',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['ip'],
                        title: 'ip',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['ip_location'],
                        title: 'ip地域信息',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        isSearchAble: true,
                        searchType: "string"
                    }]],
                },
                logDate4:'',
            }
        },
        methods: {
            getCommonFilters(field){
                var filters = [];
                var js = {};
                for (var row of this.sourceTableData){
                    var value = row[field];
                    var label = value;
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
                var uid = getUrlKey('uid', window.location.href);   // 获取当前页面的url中的uid的值

                var log_date = $('#log_date4').val();
                if(!log_date){
                    log_date = getUrlKey('log_date', window.location.href);   // 获取当前页面的url中的log_date的值
                }else{
                    log_date = log_date.replace("-","");
                    log_date = log_date.replace("-","");
                }
                self.logDate4 = log_date.slice(0,4)+'-'+log_date.slice(4,6)+'-'+log_date.slice(6,8);
                // 延迟显示，ui时间组件渲染异步
                setTimeout(function () {
                    $('#log_date4').val(self.logDate4)
                }, 0)
                var url = '/product/yqms_accounts/yqms4_log_detail_api?uid='+uid+'&log_date='+log_date;
                axios.get(url, {
                    params: {
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
                console.log("filters",filters)
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
                console.log("searcher",this.searchers)
                let columnName = searcher.columnName;

                this.searchers[columnName] = searcher;

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
                            console.log("SSSSSSSSSSSSSS",self.conditions[k])
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
            setFooterCellClass(rowIndex, colIndex, value){
                if (colIndex === 0){
                    return 'footer-cell-class-name-title'
                }else{
                    return 'footer-cell-class-name-normal'
                }
            },
            // 选择日期插件datepicker
            _datepicker(){
                $('#data_4 .input-daterange').datepicker({
                    keyboardNavigation: false,
                    forceParse: false,
                    autoclose: true,
                    // minDate: new Date(2020, 1, 1),
                    // maxDate: new Date(),
                    viewDate:new Date(),
                });

                $('#data_4 .input-daterange').datepicker("setDate", new Date());
            },

            initTable(){
                this.tableData = this.getTableData();
                this.total = this.tableData.length;
                this.getTableShowData();
                this._datepicker();
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




function initYqms3LogVue(){
    new Vue({
        el: '#yqms3_log',
        delimiters: ["[[", "]]"],
        data() {
            return {
                filters: {},
                searchers: {},
                loading: true,
                needRetry: false,
                total: 0,
                pageIndex: 1,
                pageSize: 10,
                sourceTableData: [],
                tableData: [],
                footer: [],
                conditions: {},
                tableConfig: {
                    columnDict: {
                        "operate_time":"操作时间",
                        "platform":"操作平台",
                        "phone":"手机号",
                        "mod1_name":"一级模块",
                        "mod2_name":"二级模块",
                        "param":"请求参数",
                        "ip":"ip",
                        "ip_location": "ip地域信息",
                    },
                    multipleSort: false,
                    tableData: [],
                    columns: [{
                        field: 'custome',
                        width: 60,
                        titleAlign: 'center',
                        columnAlign: 'center',
                        formatter: function(rowData, index, pagingIndex) {
                            var currentIndex = index + pagingIndex;
                            return currentIndex + 1
                        },
                        isFrozen: true
                    },{
                        field: 'operate_time',
                        width: 120,
                        columnAlign: 'center',
                        isResize: true,
                        isSelect: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['operate_time'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'platform',
                        width: 30,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['platform'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'phone',
                        width: 60,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['phone'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'mod1_name',
                        width: 40,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['mod1_name'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'mod2_name',
                        width: 80,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['mod2_name'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'param',
                        width: 80,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['param'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'ip',
                        width: 60,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['ip'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
                        field: 'ip_location',
                        width: 60,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['ip_location'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    }],
                    titleRows: [[{
                        fields: ['custome'],
                        title: '序号',
                        titleAlign: 'center',
                        // orderBy: '',
                    },{
                        fields: ['operate_time'],
                        title: '操作时间',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        orderBy: '',
                        isSearchAble: true,
                        searchType: "dateRange"
                    },{
                        fields: ['platform'],
                        title: '操作平台',
                        titleAlign: 'center',
                        filterMultiple: true,
                        filters: [{label: "PC", value: "PC"},{label: "APP", value: "APP"},{label: "微信", value: "微信"}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['phone'],
                        title: '手机号',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['mod1_name'],
                        title: '一级模块',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['mod2_name'],
                        title: '二级模块',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['param'],
                        title: '请求参数',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['ip'],
                        title: 'ip',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['ip_location'],
                        title: 'ip地域信息',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{value: ""}],
                        isSearchAble: true,
                        searchType: "string"
                    }]],
                },
                logDate3:'',
            }
        },
        methods: {
            getCommonFilters(field){
                var filters = [];
                var js = {};
                for (var row of this.sourceTableData){
                    var value = row[field];
                    var label = value;
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
                var uid = getUrlKey('uid', window.location.href);   // 获取当前页面的url中的uid的值

                var log_date = $('#log_date3').val();
                if(log_date == null || log_date =='' || log_date==undefined || log_date =='undefined'){
                    log_date = getUrlKey('log_date', window.location.href);   // 获取当前页面的url中的log_date的值
                }else{
                    log_date = log_date.replace("-","");
                    log_date = log_date.replace("-","");
                }
                self.logDate3 = log_date.slice(0,4)+'-'+log_date.slice(4,6)+'-'+log_date.slice(6,8);
                // 延迟显示，ui时间组件渲染异步
                setTimeout(function () {
                    $('#log_date3').val(self.logDate3)
                }, 0)
                var url = '/product/yqms_accounts/yqms3_log_detail_api?uid='+uid+'&log_date='+log_date;
                axios.get(url, {
                    params: {
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
                console.log("filters",filters)
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
                console.log("searcher",this.searchers)
                let columnName = searcher.columnName;

                this.searchers[columnName] = searcher;

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
                            console.log("SSSSSSSSSSSSSS",self.conditions[k])
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
            setFooterCellClass(rowIndex, colIndex, value){
                if (colIndex === 0){
                    return 'footer-cell-class-name-title'
                }else{
                    return 'footer-cell-class-name-normal'
                }
            },
            // 选择日期插件datepicker
            _datepicker(){
                $('#data_3 .input-daterange').datepicker({
                    keyboardNavigation: false,
                    forceParse: false,
                    autoclose: true,
                    viewDate:new Date()

                });
                $('#data_3 .input-daterange').datepicker("setDate",new Date());
            },

            initTable(){
                this.tableData = this.getTableData();
                this.total = this.tableData.length;
                this.getTableShowData();
                this._datepicker();
                this.loading = false;

            }
        },
        created() {
            this.getSourceTableData();
        },
        watch: {
            "sourceTableData": "initTable",
        }
    });
}


