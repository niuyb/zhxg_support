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
                        field: 'opportunity_name',
                        width: 300,
                        columnAlign: 'center',
                        isFrozen: true,
                        // isFrozen: false,
                        // isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['opportunity_name'];
                            let oid = rowData["opportunity_id"];
                            if (!value){
                                return "----";
                            }else{
                                return "<a target='_blank' href='https://crm.xiaoshouyi.com/final/opportunity.action?id=" + oid + "'>" + value + "</a>";
                            }
                        }
                    },{
                        field: 'createdat',
                        width: 120,
                        columnAlign: 'center',
                        isResize: true,
                        isSelect: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['createdat'];
                            if (!value){
                                return "----";
                            }else{
                                return value.split(" ")[0];
                            }
                        }
                    },{
                        field: 'closedate',
                        width: 120,
                        columnAlign: 'center',
                        isResize: true,
                        isSelect: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['closedate'];
                            if (!value){
                                return "----";
                            }else{
                                return value.split(" ")[0];
                            }
                        }
                    },{
                        field: 'saler_name',
                        width: 80,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true
                    },{
                        field: 'department_name',
                        width: 80,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true
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
                        field: 'level',
                        width: 90,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true
                    },{
                        field: 'opportunity_money',
                        width: 120,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            return toThousands(rowData["opportunity_money"])
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
                        field: 'sale_stage_name',
                        width: 180,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true
                    },{
                        field: 'quzong_ok',
                        width: 160,
                        columnAlign: 'center',
                        isResize: true,
                        isSelect: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['quzong_ok'];
                            if (!value){
                                return "----";
                            }else{
                                return value.split(" ")[0];
                            }
                        }
                    },{
                        field: 'last_visit',
                        width: 140,
                        columnAlign: 'center',
                        isFrozen: false,
                        isResize: true,
                        formatter: function(rowData, index, pagingIndex){
                            var value = rowData['last_visit'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }
                    },{
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
                        filterMultiple: true,
                        filters: [{label: "空", value: ""}],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['createdat'],
                        title: '创建日期',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{label: "空", value: ""}],
                        isSearchAble: true,
                        searchType: 'dateRange'
                    },{
                        fields: ['closedate'],
                        title: '结单日期',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{label: "空", value: ""}],
                        isSearchAble: true,
                        searchType: 'dateRange'
                    },{
                        fields: ['saler_name'],
                        title: '商务',
                        titleAlign: 'center',
                        filterMultiple: true,
                        filters: [],
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
                        fields: ['customer_name'],
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
                    },{
                        fields: ['opportunity_money'],
                        title: '商机金额',
                        titleAlign: 'center',
                        filterMultiple: false,
                        filters: [{label: "0", value: 0}],
                        orderBy: '',
                        isSearchAble: true,
                        searchType: 'numberRange'
                    },{
                        fields: ['win_rate'],
                        title: '赢率',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{label: "100", value: "100"}, {label: "0", value: "0"}],
                        isSearchAble: true,
                        searchType: "numberRange"
                    },{
                        fields: ['sale_stage_name'],
                        title: '销售阶段',
                        titleAlign: 'center',
                        filterMultiple: true,
                        filters: [],
                        isSearchAble: true,
                        searchType: "string"
                    },{
                        fields: ['quzong_ok'],
                        title: '区总确认归档日期',
                        titleAlign: 'center',
                        orderBy: '',
                        filterMultiple: false,
                        filters: [{label: "空", value: ""}],
                        isSearchAble: true,
                        searchType: 'dateRange'
                    },{
                        fields: ['last_visit'],
                        title: '最近拜访时间',
                        titleAlign: 'center',
                        orderBy: '',
                        // filterMultiple: false,
                        // filters: [{label: "空", value: ""}],
                        // isSearchAble: true,
                        // searchType: 'dateRange'
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
                var commonFields = ["win_rate", "saler_name", "department_name", "sale_stage_name", "level"];
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
            let oppId = this.rowData.opportunity_id;
            oppDetailVue.showDetail(oppId, this.rowData);
        },
        update(){
            let uid = this.rowData.id;
            let url = "/sale/opportunity?id=" + uid;
            window.open(url);
        },
        _delete(){

            let uid = this.rowData.id;
            let url = "/sale/opportunity/delete?id=" + uid;
            axios.get(url).then(res => {
                if (res.data.code === 1){
                    this.$message.success(res.data.error)
                    app.getSourceTableData();
                }else{
                    this.$message.error(res.data.error)
                }
            }).catch(function(err){
                console.log(err)
            });
        },
        deleteRow(){
            let self = this;
            self.$confirm('确认删除这条名称为"' + self.rowData.username + '"的商机吗？')
            .then(_ => {
                self._delete();
            }).catch(_ => {});
        }
    }
});

var oppDetailVue = new Vue({
    el: "#drawerOpp",
    delimiters: ["[[", "]]"],
    data(){
        return {
            drawer: false,
            accountActivityLoading: true,
            accountActivityData: {
                items: []
            },

            salerActivityLoading: true,
            salerActivityData: {
                items: []
            },
            salerRecordData: {
                visit_createdAt: "",
                call_createdAt: "",
                record_createdAt: "",
            },
            detail: {
                opportunity_id: "",
                opportunity_name: "",
                customer_id: "",
                customer_name: "",
            }
        }
    },
    methods: {
        showDetail(oppId){
            this.drawer = true;
            if (oppId != this.detail.opportunity_id){
                this._clear();
                this.getOpportunityDetail(oppId);
                this.getAccountActivityData(oppId);
                this.getSalerActivityData(oppId);
                this.getSalerRecordData(oppId);
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
            let url = "/statistical/api/opp_act_info?date=30&id=" + oppId;
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
        getSalerRecordData(oppId){
            let self = this;
            let url, _url = "/statistical/api/opp_record_info?time_long=30&opportunity_id=" + oppId;
            // 获取签到拜访数据
            url = _url + "&entity_type=4173079";
            axios.get(url).then(res => {
                if (res.data.items.length > 0)
                self.salerRecordData.visit_createdAt = res.data.items[0].createdAt;
            });
            // 获取电话拜访数据
            url = _url + "&entity_type=4173078";
            axios.get(url).then(res => {
                if (res.data.items.length > 0)
                self.salerRecordData.call_createdAt = res.data.items[0].createdAt;
            });
            // 获取快速记录数据
            url = _url + "&entity_type=-11";
            axios.get(url).then(res => {
                if (res.data.items.length > 0)
                self.salerRecordData.record_createdAt = res.data.items[0].createdAt;
            });
        },
        getSalerActivityData(oppId){
            let url = "/statistical/api/opp_record_list?time_long=30&opportunity_id=" + oppId;
            let self = this;
            axios.get(url).then(res => {
                self.salerActivityData = res.data;
                self.salerActivityLoading = false;
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
