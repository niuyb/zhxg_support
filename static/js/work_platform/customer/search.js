var app = new Vue({
    el: "#main",
    mixins: [ sidebarMixin, customerListMixin ],
    data(){
        return {
            searcher: "",
            oldSearcher: "",
            finished: true,
            finishedText: ""
        }
    },
    methods: {
        onSearch(){
            let that = this;
            that.finished = true;
            that.page = 1;
            that.pageSize = 20;
            that.oldSearcher = that.searcher;
            // that.filters["accountname"] = that.oldSearcher;
            for (let column of that.columns){
                if (column.name === "accountname"){
                    column.filter = column.filter || {};
                    column.filter.result = that.searcher;
                    break;
                }
            }
            that.list = [];
            that.finished = false;
            that.onLoad();
            that.finishedText = "没有更多了"
        }
    }
});