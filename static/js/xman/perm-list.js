

axios.defaults.headers.common['X-CSRFToken'] = $("input[name='csrfmiddlewaretoken']").val(); 

var app = new Vue({
    el: '#app',
    delimiters: ["[[", "]]"],
    data() {
      return {
        users: [],
        roles: [],
        userTooltip: "",
        roleTooltip: "",

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
        getSourceTableData(){
            let self = this;

            let url = "/xman/perm/list/api";
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
            let search = this.search;
            let tempTableData = this.sourceTableData.filter(data => !search || 
                    data.name.toLowerCase().includes(search.toLowerCase()) || 
                    data.code.toLowerCase().includes(search.toLowerCase()) || 
                    data.module.full_name.toLowerCase().includes(search.toLowerCase()));
            this.totalNum = tempTableData.length;
            this.tableData = tempTableData.slice(
                    this.pageSize * (this.currentPage - 1), this.pageSize * this.currentPage);
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
            let url = "/xman/perm";
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
                        msg = "权限\"" + row.name + "\"成功启用";
                    }else{
                        msg = "权限\"" + row.name + "\"成功禁用";
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
            let url = "/xman/perm/list?pids=" + ids.join(",");
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
                self.$message.warning("请选择需要删除的权限.");

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

            self.$confirm('确认要删除权限 "' + names.join(",") + '" 吗？')
            .then(_ => {
                self._multipleDelete(ids);
            }).catch(_ => {bg.deleting = false;});
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
        handleEdit(index, row){
            let id = row.id;
            let url = "/xman/perm?id=" + id;
            window.location.href = url;
        },
        getUsers(pid){
            let self = this;

            let url = "/xman/perm/info/api?id=" + pid;
            axios.get(url).then(res => {
                if (res.data.code === 1){
                    self.users = res.data.data.users;
                }else{
                    self.$message.error(res.data.error);
                } 

                if (!self.users || self.users.length === 0){
                    self.userTooltip = "无人拥有此权限";
                }                
            }).catch(err => {
                self.$message.error(err);
                self.userTooltip = "查询失败.";
            });
        },
        showUsers(index, row){
            let pid = row.id;
            if (pid != null){
                this.userTooltip = "正在查询，请稍等...";
                this.getUsers(pid);
            }
        },
        getRoles(pid){
            let self = this;

            let url = "/xman/perm/info/api?id=" + pid;
            axios.get(url).then(res => {
                if (res.data.code === 1){
                    self.roles = res.data.data.roles;
                }else{
                    self.$message.error(res.data.error);
                }

                if (!self.roles || self.roles.length === 0){
                    self.roleTooltip = "无人拥有此角色";   
                }        
            }).catch(err => {
                self.$message.error(err);
                self.roleTooltip = "查询失败.";
            });
        },
        showRoles(index, row){
            let pid = row.id;
            if (pid != null){
                this.roleTooltip = "正在查询，请稍等...";
                this.getRoles(pid);
            }
        },
        handleDelete(index, row){
            let self = this;
            let ids = [row.id];
            let name = row.name;
            self.$confirm('确认要删除权限 "' + name + '" 吗？').then(res => {
                self._multipleDelete(ids);
            }).catch(err => {
                self.$message.error(err);
            })
        },
        handleSearch(){
            this.currentPage = 1;
            this.setSignal();
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
            let url = "/xman/perm";
            window.open(url);
        },
        multipleDelete(){
            this.deleting = true;
            app.multipleDelete();
        },
        multipleAccess(){
            this.$message.info("开发中");
        }
    }
});
