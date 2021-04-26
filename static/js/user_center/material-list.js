
axios.defaults.headers.common['X-CSRFToken'] = $("input[name='csrfmiddlewaretoken']").val(); 

var app = new Vue({
    el: '#app',
    delimiters: ["[[", "]]"],
    data() {
      return {
        users: [],
        userTooltip: "",

        currentRow: null,

        materialChangeFormVisible: false,
        materialChangeForm: {
            name: "",
            title: "",
            typ: "0",
            url: "",
            comment: "",
            username: "",
            created_at: "",
        },

        materialUploading: false,
        materialUploadFormVisible: false,
        materialUploadPercent: 0,
        materialUploadForm: {
            title: "",
            typ: "0",
            comment: "",
            file: null
        },
        formLabelWidth: '120px',

        materialUploader: {
            action: "/upload",
            data: null,
            fileList: [],
        },

        sourceTableData: [],
        tableData: [],
        multipleSelection: [],

        // paginator
        currentPage: 1,
        pageSize: 10,
        pageSizes: [10, 20, 50, 100, 200, 500, 1000],
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
        uploadFile(){
            let that = this;
            that.materialUploading = true;
            let url = "/user_center/material";
            let form = document.forms.namedItem("materialUploadForm");
            let formData = new FormData(form);
            
            formData.append("title", that.materialUploadForm.title);
            formData.append("typ", that.materialUploadForm.typ);
            formData.append("comment", that.materialUploadForm.comment);
            
            axios({
                "method": "post",
                "url": url, 
                "data": formData, 
                "headers": {
                    "Content-Type": 'multipart/form-data'
                },
                onUploadProgress: function(progressEvent){
                    if (progressEvent.lengthComputable){
                        let loaded = progressEvent.loaded,
                            total = progressEvent.total;

                        that.$nextTick(() => {
                            that.materialUploadPercent = (loaded / total) * 100;
                        })
                    }
                }
            }).then(res => {
                that.materialUploading = false;
                if (res.data.code == 1){
                    that.$message.success(res.data.error);
                    that.materialUploadFormVisible = false;
                }else{
                    that.$message.error(res.data.error);
                };
            }).catch(err => {
                that.materialUploading = false;
                that.$message.error(err);
            })
        },
        getSourceTableData(){
            let self = this;

            let url = "/user_center/material/list";
            axios.get(url).then(function(res){

                self.sourceTableData = [];
                self.sourceTableData = res.data.data;

                // 运行getTableData函数
                self.currentPage = 1;
                self.setSignal();
                bg.refreshing = false;
            }).catch(function(err){
                console.log(err);
                bg.refreshing = false;
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
        toggleSelection(rows) {
            if (rows) {
                rows.forEach(row => {
                    this.$refs.multipleTable.toggleRowSelection(row);
                });
            } else {
                this.$refs.multipleTable.clearSelection();
            }
        },
        handleSelectionChange(val) {
            this.multipleSelection = val;
        },
        changeStatus(index, row){
            let self = this;
            let url = "/user_center/material";
            let _row = {"id": row.id};

            if (row.status){
                _row.status = 1;
            }else{
                _row.status = 0;
            }

            let data = Qs.stringify(_row);

            axios.patch(url, data).then(function(res){
                let msg = "状态修改失败";
                if (res.data.code == 1){
                    if (row.status){
                        msg = "资料\"" + row.name + "\"成功启用";
                    }else{
                        msg = "资料\"" + row.name + "\"成功禁用";
                    }
                    self.$message.success(msg);                
                }else{
                    msg = msg + "，" + res.data.error.split("，")[1];
                    self.$message.error(msg);
                    row.status = !row.status;
                }            
            }).catch(function(err){
                self.$message.error(err);
                row.status = !row.status;
            });
        },

        _multipleDelete(ids){
            let self = this;
            let _ids = ids.join(",");
            let url = "/user_center/material/list?ids=" + _ids;
            
            axios.delete(url).then(res => {
                if (res.data.code === 1){
                    self.$message.success(res.data.error);

                    // 刷新表格数据
                    bg.refresh();
                }else{
                    self.$message.error(res.data.error);
                }

                // 
                bg.deleting = false;
            }).catch(err => {
                self.$message.error(err);

                //
                bg.deleting = false;
            });
        },
        // 批量删除
        multipleDelete(){
            let self = this;
            if (!self.multipleSelection || self.multipleSelection.length === 0){
                self.$message.warning("请选择需要删除的资料.");

                //
                bg.deleting = false;
                return;
            }

            let ids = [];
            let names = [];

            self.multipleSelection.forEach(item => {
                ids.push(item.id);
                names.push(item.name);
            });

            self.$confirm('确认要删除资料 "' + names.join(",") + '" 吗？')
            .then(_ => {
                self._multipleDelete(ids);
            }).catch(_ => {bg.deleting = false;});
        },
        multipleAccess(){
            let self = this;
            setTimeout(function(){
                self.$message.info("开发中");
            }, 3000);
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
        handleEdit(index, row){
            // let id = row.id;
            // let url = "/user_center/material-detail?id=" + id;
            // window.location.href = url;
            let that = this;
            that.currentRow = row;

            for (let k in row){
                let v = row[k];
                if (k === "typ"){
                    v = String(v)
                }
                that.materialChangeForm[k] = v;
            };
            that.materialChangeFormVisible = true;
        },
        editFile(){
            let that = this;
            let url = "/user_center/material";
            let qs = Qs.stringify(that.materialChangeForm);

            axios.patch(url, qs).then(res => {
                if (res.data.code === 1){
                    that.$message.success(res.data.error);

                    for (let k in res.data.data){
                        let v = res.data.data[k];
                        that.currentRow[k] = v;
                    }
                    
                    that.materialChangeFormVisible = false;
                }else{
                    that.$message.error(res.data.error);
                }
            }).catch(err => {
                that.$message.error(err);
            })
        },
        handleDelete(index, row){
            let self = this;
            let ids = [row.id];
            let name = row.name;
            self.$confirm('确认要删资料 "' + name + '" 吗？').then(res => {
                self._multipleDelete(ids);
            }).catch(err => {
                self.$message.error(err);
            })
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


var bg = new Vue({
    el: "#button-group",
    data(){
        return {
            refreshing: false,
            deleting: false,
        }
    },
    methods: {
        refresh(){
            var self = this;
            this.refreshing = true;
            app.getSourceTableData();
            // setTimeout(function(){self.refreshing = false;}, 3000);
        },
        create(){
            app.materialUploadFormVisible = true;
        },
        multipleDelete(){
            this.deleting = true;
            app.multipleDelete();
        },
        multipleAccess(){
            app.multipleAccess();
        }
    }
});
