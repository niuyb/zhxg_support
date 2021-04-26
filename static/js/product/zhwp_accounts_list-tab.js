function initZhwpVue(){
    new Vue({
        el: '#zhwp',
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
                        "custom":"序号",
                        "sysuserid":"用户ID",
                        "org_name":"机构名称",
                        "crmName":"客户名称",
                        "org_type":"客户状态",
                        "customerType":"账号类型",
                        "created_time":"创建日期",
                        "expire_time":"到期日期",
                        "saleName":"商务",
                        "weeknum":"7天登陆",
                        "operations":"操作"




                    },
                    multipleSort: false,
                    tableData: [],
                    columns: [{
                        field: 'custome',
                        width: 100,
                        titleAlign: 'center',
                        columnAlign: 'center',
                        formatter: function(rowData, index, pagingIndex) {
                            var currentIndex = index + pagingIndex;
                            return currentIndex + 1
                            // return currentIndex < 3 ? '<span style="color:red;font-weight: bold;">' + (currentIndex + 1) + '</span>': currentIndex + 1
                        },
                        // isFrozen: true
                    },{
                        field:'sysuserid',
                        width:150,
                        titleAlign: 'center',
                        columnAlign: 'center',
                        formatter:function (rowData,index,pagingIndex){
                            var value = rowData['sysuserid'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }

                    },{
                        field:'org_name',
                        width:150,
                        titleAlign: 'center',
                        columnAlign: 'center',
                        formatter:function (rowData,index,pagingIndex){
                            var value = rowData['org_name'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }

                    },{
                        field:'crmName',
                        width:200,
                        titleAlign: 'center',
                        columnAlign: 'center',
                        formatter:function (rowData,index,pagingIndex){
                            var value = rowData['crmName'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }

                    },{
                        field:'org_type',
                        width:50,
                        titleAlign: 'center',
                        columnAlign: 'center',
                        formatter:function (rowData,index,pagingIndex){
                            var value = rowData['org_type'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }

                    },{
                        field:'customerType',
                        width:150,
                        titleAlign: 'center',
                        columnAlign: 'center',
                        formatter:function (rowData,index,pagingIndex){
                            var value = rowData['customerType'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }

                    },{
                        field:'created_time',
                        width:150,
                        titleAlign: 'center',
                        columnAlign: 'center',
                        formatter:function (rowData,index,pagingIndex){
                            var value = rowData['created_time'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }

                    },{
                        field:'expire_time',
                        width:150,
                        titleAlign: 'center',
                        columnAlign: 'center',
                        formatter:function (rowData,index,pagingIndex){
                            var value = rowData['expire_time'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }

                    },{
                        field:'saleName',
                        width:150,
                        titleAlign: 'center',
                        columnAlign: 'center',
                        formatter:function (rowData,index,pagingIndex){
                            var value = rowData['saleName'];
                            if (!value){
                                return "----";
                            }else{
                                return value;
                            }
                        }

                    },{
                        field:'weeknum',
                        width:150,
                        titleAlign: 'center',
                        columnAlign: 'center',
                        formatter:function (rowData,index,pagingIndex){
                            var value = rowData['weeknum'];
                            if (!value){
                                return "0";
                            }else{
                                return value;
                            }
                        }

                    },{
                        field: 'operations',
                        width: 100,
                        columnAlign: 'center',
                        componentName:'table-operations-opp'
                    }],
                    titleRows: [[{
                            fields: ['custome'],
                            title: '序号',
                            titleAlign: 'center',
                            // orderBy: '',
                        },{
                            fields: ['sysuserid'],
                            title: '用户ID',
                            titleAlign: 'center',

                        },{
                            fields: ['org_name'],
                            title: '机构名称',
                            titleAlign: 'center',

                        },{
                            fields: ['crmName'],
                            title: '客户名称',
                            titleAlign: 'center',

                        },{
                            fields: ['org_type'],
                            title: '客户状态',
                            titleAlign: 'center',

                        },{
                            fields: ['customerType'],
                            title: '账号类型',
                            titleAlign: 'center',

                        },{
                            fields: ['created_time'],
                            title: '创建日期',
                            titleAlign: 'center',

                        },{
                            fields: ['expire_time'],
                            title: '到期日期',
                            titleAlign: 'center',


                        },{
                            fields: ['saleName'],
                            title: '商务',
                            titleAlign: 'center',


                        },{
                            fields: ['weeknum'],
                            title: '7天登陆',
                            titleAlign: 'center',


                        },
                        {
                            fields: ['operations'],
                            title: '操作',
                            titleAlign: 'center',


                        }
                    ]]
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
            getTableShowDataList() {
                this.tableConfig.tableData = this.tableData.slice((this.pageIndex - 1) * this.pageSize, (this.pageIndex) * this.pageSize)
            },

            // 根据各筛选条件、和排序条件，获取当前页面的数据，进行展示
            getTableShowData() {
                const _this = this;
                _this.loading = true;
                var url = '/product/zhwp_accounts_list_api';
                axios.get(url, {
                    params: {
                        'pageNo': _this.pageIndex,
                         'pageSize': _this.pageSize
                    }
                })
                .then(
                     res => {
                        _this.loading = false;
                        if (res.data.code == 1) {

                            this.tableConfig.tableData = res.data.data.data;


                        }
                    },
                    err => {
                        _this.loading = false;
                    }
                    );
            },
            // 从服务器获取原始数据
            getSourceTableData(){
                var self = this;
                var did = getUrlKey('did', window.location.href);
                var url = '/product/zhwp_accounts_list_api';
                axios.get(url, {
                    params: {
                        'did': did,
                        'page': 1,
                        "num": 10
                    }
                }).then(function(res){
                     // console.log(res.data.data.data);
                     // return false;
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
                console.log("searcher",searcher)
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
                            if (desc.length > 10){
                                desc = desc.substr(0, 7) + "...";
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
                var url = '/product/zhwp_accounts_list_count';
                axios.get(url, {

                })
                .then(
                 res => {
                    this.total = res.data;
                 },
                err => {
                    _this.loading = false;
                }
                );

                this.getTableShowDataList();
                // this.setFilters();
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
// 操作列
Vue.component('table-operations-opp', {
    template:`<span>
    <!--<a title="修改账号" href="" @click.stop.prevent="reset_userinfo(rowData, index)"><i class="iconfont icon-bianji"></i></a>-->
    <a title="修改账号" href="" ><i class="iconfont icon-bianji"></i></a>
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



        //修改账号:新标签页打开老后台修改账号页面
        reset_userinfo(){
            let uid = this.rowData.sysuserid;
            $('#modifyCompetitorModal').addClass("modal fade in");
            $('#modifyCompetitorModal').css("display","block");

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

    // 关闭弹框
    function closewindow(){

        $('#modifyCompetitorModal').css("display","none");

    }
    // 修改提交
    function closewindow(){

        $('#modifyCompetitorModal').css("display","none");

    }



