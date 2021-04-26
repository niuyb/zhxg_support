var listMixin = {
    delimiters: ["[[", "]]"],
    // components: [ SwipeCell ],
    data() {
        return {
            // // 用来for循环计数
            // forLoopCount: 0,

            power: {},
            list: [],
            loading: false,
            finished: false,
            finishedText: "没有更多了",

            show_sort_btn:true,
            show_filter_btn:true,
            show_search_btn:true,
            show_add_btn:true,
            show_back_btn:true,

            showFilters: false,
            showAllFilters: false,
            showSorters: false,
            showAllSorters: false,

            showSearchers: false,

            // // 排序项
            // sorters: {
            //     createdat: "-"
            // },
            
            // filters: {},

            conditions: {},
            
            // 数据
            // items: [],
            columns: [
                // {
                //     label: "",
                //     name: "",
                //     type: "",
                //     sortBy: null,
                //     filter: {
                //         options: [
                //             {
                //                 label: "空",
                //                 value: null,
                //                 // name: "",
                //                 // checked: false
                //             }
                //         ],
                //         result: []
                //     }
                // },
            ],
            page: 1,
            totalPages: 0,
            pageSize: 20,
            totalNum: 0,
        }
    },
    methods: {
        onLoad() {
            console.log("onLoad");
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
                power: that.power.result,
                sortBy: sortBy,
                filterBy: filterBy,
                page: that.page,
                pageSize: that.pageSize,
            }

            let url = that.url;
            if (!url){
                url = $("#data-api").text();
            }
            // console.log(url);

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
        },
        // 显示目前已经选用的filters
        toFilt(){
            this.showFilters = true;
        },
        toSort(){
            // this.$toast.fail('排序，开发中！');
            let that = this;
            that.showSorters = true;
        },
        toAdd(){
            this.$toast.fail('添加，开发中！');
        },
        toback(){},
        toSearch(){},
        onFilt(values){
            // console.log(values);
            let that = this;
            // for (let k in values){
            //     that.filters[k] = values[k];
            // }
            that.showFilters = false;
            that.refresh();
        },
        resetFilt(){
            for (let column of this.columns){
                if (column.filter){
                    column.filter.result = [];
                }
            }
        },
        onSort(column){
            let that = this;
            let name = column.name;
            for (let col of that.columns){
                if (col.name === name){
                    if (col.sortBy !== "desc"){
                        col.sortBy = 'desc';
                    }else{
                        col.sortBy = "asc";
                    }
                }else{
                    if (col.sortBy){
                        col.sortBy = "";
                    }
                }
            }
            that.showSorters = false;
            that.refresh();
        },
        onSearch(){},

        refresh(){
            this.list = [];
            this.page = 1;
            this.finished = false;
            this.onLoad();
        }
    }
}

