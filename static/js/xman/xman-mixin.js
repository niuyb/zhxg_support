var xmanMixin = {
    data(){
        return {

        }
    },
    methods: {
        getId(){
            let id = getUrlKey("id", window.location.href);
            return id;
        },
        getApi(apiBase){
            let id = this.getId();
            let api = apiBase + id;
            return api;
        }
        getPermInfoApi(){
            let apiBase = "/xman/perm/info/api?id=";
            return this.getApi(apiBase);
        }, 
        getUserInfoApi(){
            let apiBase = "/xman/user?id=";
            return this.getApi(apiBase);
        }, 
        getModuleInfoApi(){
            let apiBase = "/xman/module?id=";
            return this.getApi(apiBase);
        }, 
        getRoleInfoApi(){
            let apiBase = "/xman/role?id=";
            return this.getApi(apiBase);
        },        
        getPermInfo(){
            this.ruleFormBackUp = JSON.parse(JSON.stringify(this.ruleForm));
            if (this.mode){
                console.log("mode: change.");

                let self = this;
                let url = self.getPermInfoApi();

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
            if (this.mode){
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
            })
        }
    }

}