var listMixin = {
    delimiters: ["[[", "]]"],
    data() {
        return {
            // 是否还有更多数据可以加载
            more: true,

            // 排序项
            sorters: {},
            // 过滤器
            filtors: {},

            conditions: {},
            
            // 数据
            items: [],
            columns: [],
            page: 1,
            totalPages: 0,
            pageSize: 20,
            totalNum: 0,
        }
    },
    methods: {

        makeElement(item){
            return "<div>需要按照自己的需求进行实现</div>"
        },

        loadItems(items){
            if (items && items.length > 0){
                for (let item of items){
                    let ele = this.makeElement(item);
                    $("#data-items").append(ele);
                }
            }
        },

        getItems(){
            let that = this;
            if (!(that.more)){
                that.$message.info("没有了!");
                return;
            }

            let sortBy = JSON.stringify(that.sorters);
            let filterBy = JSON.stringify(that.filtors);
            let params = {
                sortBy: sortBy,
                filterBy: filterBy,
                page: this.page,
                pageSize: this.pageSize,
            }
            let url = $("#data-api").text();
            console.log(url);
            axios.get(url, {
                "params": params
            }).then(function(res){
                if (res.data.code == 1){
                    that.items = res.data.data;
                    if (!(that.items) || that.items.length === 0){
                        that.$message.info("没有了!");
                        that.more = false;
                    }
                }else{
                    that.$message.error(res.data.error);   
                }
            }).catch(function(err){
                console.log(err);
                that.$message.error("网络错误，请点击重试按钮");
            });
        }
    }
}

