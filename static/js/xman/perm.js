

axios.defaults.headers.common['X-CSRFToken'] = $("input[name='csrfmiddlewaretoken']").val(); 

var app = new Vue({
    el: "#app",
    delimeters: ["[[", "]]"],
    data() {
        return {
            // submit button
            canClick: false,

            checkedId: "",
            moduleTree: {
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
                id: '',
                name: '',
                code: '',
                status: true,
                rank: 0,
                module: ''
            },
            rules: {
                name: [{
                    required: true,
                    message: '请输入权限名称，可以是中文',
                    trigger: 'blur'
                }],
                module: [{
                    required: true,
                    message: '请选择此权限所属模块',
                    // trigger: 'change'
                }],
                code: [{
                    required: true,
                    message: '请输入权限英文代码，不能含有空格',
                    trigger: 'blur'
                }],
                status: [{
                    required: true,
                    message: '请选择此权限所属应用',
                    trigger: 'change'
                }],
                rank: [{
                    required: true,
                    message: '请输入此权限的顺序',
                    trigger: 'change'
                }]
            }
        };
    },
    created(){
        this.getPermInfo();
        this.getModuleTree();
    },
    methods: {
        getPermInfo(){
            this.ruleFormBackUp = JSON.parse(JSON.stringify(this.ruleForm));
            let id = getUrlKey("id", window.location.href);
            if (id){
                let self = this;
                console.log("mode: change.");
                let url = "/xman/perm/info/api?id=" + id;
                axios.get(url).then(function(res){
                    let perm = res.data.data;
                    for (let k in self.ruleForm){
                        self.ruleForm[k] = perm[k];
                    }
                    self.ruleFormBackUp = JSON.parse(JSON.stringify(self.ruleForm));
                }).catch(function(err){
                    self.$message.error(err);
                })
            }else{
                console.log("mode: add.")
            }
        },
        getModuleTree(){
            // 这步的意思是，判断是创建还是修改
            let id = getUrlKey("id", window.location.href);
            if (id){
                // do nothing.
            }else{
                let self = this;
                let url = "/xman/module/tree/all/api";
                axios.get(url).then(function(res){
                    self.moduleTree.data = res.data.data;
                }).catch(function(err){
                    console.log(err)
                });
            }
        },
        handleNodeClick(item, checked, node) {
            if(checked === true) {
                this.checkedId = item.id;
                this.$refs.moduleTree.setCheckedKeys([item.id]);
            } else {
                if (this.checkedId == item.id) {
                    this.$refs.moduleTree.setCheckedKeys([]);
                    this.checkedId = "";
                }
            };
            this.ruleForm.module = this.checkedId;
        },
        getModuleCheckedNodes() {
          return this.$refs.moduleTree.getCheckedNodes();
        },
        getModuleCheckedKeys() {
          return this.$refs.moduleTree.getCheckedKeys();
        },
        setModuleCheckedNodes() {
          this.$refs.moduleTree.setCheckedNodes([]);
        },
        setModuleCheckedKeys() {
          this.$refs.moduleTree.setCheckedKeys([]);
        },
        unRequiredRules(){
            this.rules.module = [];
        },
        canSubmit(){
            let ok = compareTwoObjects(this.ruleForm, this.ruleFormBackUp)
            this.canClick = !ok;
        },
        addModule(){
            let url = "/xman/module";
            window.location.href = url;
        },
        submitForm(formName) {
            var self = this;

            this.$refs[formName].validate((valid) => {
                if (valid) {
                    let url = "/xman/perm";
                    let form = JSON.parse(JSON.stringify(self.ruleForm));

                    if (typeof form.module == "object"){
                        form.module = form.module.id;
                    }

                    if (form.status){
                        form.status = 1
                    }else{
                        form.status = 0
                    }
                    let data = Qs.stringify(form);
                    function good(res){
                        if (res.data.code === 1){
                            self.$message.success(res.data.error);
                            let pid = res.data.data.id;
                            let url = "/xman/perm?id=" + pid;
                            window.location.href = url;
                        }else{
                            self.$message.error(res.data.error);
                        }
                    }
                    function bad(err){
                        console.log(err);
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
        resetForm(formName) {
            this.$refs[formName].resetFields();
        }
    },
    computed: {
        permId(){
            return this.ruleForm.id;
        },
        ruleFormData(){
            return Qs.stringify(this.ruleForm);
        }
    },
    watch: {
        permId: "unRequiredRules",
        ruleFormData: "canSubmit"
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
            let url = "/xman/perm?id=" + pid;

            // 当http方法是DELETE的时候，后台只能用request.GET获取参数
            // 所以需要将参数写在url后面
            axios.delete(url).then(res => {
                if (res.data.code === 1){
                    self.$message.success(res.data.error)
                    let url = "/xman/perm/list";
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
            self.$confirm('确认删除此权限吗？')
            .then(_ => {
                self._delete();
            }).catch(_ => {});
        },
        create(){
            let url = "/xman/perm";
            window.location.href = url;
        }
    }
});