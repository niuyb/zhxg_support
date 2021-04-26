
axios.defaults.headers.common['X-CSRFToken'] = $("input[name='csrfmiddlewaretoken']").val(); 

var app = new Vue({
    el: "#app",
    delimiters: ["[[", "]]"],
    data() {
        var numberValidator = (rule, value, callback) => {
            if (value === ''){
                callback
            }
        };
        return {
            mode: 0,

            // submit button
            canClick: false,

            checkedId: "",
            modules : [],
            moduleTree: {
                data: [],
                defaultExpandedKeys: [],
                defaultCheckedKeys: [],
                defaultProps: {
                    "label": "name",
                    "children": "children"
                }
            },
            permTree: {
                defaultData: [
                    {"name": "显示", "code": "show"},
                    {"name": "查看", "code": "view"},
                    {"name": "添加", "code": "add"},
                    {"name": "删除", "code": "delete"},
                    {"name": "修改", "code": "change"},
                    {"name": "导出", "code": "export"},
                ],
                defaultNodeKey: "code",
                data: [],
                nodeKey: "",
                defaultExpandedKeys: [],
                defaultCheckedKeys: ["show", "view"],
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
                icon: '',
                url: '',
                parent: 0,
                perms: []
            },
            rules: {
                name: [{
                    required: true,
                    message: '请输入模块名称',
                    trigger: 'blur'
                }],
                code: [{
                    required: true,
                    message: '请输入模块英文代码',
                    trigger: 'blur'
                }],
                status: [{
                    required: true,
                    message: '请输入1或0',
                    trigger: 'blur'
                }],
                rank: [{
                    required: true,
                    message: '排名不能为空',
                    trigger: 'blur'
                },{ 
                    type: 'number', 
                    message: '排名必须为数字值',
                    trigger: 'blur'
                }],
            },
            permForm: {
                name: '',
                code: '',
                // permName: '',
                // permCode: '',
            },
            permFormRules: {
                name: [{
                    required: true,
                    message: '请输入模块名称',
                    trigger: 'blur'
                }],
                code: [{
                    required: true,
                    message: '请输入模块英文代码',
                    trigger: 'blur'
                }],
            }
        };
    },

    // props: ["moduleTree", "permTree"],
    created(){
        this.getMode();
        this.getModuleInfo();
        this.getModuleTree();
    },
    methods: {
        getId(){
            let id = getUrlKey("id", window.location.href);
            return id;
        },
        getMode(){
            let id = this.getId();
            this.mode = id ? 1 : 0;
        },
        initPermTree(){
            if (!(this.ruleForm.id)){
                this.permTree.nodeKey = this.permTree.defaultNodeKey;
                //this.permTree.data = this.permTree.defaultData;
            }
        },
        getModuleInfo(){

            this.ruleFormBackUp = JSON.parse(JSON.stringify(this.ruleForm));

            // 这步的意思是，判断是创建还是修改
            let id = getUrlKey("id", window.location.href);
            let self = this;
            if (id){
                console.log("mode: change.");
                let url = "/xman/module/info/api?id=" + id;
                axios.get(url).then(function(res){
                    let mod = res.data.data;
                    for (let k in self.ruleForm){
                        self.ruleForm[k] = mod[k];
                    }

                    // self.ruleForm.rank = String(self.ruleForm.rank);
                    self.ruleFormBackUp = JSON.parse(JSON.stringify(self.ruleForm));

                    //
                    self.moduleTree.defaultCheckedKeys = [mod.parent];

                    // 当修改模块的权限时比较有用
                    self.permTree.data = JSON.parse(JSON.stringify(mod.permissions));

                    // 将mod.permissions分别复制给ruleForm和ruleFormBackUp
                    self.ruleForm.perms = JSON.parse(JSON.stringify(mod.permissions));
                    self.ruleFormBackUp.perms = JSON.parse(JSON.stringify(mod.permissions));

                    self.permTree.nodeKey = "id";
                }).catch(function(err){
                    self.$message.error(err);
                })
            // 如果是新建模块，那么permTree.data和permTreeNodeKey使用默认设置
            }else{
                self.initPermTree();
            }
        },
        _createPerm(form){
            let self = this;
            let qs = Qs.stringify(form);
            let url = "/xman/perm";
            axios.post(url, qs).then(res => {
                if (res.data.code === 1){
                    self.$message.success(res.data.error);

                    // 将创建好的权限添加到permTree.data里面
                    self.permTree.data.push(res.data.data);

                    // 修改模块时，快速添加权限时，需要将permTree.defaultData里面的这条权限移除掉
                    let index = self.permTree.defaultData.indexOf(form);
                    if (index !== -1){
                        self.permTree.defaultData.splice(index, 1);
                    }

                    // 创建权限成功之后，清空permForm
                    self.resetPermForm();
                }else{
                    self.$message.error(res.data.error);
                }
            }).catch(err => {
                self.$message.error(err);
            })
        },
        createPerm(){
            let self = this;
            let form = null;
            let name = self.permForm.name;
            if (!name){
                self.$message.error("权限名称不能为空");
                return false;
            }
            let code = self.permForm.code;
            if (!code){
                self.$message.error("权限代码不能为空");
                return false;
            }
            code = /^[a-zA-Z]+[a-zA-Z\d]+$/.exec(code)[0];
            if (!code){
                self.$message.error("权限代码必须是英文和数字的组合，并且需要以英文字母开头");
                return false;
            }
            form = {"name": name, "code": code}

            // 查重
            if (self.isPermDuplicate(form)){
                return;
            }
                
            if (this.mode === 1){
                let id = self.getId();
                form.module = id;
                self._createPerm(form);                
            }else{
                self._addPerm(form);
            }
        },
        resetPermForm(){            
            this.permForm.name = "";
            this.permForm.code = "";
        },
        isPermDuplicate(perm){
            let self = this;
            for (let item of self.permTree.data){
                if (perm.code === item.code){
                    self.$message.warning('代码为"' + perm.code + '"的权限已经存在，请换一个代码吧！');
                    return true;
                }
                if (perm.name === item.name){
                    self.$message.warning('名称为"' + perm.name + '"的权限已经存在，请换一个名称吧！');
                    return true;
                }
            }
            return false;
        },
        isPermDuplicateDefault(perm){
            let self = this;
            for (let item of self.permTree.defaultData){
                if (perm.code === item.code){
                    console.log("与permTree.defaultData中数据code字段有重复，所以抛弃。");
                    return true;
                }
                if (perm.name === item.name){                    
                    console.log("与permTree.defaultData中数据name字段有重复，所以抛弃。");;
                    return true;
                }
            }
            return false;
        },
        _addPerm(perm){
            let self = this;
            self.permTree.data.push(perm);

            let index = self.permTree.defaultData.indexOf(perm);
            if (index !== -1){
                self.permTree.defaultData.splice(index, 1);
            }            

            // 清空permForm
            self.resetPermForm();
        },
        addPerm(node, data){
            let self = this;
            // 查重
            if (self.isPermDuplicate(data)){
                return;
            }

            if (this.mode === 1){
                let id = this.getId();
                let params = {"module": id, "name": data.name, "code": data.code};
                self._createPerm(params);
            }else{
                self._addPerm(data);
            }
        },

        deletePerm(node, data){
            let self = this;
            if (this.mode === 1){
                let id = data.id;
                let url = "/xman/perm?id=" + id;
                axios.delete(url).then(res => {
                    if (res.data.code === 1){
                        self.$message.success(res.data.error);

                        // 查重
                        if (!(self.isPermDuplicateDefault(data))){
                            self.permTree.defaultData.push(data);
                        }                        

                        let index = self.permTree.data.indexOf(data);
                        if (index !== -1){
                            self.permTree.data.splice(index, 1);
                        }                        
                    }else{
                        self.$message.error(res.data.error);
                    }                    
                }).catch(err => {
                    self.$message.error(err);
                })
            }else{
                self.permTree.defaultData.push(data);

                let index = self.permTree.data.indexOf(data);
                if (index !== -1){
                    self.permTree.data.splice(index, 1);
                }
            }
        },
        changePermStatus(node, data){
            let self = this;
            let form = JSON.parse(JSON.stringify(data));
            let url = "/xman/perm";
            if (form.status){
                form.status = 0;
            }else{
                form.status = 1;
            }
            let qs = Qs.stringify(form);
            axios.put(url, qs).then(res => {
                if (res.data.code === 1){
                    self.$message.success(res.data.error);

                    data.status = !(data.status);
                }else{
                    self.$message.error(res.data.error);
                }
            }).catch(err => {
                self.$message.error(res.data.error);
            });
        },
        getModuleTree(){
            // // 这步的意思是，判断是创建还是修改
            // let id = getUrlKey("id", window.location.href);
            // if (id){
            //     // do nothing.
            // }else{
                let self = this;
                let url = "/xman/module/tree/all/api";
                axios.get(url).then(function(res){
                    self.moduleTree.data = res.data.data;

                    if (self.moduleTree.defaultCheckedKeys.length == 0){
                        let parent = getUrlKey("parent", window.location.href);
                        if (parent){
                            self.moduleTree.defaultCheckedKeys = [parent];
                        }                        
                    }                    
                }).catch(function(err){
                    self.$message.error(err);
                });
            // }
        },
        handleModuleNodeClick(item, checked, node) {
            if(checked === true) {
                this.checkedId = item.id;
                this.$refs.moduleTree.setCheckedKeys([item.id]);
            } else {
                if (this.checkedId == item.id) {
                    this.$refs.moduleTree.setCheckedKeys([]);
                    this.checkedId = "";
                }
            }
            this.ruleForm.parent = this.checkedId;
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
        setModuleDisabledKeys(){
            if (this.ruleForm.id && (this.moduleTree.data.length > 0)){
                function setDisabledKeys(tree, keys){
                    for (let item of tree){
                        if ((keys.indexOf(item.id) > -1) || (keys.indexOf(item.id + "") > -1)){
                            item.disabled = true;
                        }
                        let children = item.children;
                        if (children && (children.length > 0)){
                            setDisabledKeys(children, keys)
                        }
                    }
                }
                let keys = [this.ruleForm.id];
                setDisabledKeys(this.moduleTree.data, keys);
            }
        },
        getPermCheckedNodes() {
            return this.$refs.permTree.getCheckedNodes();
        },
        getPermCheckedKeys() {
            return this.$refs.permTree.getCheckedKeys();
        },
        setPermCheckedNodes() {
            this.$refs.permTree.setCheckedNodes([]);
        },
        setPermCheckedKeys() {
            this.$refs.permTree.setCheckedKeys([]);
        },
        setRuleFormPerms(){
            // 当修改模块时，添加、删除、修改权限状态等操作，都会与后台发生实际交互
            // 所以不需要关注ruleForm中的perms

            // 但是当新建模块时，添加权限只是在前端添加了而已，并没有与后端发生实际的交互
            // 所以需要监听，点击创建模块按钮，与后台交互时，才会在数据库里面创建新的权限
            if (this.mode === 0){
                this.ruleForm.perms = JSON.parse(JSON.stringify(this.permTree.data));
            }            
        },
        resetChecked() {
            this.$refs.moduleTree.setCheckedKeys([]);
            this.$refs.permTree.setCheckedKeys([]);
        },
        unRequiredModule(){
            this.rules.module = [];
        },
        canSubmit(){
            let parents = this.getModuleCheckedKeys();
            let ok = compareTwoObjects(this.ruleForm, this.ruleFormBackUp)
            this.canClick = !ok;
        },
        submitForm(formName) {
            let self = this;

            let form = JSON.parse(JSON.stringify(self.ruleForm));

            // permission_codes
            // let perms = [];
            // for (let p of self.getPermCheckedKeys()){
            //     for (perm of self.permTree.defaultData){
            //         if (perm.code == p){
            //             perms.push(perm)
            //         }
            //     }
            // };
            let perms = self.permTree.data;


            form.perms = JSON.stringify(perms);

            // parent
            let parents = [];
            for (let m of self.getModuleCheckedKeys()){
                parents.push(m);
            };
            if (parents.length > 0){
                form.parent = parents[0];
            };

            if (form.status){
                form.status = 1
            }else{
                form.status = 0
            }

            self.$refs[formName].validate((valid) => {
                if (valid) {
                    let url = "/xman/module";

                    let data = Qs.stringify(form);

                    let method = null;
                    if (self.mode === 1){
                        method = "put";
                    }else{
                        method = "post";
                    }

                    axios[method](url, data).then(res => {
                        if (res.data.code === 1){
                            self.$message.success(res.data.error);
                            let id = res.data.data.id;
                            let url = "/xman/module?id=" + id;
                            window.location.href = url;
                        }else{
                            self.$message.error(res.data.error);
                        }
                    }).catch(function(err){
                        self.$message.error(err);
                    });
                } else {
                    console.log('error submit!!');
                    return false;
                }
            });
        },
        resetForm(formName) {
            this.$refs[formName].resetFields();
            this.resetChecked();
            this.ruleForm.parent = 0;
            this.ruleForm.perms = "";
        }
    },
    computed: {
        parents(){
            let ps = this.getModuleCheckedKeys();
            return this.getModuleCheckedKeys();
        },
        ruleFormId(){
            return this.ruleForm.id;
        },
        moduleTreeDataLength(){
            return this.moduleTree.data.length;
        },
        ruleFormData(){
            return Qs.stringify(this.ruleForm);
        },
        permTreeData(){
            return this.permTree.data;
        }
    },
    watch: {
        ruleFormId: "setModuleDisabledKeys",
        moduleTreeDataLength: "setModuleDisabledKeys",
        ruleFormData: "canSubmit",
        permTreeData: "setRuleFormPerms"
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
            let url = "/xman/module?id=" + id;

            // 当http方法是DELETE的时候，后台只能用request.GET获取参数
            // 所以需要将参数写在url后面
            axios.delete(url).then(res => {
                if (res.data.code === 1){
                    self.$message.success(res.data.error)
                    let url = "/xman/module/tree";
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
            self.$confirm('确认删除此模块吗？')
            .then(_ => {
                self._delete();
            }).catch(_ => {});
        },
        create(){
            let url = "/xman/module";
            window.location.href = url;
        }
    }
});