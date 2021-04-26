

axios.defaults.headers.common['X-CSRFToken'] = $("input[name='csrfmiddlewaretoken']").val(); 
var app = new Vue({
    el: "#app",
    delimeters: ["[[", "]]"],
    data() {
        return {
            mode: null,

            canClick: false,
            checkedId: "",

            perms : [],
            treeData : [],
            defaultExpandedKeys: [],
            defaultCheckedKeys: [],
            defaultProps: {
                "treeData": "treeData",
                "pids": "pids",
                "label": "name",
                "children": "children"
            },
            ruleFormBackUp: {},
            ruleForm: {
                id: '',
                name: '',
                code: '',
                rank: 0,
                status: true,
                pids: ""
            },
            rules: {
                name: [{
                    required: true,
                    message: '请输入角色名称，可以是中文',
                    trigger: 'blur'
                }],
                code: [{
                    required: true,
                    message: '请输入角色代码，必须是英文',
                    trigger: 'blur'
                }],
                rank: [{
                    required: true,
                    message: '请输入角色排名，必须是数字',
                    trigger: 'blur'
                }],
                status: [{
                    required: true,
                    message: '请选择角色状态',
                    trigger: 'blur'
                }]
            }
        };
    },
    props: ["treeData"],

    created(){
        this.getMode();
        this.getPerms();
        // this.getRoleInfo();
    },
    methods: {
        getMode(){
            let id = getUrlKey("id", window.location.href);
            this.mode = id ? 1 : 0;
        },
        renderPage(){
            // this.getPerms();
            this.getRoleInfo();
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
        getTreeData(){
            let treeData = this.perms;
            this.treeData = treeData;
        },
        getRoleInfoApi(){
            let id = getUrlKey("id", window.location.href);
            let api = "/xman/role?id=" + id;
            return api;
        },
        getRoleInfo(){
            let self = this;
            self.ruleFormBackUp = JSON.parse(JSON.stringify(self.ruleForm));
            if (this.mode !== 1){
                return;
            }
            let url = this.getRoleInfoApi();
            axios.get(url).then(res => {
                if (res.data.code === 1){
                    self.ruleForm.id = res.data.data.id;
                    self.ruleForm.name = res.data.data.name;
                    self.ruleForm.code = res.data.data.code;
                    self.ruleForm.rank = String(res.data.data.rank);
                    self.ruleForm.status = res.data.data.status;

                    self.ruleFormBackUp = JSON.parse(JSON.stringify(self.ruleForm));

                    self.defaultCheckedKeys = res.data.data.pids;
                }else{
                    self.$message.error(res.data.error);
                }
            }).catch(err => {
                self.$message.error(err);
            })
        },
        getCheckedNodes() {
          return this.$refs.tree.getCheckedNodes();
        },
        getCheckedKeys() {
          return this.$refs.tree.getCheckedKeys();
        },
        setCheckedNodes() {
          this.$refs.tree.setCheckedNodes([]);
        },
        setCheckedKeys() {
          this.$refs.tree.setCheckedKeys([]);
        },
        resetChecked() {
          this.$refs.tree.setCheckedKeys([]);
        },
        addPerm(){
            let url = "/xman/perm";
            window.location.href = url;
        },
        canSubmit(){
            try {
                let ok = compareTwoObjects(this.ruleForm, this.ruleFormBackUp)
                this.canClick = !ok;
            }catch(e){
                this.$message.error(e);
            }
            
        },
        submitForm(formName) {
            var self = this;
            let pids = [];
            for (let p of self.getCheckedKeys()){
                if (/^\d+$/.test(p)){
                    pids.push(p);
                }
            };
            self.ruleForm.pids = pids.join(",");
            let form = JSON.parse(JSON.stringify(self.ruleForm));
            form.pids = pids.join(",");
            if (form.status){
                form.status = 1;
            }else{
                form.status = 0;
            }
            self.$refs[formName].validate((valid) => {
                if (valid) {
                    let url = "/xman/role";
                    let data = Qs.stringify(form);

                    function good(res){
                        if (res.data.code === 1){
                            self.$message.success(res.data.error);
                            let id = res.data.data.id;
                            let url = "/xman/role/detail?id=" + id;
                            window.location.href = url;
                        }else{
                            self.$message.error(res.data.error);
                        }
                    }
                    function bad(err){
                        self.$message.error(err);
                    }

                    if (self.mode === 0){
                        axios.post(url, data).then(good).catch(bad);
                    }else if(self.mode === 1){
                        axios.put(url, data).then(good).catch(bad);
                    }

                } else {
                    console.log('error submit!!');
                    return false;
                }
            });
        },
        resetForm(formName) {
            this.$refs[formName].resetFields();
            this.resetChecked();
            this.ruleForm.pids = "";
        }
    },
    computed: {
        ruleFormData(){
            return Qs.stringify(this.ruleForm);
        }
    },
    watch: {
        perms: "getTreeData",
        ruleFormData: "canSubmit",
        mode: "renderPage"
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
            let id = getUrlKey("id", window.location.href);
            let url = "/xman/role?id=" + id;

            // 当http方法是DELETE的时候，后台只能用request.GET获取参数
            // 所以需要将参数写在url后面
            axios.delete(url).then(res => {
                if (res.data.code === 1){
                    self.$message.success(res.data.error)
                    let url = "/xman/role/list";
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
            let url = "/xman/role";
            window.location.href = url;
        }
    }
});
