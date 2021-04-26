var app = new Vue({
    el: '#saler-kpi-month',
    delimiters: ["[[", "]]"],
    data() {
        return {
            date: null,

            tableData: []
        }
    },
    methods: {
        getDate(){
            let date = getUrlKey("date", window.location.href);
            if (!date){
                let now = new Date();
                let month = (now.getMonth() + 1).toString();
                if (month.length === 1){
                    month = "0" + month
                }
                date = now.getFullYear() + "-" + month
            }
            this.date = date;
        },
        getTableData(){
            let self = this;
            let api = "/sale/saler/kpi/overview/api?date=" + self.date;
            axios.get(api).then(res => {
                if (res.data.code == 1){
                    self.tableData = res.data.data;
                }else{
                    self.$message.error(res.data.error)
                }
            }).catch(err => {
                self.$message.error(err)
            });
        },
        makeLink(row, key, start, end){
            if (start === 0){
                start = "0"
            }
            if (end === 0){
                end = "0"
            }
            if (!start){
                start = ""
            }
            if (!end){
                end = ""
            }

            let link = "/sale/saler/kpi/month";
            let params = ["date=" + this.date];
            let join_days = {
                columnName: "join_days",
                start: "181",
                end: "",
                searchType: "numberRange"
            }

            if (row.join_days === "三个月以内"){
                join_days.start = "0";
                join_days.end = "90"
            }else if(row.join_days === "三到六个月"){
                join_days.start = "91";
                join_days.end = "180"
            }

            params.push("join_days=" + encodeURI(JSON.stringify(join_days)));
            let other = {
                columnName: key,
                start: start,
                end: end,
                searchType: "numberRange"
            }
            
            params.push(key + "=" + encodeURI(JSON.stringify(other)));
            let query = params.join("&")
            return link + "?" + query
        },
        makeLink0(row, key){
            return this.makeLink(row, key, 0, 0)
        }
    },
    created(){
        this.getDate();
        // this.getTableData
    },
    watch: {
        "date": "getTableData"
    }
});
