var app = new Vue({
    el: "#main",
    mixins: [ sidebarMixin, customerListMixin ],
    data(){
        return {
            show_back_btn: false,
            show_add_btn: false,
        }
    },
    methods: {
        toSearch(){
            window.location.href = "/work_platform/customer/search"
        },
        // toFilt(){
        //     console.log("toFilt")
        // }
    },
    created(){
        this.parseUrl();
    }
}); 