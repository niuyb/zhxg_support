
axios.defaults.headers.common['X-CSRFToken'] = $("input[name='csrfmiddlewaretoken']").val(); 

var app = new Vue({
    el: '#app',
    delimiters: ["[[", "]]"],
    data() {
      return {
        tableFields: {
            username: {name: "用户名称", show: 1},
            dtalkid: {name: "钉钉id", show: 0},
            mobile: {name: "手机号", show: 0},
            status: {name: "状态", show: 1},
            departments: {name: "部门", show: 1},
            departments_top: {name: "上级部门", show: 1},
            position: {name: "职位", show: 1},
            role_names: {name: "角色", show: 1},
            email: {name: "邮箱", show: 0},
            is_superuser: {name: "超级管理员", show: 1},
            is_staff: {name: "后台管理", show: 0},
            last_login: {name: "最近登录", show: 0},
            operation: {name: "操作", show: 1},
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
        getSourceTableData(){
            let self = this;
            let status = getUrlKey("status", window.location.href);
            if (!status){
                status = "";
            }

            let url = "/xman/user/list?status=" + status + "&rand=" + Math.random();
            axios.get(url).then(function(res){

                self.sourceTableData = [];
                self.sourceTableData = res.data.data;

                // 运行getTableData函数
                self.currentPage = 1;
                self.setSignal();
                //bg.refreshing = false;
            }).catch(function(err){
                console.log(err);
                bg.refreshing = false;
            })
        },
        getTableData(){
            if (this.sourceTableData && this.sourceTableData.length > 0){
            }
            
            let search = this.search;
            let tempTableData = this.sourceTableData.filter(data => !search || 
                    data.username.toLowerCase().includes(search.toLowerCase()) || 
                    data.mobile.toLowerCase().includes(search.toLowerCase()) || 
                    data.position.toLowerCase().includes(search.toLowerCase()) || 
                    data.role_names.toLowerCase().includes(search.toLowerCase()) || 
                    // data.permission_names.toLowerCase().includes(search.toLowerCase()) || 
                    data.departments.toLowerCase().includes(search.toLowerCase()) ||
                    data.departments_top.toLowerCase().includes(search.toLowerCase()));
            this.totalNum = tempTableData.length;

            // console.log(tempTableData[0]);
            this.tableData = tempTableData.slice(
                    this.pageSize * (this.currentPage - 1), this.pageSize * this.currentPage);
            bg.refreshing = false;
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
        columnShowOrNot(key){
            this.tableFields[key].show = !this.tableFields[key].show;
        },
        changeStatus(index, row){
            let self = this;
            let url = "/xman/user";
            let _row = JSON.parse(JSON.stringify(row));
            if (_row.status){
                _row.status = 1;
            }else{
                _row.status = 0;
            }
            console.log(_row);
            return;
            let data = Qs.stringify(_row);

            axios.put(url, data).then(function(res){
                let msg = "状态修改失败";
                if (res.data.code == 1){
                    if (row.status){
                        msg = "用户\"" + row.name + "\"成功启用";
                    }else{
                        msg = "用户\"" + row.name + "\"成功禁用";
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
            let url = "/xman/user/list?uids=" + ids.join(",");
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
                self.$message.warning("请选择需要删除的用户.");

                //
                bg.deleting = false;
                return;
            }

            let ids = [];
            let usernames = [];

            self.multipleSelection.forEach(item => {
                ids.push(item.id);
                usernames.push(item.username);
            });

            self.$confirm('确认要删除用户 "' + usernames.join(",") + '" 吗？')
            .then(_ => {
                self._multipleDelete(ids);
            }).catch(_ => {bg.deleting = false;});
        },
        // 批量授权、分配角色等
        multipleAccess(index, row){
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
            let id = row.id;
            let url = "/xman/user/detail?id=" + id;
            window.location.href = url;
        },
        handleDelete(index, row){
            let self = this;
            let ids = [row.id];
            let username = row.username;
            self.$confirm('确认要删除用户 "' + username + '" 吗？')
            .then(_ => {
                self._multipleDelete(ids);
            }).catch(_ => {});
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
    delimiters: ["[[", "]]"],
    data(){
        return {
            popover: {
                title: "",
                width: 800
            },
            usersChecked: false,
            canClick: false,

            roles: [],
            perms: [],
            roleTree: {
                data: [],
                defaultExpandedKeys: [],
                defaultCheckedKeys: [],
                defaultProps: {}
            },
            permTree: {
                data: [],
                defaultExpandedKeys: [],
                defaultCheckedKeys: [],
                defaultProps: {
                    "label": "name",
                    "children": "children"
                }
            },
            ruleFormBackUp: {},
            ruleForm: {
                uids: "",
                rids: "",
                pids: "",
                role_type: '1',
            },
            rules: [],

            refreshing: false,
            deleting: false,
            tableFields: app.tableFields
        }
    },
    methods: {
        initialRuleFormBackUp(){
            this.ruleFormBackUp = JSON.parse(JSON.stringify(this.ruleForm));
        },
        refresh(){
            let self = this;
            this.refreshing = true;
            app.getSourceTableData();
            // setTimeout(function(){self.refreshing = false;}, 3000);
        },
        create(){
            let url = "/xman/user";
            window.open(url);
        },
        getPerms(){
            let self = this;
            let url = "/xman/pure/perm/tree/api";        
            axios.get(url).then(function(res){
                self.perms = res.data.data;
            }).catch(function(err){
                console.log(err)
            });
        },
        addPerm(){
            let url = "/xman/perm";
            window.location.href = url;
        },
        getRoles(){
            let self = this;
            let url = "/xman/role/list?rand=" + Math.random();        
            axios.get(url).then(function(res){
                self.roles = res.data.data;
            }).catch(function(err){
                console.log(err)
            });
        },
        addRole(){
            let url = "/xman/role";
            window.location.href = url;
        },
        getRoleTreeData(){
            let treeData = [];
            for (let r of this.roles){
                let rid = r.id;
                let name = r.name;
                let child = {'rid': rid, label: name}
                treeData.push(child);
            }
            this.roleTree.data = treeData;
        },
        getPermTreeData(){
            let treeData = this.perms;
            this.permTree.data = treeData;
        },

        multipleDelete(){
            this.deleting = true;
            app.multipleDelete();
        },
        multipleAccess(ids){

            //app.multipleAccess();
        },
        columnShowOrNot(key){
            app.columnShowOrNot(key);
        },
        resetChecked() {
            this.$refs.roleTree.setCheckedKeys([]);
            this.$refs.permTree.setCheckedKeys([]);
        },
        getUsers(){
            return app.multipleSelection || [];
        },
        checkUsers(){
            let self = this;
            let users = self.getUsers();
            if (users && users.length > 0){
                self.usersChecked = true;
                self.popover.title = "为用户增加角色和权限";
                self.popover.width = 800;
                return true;
            }else{
                self.usersChecked = false;
                self.popover.title = "请选择需要授权的用户！";
                self.popover.width = 400;
                setTimeout(self.clickAccessButton, 2000);
                return false;
            }            
        },
        submitForm(formName) {
            let self = this;
            let users = self.getUsers();
            let uids = [];
            for (let user of users){
                if (user.id != null){
                    uids.push(user.id);
                }
            }
            
            let roles = self.$refs.roleTree.getCheckedKeys();
            let rids = [];
            for (let role of roles){
                if (role != null){
                    rids.push(role);
                }
            }
            let perms = self.$refs.permTree.getCheckedKeys();
            let pids = [];
            for (let perm of perms){
                if (perm != null){
                    pids.push(perm);
                }
            }
            
            if (uids.length == 0){
                self.$message.warning("您还未选择用户");
                return false;
            }

            if (rids.length === 0 && pids.length === 0){
                self.$message.warning("请选择需要授与用户的权限或者角色");
                return false;
            }

            let role_type = self.ruleForm.role_type;

            let url = "/xman/user/list";
            let form = {
                "uids": uids.join(","),
                "rids": rids.length ? rids.join(",") : "",
                "pids": pids.length ? pids.join(",") : "",
                "role_type": role_type,
            };
            // console.log(form);
            let data = Qs.stringify(form);
            axios.patch(url, data).then(res => {
                if (res.data.code === 1){
                    self.$message.success(res.data.error);
                }else{
                    self.$message.error(res.data.error);
                }
                self.clickAccessButton();
            }).catch(function(err){
                self.$message.error(err);
            });
        },
        resetForm(formName) {
            this.$refs[formName].resetFields();
            this.resetChecked();
        },
        clickAccessButton(){
            let button = $("#accessButton");
            button.click();
        }
    },
    created(){
        this.getRoles();
        this.getPerms();
    },
    computed: {
        ruleFormData(){
            return Qs.stringify(this.ruleForm);
        }
    },
    watch: {
        roles: "getRoleTreeData",
        perms: "getPermTreeData" 
    }
});
