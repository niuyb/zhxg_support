var app = new Vue({
    el: '#app',
    data() {
        return {
            filters: {},
            searchers: {},
            loading: true,
            total: 0,
            pageIndex: 1,
            pageSize: 20,
            sourceTableData: [],
            tableData: [],
            footer: [],
            tableConfig: {
                titleBgColor: "#eee",
                multipleSort: false,
                tableData: [],
                columns: [{
                    field: 'id',
                    width: 100,
                    columnAlign: 'left',
                    isFrozen: true
                },{
                    field: 'name',
                    width: 60,
                    columnAlign: 'left',
                    isFrozen: false,
                    isResize: true,
                    formatter: function(rowData, index, pagingIndex){
                        let value = rowData['name'];
                        let id = rowData.id;
                        if (!value){
                            return "----";
                        }else{
                            return "<a href='/xman/module?id=" + id + "'>" + value + "</a>";
                        }
                    }
                },{
                    field: 'code',
                    width: 200,
                    columnAlign: 'left',
                    isFrozen: false,
                    isResize: true
                },{
                    field: 'status',
                    width: 200,
                    columnAlign: 'left',
                    isFrozen: false,
                    isResize: true
                },{
                    field: 'rank',
                    width: 200,
                    columnAlign: 'left',
                    isFrozen: false,
                    isResize: true
                },{
                    field: 'parent',
                    width: 200,
                    columnAlign: 'left',
                    isFrozen: false,
                    isResize: true
                },{
                    field: 'operation',
                    width: 80,
                    columnAlign: 'center',
                    isFrozen: false,
                    isResize: true,
                    componentName:'table-operation'
                }],
                titleRows: [[{
                    fields: ['id'],
                    title: 'ID',
                    titleAlign: 'center',
                    // orderBy: '',
                },{
                    fields: ['name'],
                    title: '??????',
                    titleAlign: 'center',
                    filterMultiple: false,
                    filters: [{label: "???", value: ""}],
                    isSearchAble: true,
                    searchType: 'string'
                },{
                    fields: ['code'],
                    title: '??????',
                    titleAlign: 'center',
                    filterMultiple: false,
                    filters: [{label: "???", value: ""}],
                    isSearchAble: true,
                    searchType: 'string'
                },{
                    fields: ['status'],
                    title: '??????',
                    titleAlign: 'center'
                },{
                    fields: ['rank'],
                    title: '??????',
                    titleAlign: 'center'
                },{
                    fields: ['parent'],
                    title: '????????????',
                    titleAlign: 'center',
                    filterMultiple: false,
                    filters: [{label: "???", value: ""}],
                    isSearchAble: true,
                    searchType: 'string'
                },{
                    fields: ['operation'],
                    title: '??????',
                    titleAlign: 'center',
                }]],
            }
        }
    },
    methods: {
        // ????????????????????????????????????????????????????????????????????????????????????
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
                    label = "???";
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
        // ??????????????????????????????
        getSourceTableData(){
            // ????????????????????????
            // this.sourceTableData = initCustomers(45000); 
            var self = this;
            var did = getUrlKey('did', window.location.href);
            var url = '/xman/module/list/api';
            axios.get(url, {
                params: {
                    'did': did,
                    'page': 1,
                    "num": 0
                }
            }).then(function(res){
                self.sourceTableData = res.data.data;
            }).catch(function(err){
                console.log(err)
            });
        },
        // ?????????????????????
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
                    if ("date_joined" === k || "last_login" === k){
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

        // ??????????????????????????????????????????????????????
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
            var commonFields = ["customer_level", "saler_name"];
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
            let sumVal = ["??????"];
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
        },
        customCompFunc(params){

            console.log(params);

            if (params.type === 'delete'){ // do delete operation

                this.$delete(this.tableData,params.index);

            }else if (params.type === 'edit'){ // do edit operation

                alert(`?????????${params.index} ?????????${params.rowData['name']}`)
            }

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

// ??????????????????
Vue.component('table-operation',{
    template:`<span>
    <a href="" @click.stop.prevent="update(rowData,index)">??????</a>&nbsp;
    <a href="" @click.stop.prevent="deleteRow(rowData,index)">??????</a>
    </span>`,
    props:{
        rowData:{
            type: Object
        },
        field:{
            type: String
        },
        index:{
            type: Number
        }
    },
    methods:{
        update(){

           // ????????????????????????????????????
        //    let params = {type: 'edit', index: this.index, rowData: this.rowData};
        //    this.$emit('on-custom-comp', params);
            let id = this.rowData.id;
            let url = "/xman/module?id=" + id;
            window.open(url);
        },
        _delete(){

            let id = this.rowData.id;
            let url = "/xman/module?id=" + id;
            axios.delete(url).then(res => {
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
            self.$confirm('???????????????????????????"' + self.rowData.name + '"???????????????')
            .then(_ => {
                self._delete();
            }).catch(_ => {});
        }
    }
});


var bg = new Vue({
    el: "#button-group",
    data(){
        return {
            refreshing: false
        }
    },
    methods: {
        refresh(){
            var self = this;
            this.refreshing = true;
            app.getSourceTableData();
            setTimeout(function(){self.refreshing = false;}, 3000);
        },
        create(){
            let url = "/xman/module";
            window.open(url);
        }
    }
});
