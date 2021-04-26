axios.defaults.headers.common['X-CSRFToken'] = $("input[name='csrfmiddlewaretoken']").val(); 

var app = new Vue({
    el: '#app',
    delimiters: ["[[", "]]"],
    data() {
      return {
        users: [],
        userTooltip: "",

        currentRow: null,

        materialListLoading: true,
        materialListVisible: false,

        sourceTableData: [],
        tableData: [],
        multipleSelection: [],

        // paginator
        currentPage: 1,
        pageSize: 5,
        pageSizes: [5, 10, 20, 50, 100, 200, 500, 1000],
        totalNum: 0,

        search: "",

        // 控制表格当前页数据的加载
        signal: null
      }
    },
    created(){
        this.getSourceTableData();
    },
    methods: {
        getSourceTableData(){
            let self = this;

            let url = "/user_center/material/list";
            axios.get(url).then(function(res){

                self.sourceTableData = [];
                self.sourceTableData = res.data.data;

                // 运行getTableData函数
                self.currentPage = 1;
                self.setSignal();
                
                self.materialListLoading = false;
                
            }).catch(function(err){
                console.log(err);
                
                self.materialListLoading = false;
                
            })
        },
        getTableData(){
            // if (this.sourceTableData && this.sourceTableData.length > 0){
            //     console.log(this.sourceTableData[0]);
            // }
            
            let search = this.search;
            let tempTableData = this.sourceTableData.filter(data => !search || 
                    data.name.toLowerCase().includes(search.toLowerCase()) || 
                    data.title.toLowerCase().includes(search.toLowerCase()));

            this.totalNum = tempTableData.length;
            this.tableData = tempTableData.slice(
                    this.pageSize * (this.currentPage - 1), this.pageSize * this.currentPage);
        },
        filterHandler(value, row, column){
            console.log(value);
            console.log(row);
            console.log(column);
            const property = column['property'];
            return row[property] === value;
        },

        // paginator
        handleSizeChange(val){
            this.pageSize = val;
            this.currentPage = 1;
            this.setSignal();          
        },
        handleCurrentChange(val){
            this.currentPage = val;
            this.setSignal();
        },
        handleSearch(){
            this.currentPage = 1;
            this.setSignal();
        },
        handleChoose(index, row){
            // let id = row.id;
            // let url = "/user_center/material-detail?id=" + id;
            // window.location.href = url;
            let that = this;
            that.currentRow = row;
            
            $("#messageTitle").val(row.title);
            $("#messageTitle").text(row.title);
            $("#messageContent").val(row.comment);
            $("#messageContent").text(row.comment);
            $("#messageUrl").val(window.location.origin + row.url);
            $("#messageUrl").text(window.location.origin + row.url);

            that.materialListVisible = false;
            $("#messageModal").modal();
        },
        setSignal(){
            console.log("setSignal");
            this.signal = Math.random()
        }
    },
    watch: {
        search: "setSignal",
        signal: "getTableData"
    }
});
