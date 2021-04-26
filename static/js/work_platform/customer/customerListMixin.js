
function dateTimeToString(dateTime){ 
    var year = dateTime.getFullYear(); 
    var month =(dateTime.getMonth() + 1).toString(); 
    var day = (dateTime.getDate()).toString();  
    var hour = (dateTime.getHours()).toString();
    var minute = (dateTime.getMinutes()).toString();
    var second = (dateTime.getSeconds()).toString();

    if (month.length == 1) { 
        month = "0" + month; 
    } 
    if (day.length == 1) { 
        day = "0" + day; 
    }
    if (hour.length == 1){
        hour = "0" + hour;
    }
    if (minute.length == 1){
        minute = "0" + minute;
    }
    if (second.length == 1){
        second = "0" + second;
    }
    var str = year + "-" + month + "-" + day + " " + hour + ":" + minute + ":" + second;
    return str; 
  }
  

var customerListMixin = {
    mixins: [ listMixin ],
    filters: {
        timestampToDatetimeString(timestamp){
            function add0(m){return m<10?'0'+m:m }
            function format(shijianchuo)
            {
            //shijianchuo是整数，否则要parseInt转换
            var time = new Date(shijianchuo);
            var y = time.getFullYear();
            var m = time.getMonth()+1;
            var d = time.getDate();
            var h = time.getHours();
            var mm = time.getMinutes();
            var s = time.getSeconds();
            return y+'-'+add0(m)+'-'+add0(d)+' '+add0(h)+':'+add0(mm)+':'+add0(s);
            }
            return format(timestamp);
        },
        levelFormatter(level){
            if (level == 1){
                return "重点客户"
            }else if(level == 4){
                return "开发客户"
            }else if(level == 5){
                return "正式客户"
            }else{
                return "未填写"
            }
        }
    },
    data() {
        return {
            // parseUrl之后，再将finished设置成true
            // 这样才会携带参数向后台请求客户列表数据
            finished: false,


            showWechatButtonGroup: false,
            showBindingForm: false,
            defaultTimeCounter: 30,
            timeCounter: 30,

            // 当前操作对象
            currentItem: {},
            wechatBindingForm: {
                "type": 1,
                customer_id: "",
                customer_name: "",
                wechat_group_name: "",
                robot_name: "",
                qr_code: []
            },

            wechatGroupMembers: {
                show: false,
                loading: false,
                finished: false,
                items: [],
            },

            wechatGroupMessageList: {
                showCheckBox: false,
                show: false,
                refreshing: false,
                loading: false,
                finished: true,
                finishedText: "没有更多了",
                customer: null,
                items: [],
                result: [],

                pageSize: 20
            },

            power: {
                options: [
                    {text: "全部客户", value: "0"},
                    {text: "我的客户", value: "1"}
                ],
                result: "0"
            },

            columns: [
                {
                    label: "客户名称",
                    name: "accountname",
                    disabled: false,
                    type: "string",
                    sortBy: null,
                    filter: {
                        options: null,
                        result: []
                    }
                },
                {
                    label: "创建日期",
                    name: "createdat",
                    disabled: false,
                    type: "string",
                    sortBy: "desc",
                    filter: null
                },
                {
                    label: "最新活动",
                    name: "recentactivityrecordtime",
                    disabled: false,
                    type: "string",
                    sortBy: "",
                    filter: null
                },
                {
                    label: "最新消息",
                    name: "message_ctime",
                    disabled: false,
                    type: "string",
                    sortBy: "",
                    filter: null
                },
                {
                    label: "客户级别",
                    name: "level",
                    disabled: false,
                    type: "string",
                    sortBy: null,
                    filter: {
                        type: "multiple",
                        options: [
                            {
                                label: "重点客户",
                                value: 1
                            },
                            {
                                label: "开发客户",
                                value: 4
                            },
                            {
                                label: "正式客户",
                                value: 5
                            },
                            {
                                label: "空",
                                value: null
                            }
                        ],
                        result: []
                    }
                },
                {
                    label: "微信群",
                    name: "wechat_group",
                    disabled: false,
                    type: "string",
                    sortBy: null,
                    filter: {
                        type: "multiple",
                        options: [
                            {
                                label: "未绑定",
                                value: 0
                            },
                            {
                                label: "申请中",
                                value: 1
                            },
                            {
                                label: "审核中",
                                value: 2
                            },
                            {
                                label: "已绑定",
                                value: 3
                            },
                            {
                                label: "绑定失败",
                                value: 4
                            },
                            // {
                            //     label: "空",
                            //     value: null,
                            //     // name: "",
                            //     // checked: false
                            // }
                        ],
                        result: []
                    }
                },
                {
                    label: "消息状态",
                    name: "is_read",
                    disabled: true,
                    type: "number",
                    sortBy: null,
                    filter: {
                        options: [
                            {
                                label: "有新消息",
                                value: 0
                            },
                            {
                                label: "无新消息",
                                value: 1
                            },
                        ],
                        result: []
                    }
                }
                // {
                //     label: "最新群消息",
                //     name: "wechat_group_message_ctime",
                //     type: "time",
                //     sortBy: "",
                //     filter: {
                //         options: [
                //             {
                //                 label: "有",
                //                 value: 1
                //             },
                //             {
                //                 label: "无",
                //                 value: 0
                //             }
                //         ],
                //         result: []
                //     }
                // },
            ]
        }        
    },
    methods: {
        countTime(){
            let that = this;
            let tip = "正在进行绑定，请稍后：" + that.timeCounter + "...";
            $("#form-tip").text(tip);
            if ((that.timeCounter - 2) % 3 === 2){
                that.getBindingResult(that.taskId);
            }
            that.timeCounter --;
            
            if (that.timeCounter < 0){
                $("#waiting").hide();
                $("#form-tip").text("网络超时。");
                clearInterval(inter);
            }
        },
        onSubmit(values) {
            let that = this;
            that.timeCounter = that.defaultTimeCounter;

            if (!(that.wechatBindingForm.qr_code) || that.wechatBindingForm.qr_code.length === 0){
                let tip = "请上传微信群二维码。";
                $("#form-tip").text(tip);
                return;
            }

            that.taskId = "";

            let url = "/work_platform/wechat";

            var formData = new FormData();
            
            for (let k in that.wechatBindingForm){
                let v = that.wechatBindingForm[k];

                if (k === "qr_code"){
                    formData.append(k, v[0].file);
                }else{
                    formData.append(k, v)
                }                
            }
            
            let config = {
                headers: {
                    'Content-Type': 'multipart/form-data'
                }
            }        
            
            var second = 10;
            that.$toast.loading(`请稍候 ${second} 秒`);

            const timer = setInterval(() => {
                second--;
                if (second){
                    that.$toast.loading(`请稍候 ${second} 秒`);
                } else {
                    clearInterval(timer);
                }
            }, 1000);

            axios.post(url, formData, config).then(res => {

                clearInterval(timer);

                if (res.data.code === 1){
                    that.taskId = res.data.data.taskId;
                    that.$toast.success("等待微信官方审核...");
                    that.showBindingForm = false;
                    that.currentItem.wechat_group_id = res.data.data.wxRoomId;
                    that.currentItem.status = 3;
                    that.currentItem.ctime = dateTimeToString(new Date());
                }else{
                    let tip = "微信群绑定失败，原因：" + res.data.error;
                    that.currentItem.status = 2;
                    that.$toast.fail(tip);
                }
            }).catch(err => {
                clearInterval(timer);
                
                let tip = "微信群绑定失败, 原因：" + err;
                that.$toast.fail(tip);
                // that.$toast.fail(err);
            })
        },
        
        unbindWechatGroup(item){
            let customerId = item.id;
            let that = this;
            let url = "/work_platform/wechat?customer_id=" + customerId;
            axios.patch(url).then(res => {
                if (res.data.code == 1){
                    that.$toast.success(res.data.error);
                    // messager.success(res.data.error);
                    that.currentItem.wechat_group_id = null;
                    // 0代表微信群解绑了
                    that.currentItem.status = 0;
                }else{
                    // messager.error(res.data.error);
                    that.$toast.fail(res.data.error);
                }
                
            }).catch(err => {
                // messager.error(err);
                let tip = "解绑失败，原因：" + err;
                that.$toast.fail(tip);
            })
        },

        bindWechatGroup(item){
            let customerId = item.id;
            let that = this;
            that.currentItem = item;

            if (!customerId){
                return;
            }

            that.showBindingForm = true;
            if (customerId !== that.wechatBindingForm.customer_id){

                that.wechatBindingForm.customer_id = that.currentItem.id;
                that.wechatBindingForm.customer_name = that.currentItem.accountname;
                that.wechatBindingForm.wechat_group_name = that.currentItem.accountname + "-微信群";
                that.wechatBindingForm.robot_name = "客服";
                that.wechatBindingForm.qr_code = [];
            }

        },

        getBindingResult(){
            let that = this;

            if (!that.taskId){
                return;
            }

            let url = "/work_platform/wechat/result?task_id=" + that.taskId;
            axios.get(url).then(res => {
                if (res.data.code == 1){
                    $("#waiting").hide();
                    that.currentItem.wechat_group_id = res.data.data.wxRoomId;
                    that.showBindingForm = false;
                    messager.success("微信群绑定成功！")
                    clearInterval(inter);
                }
            }).catch(err => {
                $("#waiting").hide();
                clearInterval(inter);
                $("#form-tip").text("微信群绑定失败，原因：" + err);
            })
        },

        beforeClose({ position, instance }) {
            let that = this;
            that.currentRow = instance;

            switch (position) {
                case 'left':
                    break;
                case 'cell':
                case 'outside':
                    instance.close();
                    break;
                case 'right':
                    let item = instance.name;
                    if (item.status === 1 && new Date() - (new Date(item.ctime)) > 24 * 60 * 60 * 1000){
                        let message = "确定要解除绑定吗？"
                        that.$dialog({
                            message: message,
                            showCancelButton: true,
                            className: "dialog"
                        }).then(() => {
                            that.unbindWechatGroup(item);
                        }).catch(err => {});
                    }else{
                        that.bindWechatGroup(item);
                    }
                    break;
            }
        },
        confirmUnbindWechatGroup(item){
            let that = this;
            that.currentItem = item;
            if (item.status === 1 && new Date() - (new Date(item.ctime)) > 24 * 60 * 60 * 1000){
                let message = "确定要解除绑定吗？"
                that.$dialog({
                    message: message,
                    showCancelButton: true,
                    className: "dialog"
                }).then(() => {
                    that.unbindWechatGroup(item);
                }).catch(err => {});
            }else{
                that.bindWechatGroup(item);
            }
        },

        dropQrCode(){
            let qr_codes = this.wechatBindingForm.qr_code;
            if (qr_codes && qr_codes.length > 1){
                this.wechatBindingForm.qr_code = [qr_codes.pop()];
            }
        },

        showWechatGroupMembers(item){
            let that = this;
            that.wechatGroupMembers.items = [];
            that.wechatGroupMembers.show = true;
            that.wechatGroupMembers.finished = false;
            that.wechatGroupMembers.loading = true;

            let wechatGroupId = item.wechat_group_id || "";
            if (wechatGroupId || wechatGroupId != 0){
                let url = "/work_platform/wechat/group/members/api?wechatGroupId=" + wechatGroupId;
                axios.get(url).then(res => {
                    if (res.data.code === 1){
                        that.wechatGroupMembers.items = res.data.data;
                    }else{
                        that.$toast.fail(res.data.error);
                    }

                    that.wechatGroupMembers.finished = true;
                    that.wechatGroupMembers.loading = false;
                }).catch(err => {
                    that.$toast.fail("网络错误，请稍后重试");

                    that.wechatGroupMembers.finished = true;
                    that.wechatGroupMembers.loading = false;
                })
            }
        },

        showWechatGroupMessageList(item){
            let that = this;
            that.wechatGroupMessageList.show = true;
            if (that.wechatGroupMessageList.customer && item.customer_id === that.wechatGroupMessageList.customer.customer_id){
                that.wechatGroupMessageList.finished = false;
                return;
            }

            that.wechatGroupMessageList.customer = item;
            // that.loadWechatGroupMessageList();
            that.wechatGroupMessageList.items = [];
            that.wechatGroupMessageList.finished = false;
            // that.getWechatGroupMessageList();
        },
        loadWechatGroupMessageList(Type){
            let that = this;
            Type = Type || 2;
            if (that.wechatGroupMessageList.items && that.wechatGroupMessageList.items.length === 0){
                Type = 0;
            }
            
            // this.wechatGroupMessageList.items = [];
            this.getWechatGroupMessageList(Type);
        },
        getWechatGroupMessageList(Type){

            let that = this;
            let _type = Type || 0;
            let items = this.wechatGroupMessageList.items;
            let minId = items.length > 0 ? items[0].id : null;
            let maxId = items.length > 0 ? items[items.length - 1].id : null;
            let customerId = this.wechatGroupMessageList.customer.customer_id;

            let curId = "";
            
            if (_type === 0 || _type === 1){
                curId = minId;
            }else if(_type === 2 || _type === 3){
                curId = maxId;
            }

            let url = "/work_platform/wechat/group/message/list/api";
            let params = {
                //type: 0, 默认查询历史消息 1、查询历史消息的数量 
                //      2、查询新的群信息 3、查询新的群消息的数量 
                //      4、查询已读消息 5、查询已读的消息数量
                //      6、查询未读消息 7、查询未读的消息数量
                'type': _type,
                'curId': curId,
                'customerId': customerId,
                'pageSize': that.wechatGroupMessageList.pageSize
            }
            
            axios.get(url, {
                "params": params
            }).then(res => {
                if (res.data.code === 1){
                    
                    if (!(res.data.data) || res.data.data.length === 0){
                        // do nothing.
                    }else{

                        for (let item of res.data.data){
                            if (_type === 0){
                                that.wechatGroupMessageList.items.unshift(item);
                            }else if(_type === 2){
                                that.wechatGroupMessageList.items.push(item);
                            }
                        }

                    }
                }else{

                    that.$toast.fail(res.data.error);

                }

                if(_type === 0){
                    that.wechatGroupMessageList.refreshing = false;

                }
                
                that.wechatGroupMessageList.finished = true;
                that.wechatGroupMessageList.loading = false;

            }).catch(err => {
                that.$toast.fail(err);

                if(_type === 0){
                    that.wechatGroupMessageList.refreshing = false;
                }

                that.wechatGroupMessageList.finished = true;
                that.wechatGroupMessageList.loading = false;
            })
        },
        hasNewWechatMessage(){
            let that = this;
            let items = this.wechatGroupMessageList.items;
            let maxId = items.length > 0 ? items[items.length - 1].id : null;
            let customerId = this.wechatGroupMessageList.customer.customer_id;
            let url = "/work_platform/wechat/group/message/list/api";
            let params = {
                // 查询新群消息的数量
                'type': 2,
                maxId: maxId,
                customerId: customerId,
                pageSize: this.wechatGroupMessageList.pageSize
            }
            axios.get(url, {
                    "params": params
                }).then(res => {
                if (res.data.code === 1){
                    ///////////////////////////
                }else{
                    that.$toast.fail(res.data.error);
                }
            }).catch(err => {
                that.$toast.fail(err);
            })
        },
        parseUrl(){
            console.log("parseUrl");
            let that = this;
            let url = window.location.href;
            let power = getUrlKey("power", url);
            let sortBy = getUrlKey("sortBy", url);
            let filterBy = getUrlKey("filterBy", url);
            let page = getUrlKey("page", url);
            let pageSize = getUrlKey("pageSize", url);

            if (!power){
                power = "0";
            }
            that.power.result = power;

            if (!page){
                page = 0;
            }

            try{
                page = parseInt(page)
            }catch(e){
                page = 0
            }
            if (page <=0 ){
                page = 1
            }
            that.page = page;

            if (!pageSize){
                pageSize = 0;
            }
            try{
                pageSize = parseInt(pageSize)
            }catch(e){
                pageSize = 0
            }
            if (pageSize <= 0){
                pageSize = 20
            }
            that.pageSize = pageSize;

            try{
                sorters = JSON.parse(sortBy)
            }catch(e){
                sorters = null;
            }

            if (sorters){
                for (let name in sorters){
                    for (let column of that.columns){
                        if (name === column.name){
                            let sortBy = sorters[name];
                            column.sortBy = sortBy;
                            break;
                        }
                    }
                }
            }

            try{
                filters = JSON.parse(filterBy)
            }catch(e){
                filters = {}
            }

            if (filters){
                for (let name in filters){
                    for (let column of that.columns){
                        if (name === column.name){
                            column.filter = column.filter || {};
                            let filterBy = filters[name];
                            column.filter.result = filterBy;
                            break;
                        }
                    }
                }
            }

            that.finished = false;
        },

        changeIsReadStatus(){
            let that = this;
            let isReadColumn = null;
            for (let column of that.columns){
                if (column.name === "is_read"){
                    isReadColumn = column;
                    break;
                }
            }

            if (!isReadColumn){
                console.log("isReadColumn is null.")
                return;
            }

            if (that.wechatGroupResult.indexOf(2) !== -1 || that.wechatGroupResult.indexOf(3) !== -1){
                isReadColumn.disabled = false;
            }else{
                isReadColumn.filter.result = [];
                isReadColumn.disabled = true;
            }
        }
    },
    computed: {
        qr_code(){
            return this.wechatBindingForm.qr_code;
        },
        wechatGroupResult(){
            let that = this;
            for (let column of that.columns){
                if (column.name === "wechat_group"){
                    return column.filter.result;
                }
            }
        },
        powerResult(){
            return this.power.result;
        }
    },
    watch: {
        "qr_code": "dropQrCode",
        "wechatGroupResult": "changeIsReadStatus",
        "powerResult": "refresh",
    }
}
