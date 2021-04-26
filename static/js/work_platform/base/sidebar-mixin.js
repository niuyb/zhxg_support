var sidebarMixin = {
    delimiters: ["[[", "]]"],
    data(){
        return {
            loading: true,
            sidebarItems: [],
            showSidebar: false
        }
    },
    methods: {
        toSidebar(){
            this.showSidebar = true;
        },
        getSidebarItems(){
            let that = this;
            let sidebarItems = [];
            let _modules = sessionStorage.getItem("sidebarItems");
            if (_modules){
                try{
                    sidebarItems = JSON.parse(_modules);
                }catch(e){
                    console.log(e);
                }
            }

            if (sidebarItems && sidebarItems.length > 0){
                that.sidebarItems = sidebarItems;
                return
            }

            let url = "/work_platform/modules";
            axios.get(url).then(res => {
                if (res.data.code === 1){

                    that.sidebarItems = res.data.data;

                    // 将侧边导航信息缓存到sessionStorage里面
                    sessionStorage.setItem("sidebarItems", JSON.stringify(res.data.data));

                }else{
                    let tip = "获取侧边导航失败，原因：" + res.data.error;
                    that.$toast.fail(tip);
                }
            }).catch(err => {
                let tip = "获取侧边导航失败，原因：" + err;
                that.$toast.fail(tip);
            })
        }
    },
    created(){
        this.getSidebarItems();
    }
}