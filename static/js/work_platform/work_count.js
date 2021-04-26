
var app = new Vue({
    el: "#main",
    mixins: [ sidebarMixin, listMixin ],
    data(){
        return{
            show_sort_btn:true,
            show_filter_btn:false,
            show_search_btn:false,
            show_add_btn:false,
            show_back_btn:true,

            showSorted:false,
            show_detail:false,

            radio_result:"",
            date_result:"",
            date: '',
            timeShow: false,

            minDate: new Date(2020, 8, 23),
            maxDate: new Date(2025, 0, 31),

            columns: [
                {
                    label: "销售名称",
                    name: "saler_name",
                    disabled: false,
                    type: "string",
                    sortBy: null,
                    filter: {
                        options: null,
                        result: []
                    }
                },
            ],

            sorted_columns: [
                {
                    label: "新建客户数目",
                    name: "account_num",
                    disabled: false,
                    type: "string",
                    sortBy: null,
                    filter: {
                        options: null,
                        result: []
                    }
                },
                                {
                    label: "新建商机数目",
                    name: "opp_num",
                    disabled: false,
                    type: "string",
                    sortBy: null,
                    filter: {
                        options: null,
                        result: []
                    }
                },
                                {
                    label: "新建订单数目",
                    name: "order_num",
                    disabled: false,
                    type: "string",
                    sortBy: null,
                    filter: {
                        options: null,
                        result: []
                    }
                },
                                {
                    label: "订单归档数目",
                    name: "order_back_num",
                    disabled: false,
                    type: "string",
                    sortBy: null,
                    filter: {
                        options: null,
                        result: []
                    }
                },
                                {
                    label: "新建秘书账号数目",
                    name: "ms_num",
                    disabled: false,
                    type: "string",
                    sortBy: null,
                    filter: {
                        options: null,
                        result: []
                    }
                },
                                                {
                    label: "当月业绩",
                    name: "kpi_num",
                    disabled: false,
                    type: "string",
                    sortBy: null,
                    filter: {
                        options: null,
                        result: []
                    }
                },
                                                {
                    label: "今日绑定微信群数目",
                    name: "wechat_group",
                    disabled: false,
                    type: "string",
                    sortBy: null,
                    filter: {
                        options: null,
                        result: []
                    }
                },
                {
                    label: "微信群消息推送数目",
                    name: "wechat_message_num",
                    disabled: false,
                    type: "string",
                    sortBy: null,
                    filter: {
                        options: null,
                        result: []
                    }
                },
                {
                    label: "签到拜访数目",
                    name: "visit_num",
                    disabled: false,
                    type: "string",
                    sortBy: null,
                    filter: {
                        options: null,
                        result: []
                    }
                },
                {
                    label: "电话拜访数目",
                    name: "phone_num",
                    disabled: false,
                    type: "string",
                    sortBy: null,
                    filter: {
                        options: null,
                        result: []
                    }
                },

            ],

            detail_data_list:[],
            detail_data_type:"",

            detail_type:"",
            detail_id:"",
            detail_finished:false,
            detail_title_dict:{
                "account_num":"新建客户",
                "opp_num":"新建商机",
                "approve_num":"新建报价单",
                "order_num":"新建订单",
                "order_back_num":"订单归档",
                "wechat_group":"绑定微信群",
                "wechat_message_num":"推送微信群",
                "kpi_num":"员工业绩",
                "visit_num":"签到拜访",
                "phone_num":"电话拜访",
                "ms_num":"新建秘书账号",
                "act_account_num":"活跃客户"
            },

        }
    },
    methods: {
        onLoad() {
            let that = this;
            if (that.finished){
                return;
            }

            let sorters = {};
            let filters = {};

            for (let column of that.columns){
                let name = column.name;
                let sortBy = column.sortBy || null;
                if (sortBy){
                    sorters[name] = sortBy;
                }

                if (column.filter){
                    if (column.disabled){
                        // do nothing;
                    }else{
                        let filterBy = column.filter.result || null;
                        if (filterBy){
                            filters[name] = filterBy;
                        }
                    }
                }
            }

            let sortBy = JSON.stringify(sorters);
            let filterBy = JSON.stringify(filters);

            // let sortBy = JSON.stringify(that.sorters);
            // let filterBy = JSON.stringify(that.filters);
            let params = {
                sortBy: sortBy,
                filterBy: filterBy,
                page: this.page,
                pageSize: this.pageSize,
            }

            let url = $("#data-api").text();
            if (!url){
                that.loading = false;
                return;
            }

            that.loading = true;

            axios.get(url, {
                "params": params
            }).then(function(res){
                let items = [];
                if (res.data.code == 1){
                    items = res.data.data || [];
                    for (let item of items){
                        that.list.push(item);
                    }
                }else{
                    // messager.error(res.data.error);
                    that.$toast.fail(res.data.error);
                }

                that.loading = false;

                if (items.length < that.pageSize){
                    that.finished = true;
                }else{
                    that.page += 1;
                }

            }).catch(function(err){
                // console.log(err);
                that.finished = true;
                that.loading = false;
                // messager.error("网络错误，请稍候重试。");
                that.$toast.fail("网络错误，请稍候重试。");
                // setTimeout(function(){
                //     that.finishedText = "没有更多了"
                //     that.finished = false;
                // }, 30000)
            });
            that.add_histroy(url);
        },

        change_infos(url,that){
            var change_infos_list=[]
            axios.get(url).then(res=>{
                if (res.data.code == 1){
                    items = res.data.data || [];
                    for (let item of items){
                        change_infos_list.push(item);
                    }
                    that.list = change_infos_list
                }else{
                    that.finished = true;
                    that.loading = false;
                    // that.$toast.fail("网络错误，请稍候重试。");
                }
            });
        },

        toSearch(){},

        into_detail(event){
            var f_div = event.currentTarget.childNodes
            var depart_id = f_div[1].innerHTML;
            var level = f_div[3].innerHTML;

            if(level == "0" || level == "1"){
                url="/work_platform/count/departapi?depart="+depart_id+"&flag=1"
            }else if(depart_id != ""){
                url="/work_platform/count/departapi?depart="+depart_id
            }else{
             this.remove_history()
            }
            this.change_infos(url,this)
            this.add_histroy(url);
        },

        // toSearch(){
        //     window.location.href = "/work_platform/customer/search"
        // },
        // toFilt(){
        //     console.log("toFilt")
        // }
        onFilt(values){
            saler_name = values.saler_name
            // console.log(this.date_result)
            date = this.date_result
            // console.log(saler_name,date)
            // date = document.getElementById("time_selecter").lastChild.lastChild.textContent
            var url="/work_platform/count/perapi?"
            if(saler_name!=""){
                url = url + "id="+saler_name
            }
            if(date!="" && saler_name!=""){
                url= url + "&date="+date
            }else if(date!="" && saler_name ==""){
                url= "/work_platform/count/perapi?date="+date
            }else if(date=="" && saler_name !=""){
                url= "/work_platform/count/perapi?id="+saler_name
            }else if(date=="" && saler_name ==""){
                return
            }else{
                url= "/work_platform/count/departapi"
            }
            // console.log("url",url)
            this.change_infos(url,this)
            this.showFilters=false
        },
        toback(){
            res_list = this.remove_history()
            url=res_list[0]
            tag_borther_url = res_list[1]
            and_index = url.indexOf("&")
            g_index = url.indexOf("?")
            if (typeof(tag_borther_url) != undefined && tag_borther_url!=""){
                back_url = tag_borther_url
            }else{
                if(and_index >0){
                    back_url = url.substr(0,g_index)
                }else if(g_index > 0){
                    back_url = url.substr(0,g_index)
                }else{
                    back_url = url
                }
            }
            this.change_infos(back_url,this)
        },
        add_histroy(url){
            var tag_a = document.createElement("a");
            tag_a.style="display:none"
            tag_a.innerHTML = url
            var tag_back = document.getElementById("back")
            tag_back.appendChild(tag_a)
        },
        remove_history(){
            var tag_back = document.getElementById("back")
            var tag_a = tag_back.lastChild
            var back_url= tag_a.textContent
            if(back_url == ""){}else{
            tag_back.removeChild(tag_a)
            }
            var tag_borther = tag_back.lastChild.textContent
            return [back_url,tag_borther]
        },

        confirmDate(date){
            this.timeShow=false;
            this.date = date.getFullYear()+"-"+`${date.getMonth() + 1}`+"-"+date.getDate();
        },
        showTime(){
            this.timeShow=true;
        },

        to_sorted(){
            this.showSorted = true;
        },
        resetSorted(){
            this.radio_result=""
        },

        on_sorted(){
            var tag_back = document.getElementById("back")
            var tag_a = tag_back.lastChild
            var back_url= tag_a.textContent
            g_index = back_url.indexOf("?")
            if(this.radio_result != ""){
                if(g_index >= 0){
                    back_url = back_url+"&order="+this.radio_result
                    this.change_infos(back_url,this)
                }else{
                    back_url = back_url+"?order="+this.radio_result
                    this.change_infos(back_url,this)
                }
            }
            this.showSorted = false;
        },

        resetFilt(){
            for (let column of this.columns){
                if (column.filter){
                    column.filter.result = [];
                }
            }
            this.date = ""
            // document.getElementsByClassName("van-cell__value")[-1].lastChild.textContent=""
        },
        // 点击查看数目详情
        detail_infos(){
            let that = this;
            that.detail_data_list=[]
            istar_id = that.detail_id
            type = that.detail_type
            detail_url = "count/detailapi?type="+type+"&id="+istar_id
            axios.get(detail_url).then(function(res){
                if (res.data.code == 1){
                    that.detail_data_list = res.data.data
                    detail_data_type = res.data.type
                    that.detail_data_type = that.detail_title_dict[detail_data_type]

                    // console.log("data",detail_type)
                    // console.log(that.detail_data_list)
                    that.detail_finished = true
                }else{
                    that.detail_finished = true
                    // that.$toast.fail(res.data.error);
                }
            }).catch(function(err){
                console.log(err)
                that.detail_finished = true
                // that.$toast.fail("网络错误，请稍候重试。");
            });
        },
        to_detail(istar_id,type) {
            let that = this;
            if (istar_id) {
                that.detail_type = type
                that.detail_id = istar_id
                that.show_detail = true
            } else {
                that.detail_type = type
                that.detail_id = ""
            }
            that.detail_finished = false
        },
        close_detail(){
            let that=this
            that.detail_finished = false
            that.show_detail = false
        },

    },
    // watch: {
    //     detail_data_list: "setSignal",
    //     signal: "getTableData"
    // }
});