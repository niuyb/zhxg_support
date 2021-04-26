let app = new Vue({
    el: "#main",
    delimiters: ["[[", "]]"],
    data(){
        return {
            settings: [],
            _settings: [],
            ok: false
        }
    },
    created(){
        this.getSettings();
        // this.settings = [{'notice_type_id': 1, 'status': true, 'name': '客户保有量每日提醒', 'comment': '统计名下客户数量'}, 
        // {'notice_type_id': 2, 'status': true, 'name': '客户超限自动踢回公海池通知', 'comment': '超过限制自动踢回'}, 
        // {'notice_type_id': 3, 'status': false, 'name': '回款计划异常提醒', 'comment': '主要判断承诺回款日期填写是否异常'}, 
        // {'notice_type_id': 4, 'status': false, 'name': '账号开通提醒', 'comment': '快速开通秘书、指挥平台、网评、态势感知'}, 
        // {'notice_type_id': 5, 'status': 1, 'name': '秘书帐号重新关联商机每周一提醒', 'comment': '关联商机赢率达到100%，需要重新关联商机'}, 
        // {'notice_type_id': 6, 'status': 1, 'name': '任务提醒', 'comment': '商务的10种任务类型提醒'}, 
        // {'notice_type_id': 7, 'status': 1, 'name': '下载移动端和绑定微信公众号提醒', 'comment': '商务提醒客户下载移动端和绑定微信号'}, 
        // {'notice_type_id': 8, 'status': 1, 'name': '计划回款提醒', 'comment': '在计划回款日的前15天和30天提醒'}, 
        // {'notice_type_id': 9, 'status': 1, 'name': '订单到期提醒', 'comment': '订单到期前25天通知'}, 
        // {'notice_type_id': 10, 'status': 1, 'name': '停用账号活跃提醒', 'comment': '近30天内停用状态超过21天，但30天内活跃有6天'}];
        // this.ok = true;
    },

    methods: {
        getSettings(){
            let url = "/notice/setting/list/api";
            axios.get(url).then(res => {
                let settings = [];
                for (let setting of res.data.data){
                    setting.status = setting.status == 1 ? true : false;
                    settings.push(setting);
                };
                this.settings = settings;
                this.ok = true;
            }).catch(res => {
                console.log(res);
            })
        },

        changeSwitch(setting){
            let self = this;
            let url = "/notice/settings/change";
            let _setting = JSON.parse(JSON.stringify(setting));

            if (setting.status == 1){
                _setting.status = 1
            }else{
                _setting.status = 0
            }

            axios.get(url, {
                params: _setting
            }).then(res => {
                if (res.data.code !== 1){
                    self.$message.error(res.data.error);
                }
            }).catch(err => {
                self.$message.error(err);
            });
        },
    }
})