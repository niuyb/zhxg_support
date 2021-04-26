var salerKpiMixin = {
    delimiters: ["[[", "]]"],
    data() {
        return {
            canExport: $("#can-export").text() == 1,
            showDatePicker: $("#table-source-api").text().indexOf("month") !== -1,
            showSalerSelector: $("#table-source-api").text().indexOf("history") !== -1,

            exporting: false,

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
            tableConfig: {}
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
        getDate(){            
            this.date = getUrlKey("date", window.location.href);
        },
        getParams(){
            let self = this;
            let date = self.date;
            let istarshine_id = self.istarshine_id;

            let did = getUrlKey('did', window.location.href);
            // if (!date){
            //     date = dateToString(new Date(new Date() - 3600 * 24 * 1000))
            // }
            // self.date = date;
            let params = {
                    'istarshine_id': istarshine_id || "",
                    'date': date || "",
                    'did': did,
                    'page': 1,
                    "num": 0
                }
            return params;
        },

        // 从服务器获取原始数据
        getSourceTableData(){
            let self = this;
            let params = self.getParams();
            let url = $("#table-source-api").text();
            console.log(url);
            axios.get(url, {
                "params": params
            }).then(function(res){
                self.sourceTableData = res.data.data;
            }).catch(function(err){
                console.log(err);
                self.$message.error("网络错误，请点击重试按钮");
                self.loading = false;
                self.needRetry = true;
            });
        },
        getSalers(){
            let self = this;
            let url = "/sale/saler/list/api";
            axios.get(url).then(res => {
                if (res.data.code === 1){
                    self.salers = res.data.data;
                }else{
                    self.$message.error(res.data.error);
                }
            }).catch(err => {
                self.$message.error(err);
            })
        },
        getSalerInfo(){
            if (this.sourceTableData && this.sourceTableData.length > 0){ 
                this.salerInfo = this.sourceTableData[0]
            }
        },
        getDropdown(k){
            let dropdown = this.$refs["table1"].$refs["dropdown"].find(x => x.columnName === k);
            return dropdown;
        },

        _removeCondition(k){
            // this.filters[k] = null;
            if(this.filters[k]){
                delete(this.filters[k]);
            }

            // this.resetConditions();

            if (this.searchers[k]){
                delete(this.searchers[k]);
            }

            // this.resetConditions();
            this.searchMethod();
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
            console.log(this.searchers, this.filters);
            // this.resetConditions();
            this.searchMethod();
            let dropdown = this.getDropdown(k);
            // 重置dropdown里面的筛选条件
            dropdown.rest();
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
                    }
                }
            }
        },
        expt(){
            let self = this;
            self.exporting = true;

            let url = "";
            if (self.showDatePicker){
                url = "/sale/saler/kpi/month/export";
            }
            if (self.showSalerSelector){
                url = "/sale/saler/kpi/history/export";
            }
            
            let params = self.getParams();
            params.fields = "fields=saler,level,ownerid,istarshine_id,hiredate,join_days,department_name,parent_name,job_name," +
            "month_confirm_money,month_fight_money,month_complete_money," +
            "month_new_goal,month_renew_goal,month_goal,month_new_performance,month_renew_performance,month_performance," + 
            "month_renew_goal,month_call_num,week_call_num,month_visit_num,week_visit_num," + 
            "ms_trial_num,ms_month_active_num,ms_month_new_num,ms_week_new_num,ts_trial_num," + 
            "ts_ month_active_num,ts_month_new_num,ts_week_new_num,ctime";

            url = url + "?" + Qs.stringify(params)
            window.open(url);
            // bg.exporting = false;
            self.exporting = false;
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
                    if ("hiredate" === k || "ctime" === k){
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

            this.resetConditions();
        },
        _searchOnce(tableData, searcher){

            var searchType = searcher.searchType;
            var columnName = searcher.columnName;
            var start = searcher.start;
            var end = searcher.end;

            if (searchType == "string" || searchType == String){

                start = start || "";
                end = end || "";
                // 去除空格
                start = start.replace(/(^\s*)|(\s*$)/g, "");
                end = end.replace(/(^\s*)|(\s*$)/g, "");
                
                if (start){
                    var re = new RegExp(start, "i");
                    // console.log(start);
                    // console.log(re);
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
            
            if (searcher){
                let columnName = searcher.columnName;
                this.searchers[columnName] = searcher;
            }            

            tableData = this._filterMethod(tableData);

            tableData = this._searchMethod(tableData);

            this.tableData = tableData;

            this.total = this.tableData.length;
            this.pageChange(1);
            // this.setFooterData();
            this.resetConditions();
        },
        setFilters(){
            var commonFields = ["saler", "department_name", "parent_name", "job_name"];
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
        // 从url中解析参数，生成searchers和filters
        //http://127.0.0.1/sale/saler/kpi/month?istarshine_id=&date=2020-08-03&did=&page=1&num=0&performance=10~100,90&saler={%22columnName%22:%22saler%22,%22searchType%22:%22string%22,%22start%22:%22%E4%B8%81%22,%22end%22:%22%22}
        parseUrl(){
            let self = this;
            let url = window.location.href;
            let query = window.location.search.substring(1);
            let ps = query.split("&");
            for (let p of ps){
                let kv = p.split("=");
                let k = kv[0];
                let v = kv[1];
                if (v){
                    try {
                        self.searchers[k] = JSON.parse(decodeURI(v));
                    }catch(e){
                        console.log(e);
                        console.log(k, v);
                    }
                }
            }
            // self.resetConditions();
            self.searchMethod();
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

            this.parseUrl();

            // 包装一下dropdown的rest函数，执行完之后，调用table的_removeCondition函数
            let self = this;
            for (let dropdown of self.$refs["table1"].$refs["dropdown"]){
                let rest = dropdown.rest;
                let k = dropdown.columnName;
                let newRest = function(){
                    rest();
                    try{
                        self._removeCondition(k);
                        // this.$emit("_removeCondition", k);
                    }catch(e){
                        console.log(e);
                    }
                    // this.$emit("_removeCondition", k);
                }
                dropdown.rest = newRest;
            }
        }
    },
    computed: {
        exportDisabled(){
            return !(this.sourceTableData && (this.sourceTableData.length > 0));
        }
    },
    // created() {
    //     this.getSourceTableData();
    //     if (this.showSalerSelector){
    //         this.getSalers();
    //     }
    // },
    // watch: {
    //     "istarshine_id": "getSourceTableData",
    //     "date": "getSourceTableData",
    //     "sourceTableData": "initTable",
    //     // "conditions": "filterMethod"
    //     // "customerLevelFilters": "setCustomerLevelFilters",
    // }
}

