
axios.defaults.headers.common['X-CSRFToken'] = $("input[name='csrfmiddlewaretoken']").val(); 
var app = new Vue({
    el: "#app",
    delimiters: ["[[", "]]"],
    data(){
        var checkMobile = (rule, value, callback) => {
          if (!value) {
            return callback();
          }
          setTimeout(() => {
            if (!Number.isInteger(value)) {
              callback(new Error('请输入数字值'));
            } else {
              if (len(String(value)) === 0 || len(String(value)) != 11){
                callback(new Error('请输入正确的手机号或者留空'));
              } else {
                callback();
              }
            }
          }, 1000);
        };
        var validatePass = (rule, value, callback) => {
          if (value === '') {
            callback(new Error('密码不能为空'));
          } else {
            if (this.ruleForm.checkPass !== '') {
              this.$refs.ruleForm.validateField('checkPass');
            }
            callback();
          }
        };
        var validatePass2 = (rule, value, callback) => {
          if (value === '') {
            callback(new Error('请再次输入密码'));
          } else if (value !== this.ruleForm.password) {
            callback(new Error('两次输入密码不一致!'));
          } else {
            callback();
          }
        };
        var validateMobile = (rule, value, callback) => {
            if (value === ""){
                callback(new Error('手机号不能为空'));
            }else if(!(/^1\d{10}$/.test(value))){
                callback(new Error('请输入11位手机号'));
            }else{
                callback();
            }
        };
        return {
            // canClick: false,
            canClick: true,
            checkedId: "",
            dingframes: [],
            checked: false,
            roles: [],
            perms: [],
            roleTree: {
                data: [],
                defaultExpandedKeys: [],
                defaultCheckedKeys: [],
                defaultProps: []
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
            direction: 'rtl',
            ruleFormBackUp: {},
            ruleForm: {
                id: '',
                username: '',
                password: '',
                checkPass: '',
                mobile: '',
                email: '',
                avatar: '',
                is_superuser: 0,
                is_staff: 0,
                status: 1,
                dtalkid: '',
                dingframe: '',
                position: '',
                rids: '',
                pids: '',
            },
            rules: {
                username: [
                    {required: true, message: '用户名不能为空', trigger: 'blur'},
                    {min: 1, max: 20, message: '长度在 1 到 20 个字符', trigger: 'blur'}
                ],
                password: [
                    {validator: validatePass, trigger: 'blur', required: true}
                ],
                checkPass: [
                    {validator: validatePass2, trigger: 'blur', required: true}
                ],
                dtalkid: [
                    {required: true, message: '钉钉ID不能为空', trigger: 'blur'}
                ],
                dingframe: [
                    {required: true, message: '钉钉部门不能为空', trigger: 'blur'}
                ],
                mobile: [
                    {required: true, trigger: 'blur', validator: validateMobile}
                ],
                status: [
                    {required: true, message: '用户状态必填', trigger: 'blur'}
                ],
            }
        }
    },
    methods: {
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
        addRole(){
            let url = "/xman/role";
            window.location.href = url;
        },
        getPermTreeData(){
            let treeData = this.perms;
            this.permTree.data = treeData;
        },
        getCheckedNodes() {
          return this.$refs.tree.getCheckedNodes();
        },
        setCheckedNodes() {
          this.$refs.tree.setCheckedNodes([]);
        },
        getRoleCheckedKeys() {
          return this.$refs.roleTree.getCheckedKeys();
        },
        getPermCheckedKeys() {
          return this.$refs.permTree.getCheckedKeys();
        },
        setRoleCheckedKeys() {
            this.$refs.roleTree.setCheckedKeys([]);
        },
        setPermCheckedKeys() {
            this.$refs.permTree.setCheckedKeys([]);
        },

        resetChecked() {
            this.$refs.roleTree.setCheckedKeys([]);
            this.$refs.permTree.setCheckedKeys([]);
        },
        handleClose(done){
            this.$confirm('确认关闭？')
            .then(_ => {
                done();
            })
            .catch(_ => {});
        },
        unRequiredRules(){
            this.rules.password = [];
            this.rules.checkPass = [];
        },
        canSubmit(){
            let ok = compareTwoObjects(this.ruleForm, this.ruleFormBackUp);
            this.canClick = !ok;
        },
        submitForm(formName) {
            var self = this;
            let pids = [];
            for (let p of self.getPermCheckedKeys()){
                if (/^\d+$/.test(p)){
                    pids.push(p);
                }
            };
            let form = JSON.parse(JSON.stringify(self.ruleForm));
            form.pids = pids.join(",");
            form.rids = self.getRoleCheckedKeys().join(",");
            if (form.is_superuser){
                form.is_superuser = 1;
            }else{
                form.is_superuser = 0;
            }
            if (form.is_staff){
                form.is_staff = 1;
            }else{
                form.is_staff = 0;
            }

            self.$refs[formName].validate((valid) => {
                if (valid) {
                    let url = "/xman/user";
                    let data = Qs.stringify(form);

                    function good(res){
                        if (res.data.code === 1){
                            self.$message.success(res.data.error);
                            let pid = res.data.data.id;
                            let url = "/xman/user/detail?id=" + pid;
                            window.location.href = url;
                        }else{
                            self.$message.error(res.data.error);
                        }
                    }

                    function bad(err){
                        self.$message.error(err);
                    }

                    if (self.ruleForm.id){
                        // 修改数据，使用PUT方法
                        axios.put(url, data).then(good).catch(bad);
                    }else{
                        // 创建数据，使用POST方法
                        axios.post(url, data).then(good).catch(bad);
                    }
                } else {
                    console.log('error submit!!');
                    return false;
                }
            });
        },
        resetForm(){
            this.$refs[formName].resetFields();
            this.resetChecked();
            this.ruleForm.rids = '';
            this.ruleForm.pids = '';
        },
        getDingFrames(){
            this.dingframes = [{label: "----", value: ""}, {value: "111111111111", label: "自由人"}];
        },
        getUserInfo(){
            this.ruleFormBackUp = JSON.parse(JSON.stringify(this.ruleForm));
            let self = this;
            let id = getUrlKey("id", window.location.href);
            if (!id){
                return;
            }
            let url = "/xman/user?id=" + id;
            axios.get(url).then(res => {
                if (res.data.code === 1){
                    let info = res.data.data;
                    self.ruleForm.id = info.id;
                    self.ruleForm.username = info.username;
                    self.ruleForm.mobile = info.mobile;
                    self.ruleForm.email = info.email;
                    self.ruleForm.avatar = info.avatar;
                    self.ruleForm.is_superuser = info.is_superuser;
                    self.ruleForm.is_staff = info.is_staff;
                    self.ruleForm.status = info.status;
                    self.ruleForm.dtalkid = info.dtalkid;
                    self.ruleForm.dingframe = info.dingframe;
                    self.ruleForm.position = info.position;
                    self.ruleForm.rids = info.rids.join(",");
                    self.ruleForm.pids = info.pids.join(",")

                    self.ruleFormBackUp = JSON.parse(JSON.stringify(self.ruleForm));

                    self.roleTree.defaultCheckedKeys = info.rids;
                    self.permTree.defaultCheckedKeys = info.pids;
                }else{
                    self.$message.error(res.data.error);
                }
            }).catch(err => {
                self.$message.error(err);
            })
        }
    },
    created(){
        this.getDingFrames();
        this.getRoles();
        this.getPerms();
        this.getUserInfo();
    },
    computed: {
        ruleFormId(){
            return this.ruleForm.id;
        },
        ruleFormData(){
            return Qs.stringify(this.ruleForm)
        }
    },
    watch: {
        roles: 'getRoleTreeData',
        perms: 'getPermTreeData',
        ruleFormId: "unRequiredRules",
        // ruleFormData: "canSubmit"
    }
});

var bg = new Vue({
    el: "#button-group",
    data(){
        return {
            bgShow: false,
            refreshing: false
        }
    },
    created(){
        let id = getUrlKey("id", window.location.href);
        if (id){
            this.bgShow = true;
        }
    },
    methods: {
        _delete(){
            let self = this;
            let pid = getUrlKey("id", window.location.href);
            let url = "/xman/user?id=" + pid;

            // 当http方法是DELETE的时候，后台只能用request.GET获取参数
            // 所以需要将参数写在url后面
            axios.delete(url).then(res => {
                if (res.data.code === 1){
                    self.$message.success(res.data.error);
                    let url = "/xman/user/list";
                    setTimeout(function(){
                        window.location.href = url;
                    }, 1000);                    
                }else{
                    self.$message.error(res.data.error);
                }
            }).catch(function(err){
                console.log(err)
            });
        },
        dlt(){
            let self = this;
            self.$confirm('确认要删除吗？')
            .then(_ => {
                self._delete();
            }).catch(_ => {});
        },
        create(){
            let url = "/xman/user";
            window.location.href = url;
        }
    }
});
