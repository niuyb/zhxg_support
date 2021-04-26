
axios.defaults.headers.common['X-CSRFToken'] = $("input[name='csrfmiddlewaretoken']").val(); 

var app = new Vue({
    el: '#app',
    delimiters: ["[[", "]]"],
    data() {
      return {
        tableData: [],
        multipleSelection: []
      }
    },
    created(){
        this.getTableData();
    },
    methods: {
        getTableData(){
            let self = this;
            let url = "/xman/module/tree/all/api";
            axios.get(url).then(function(res){
                self.tableData = res.data.data;
            }).catch(function(err){
                console.log(err);
            })
        },
      toggleSelection(rows) {
        if (rows) {
          rows.forEach(row => {
            this.$refs.multipleTable.toggleRowSelection(row);
          });
        } else {
          this.$refs.multipleTable.clearSelection();
        }
      },
      handleSelectionChange(val) {
        this.multipleSelection = val;
      },
      update(row){
      },
      changeStatus(index, row){
        let self = this;
        let url = "/xman/module";
        let _row = JSON.parse(JSON.stringify(row));
        if (_row.status){
            _row.status = 1;
        }else{
            _row.status = 0;
        }
        
        delete _row.children;

        let data = Qs.stringify(_row);

        axios.patch(url, data).then(function(res){
            let msg = "状态修改失败";
            if (res.data.code == 1){
                if (row.status){
                    msg = "模块\"" + row.name + "\"成功启用";
                }else{
                    msg = "模块\"" + row.name + "\"成功禁用";
                }
                self.$message.success(msg);                
            }else{
                msg = msg + "，" + res.data.error.split("，")[1];
                self.$message.error(msg);
                row.status = !row.status;
            }            
        }).catch(function(err){
            self.$message.error(err);
            row.status = !row.status;
        });
      },
      handleAdd(a, b){
        let parent = b.id;
        let url = "/xman/module?parent=" + parent;
        window.location.href = url;
      },
      handleEdit(a, b){
        let id = b.id;
        let url = "/xman/module?id=" + id;
        window.location.href = url;
      },
      _delete(a, b){
          let self = this;
          let id = b.id;
          let url = "/xman/module?id=" + id;
          axios.delete(url).then(res => {
              if (res.data.code === 1){
                self.$message.success(res.data.error);

                // 删除成功之后，需要刷新表格
                bg.refresh();
              }else{
                self.$message.error(res.data.error);
              }
          }).catch(err => {
            self.$message.error(err);
          })
      },
      handleDelete(a, b){
        let self = this;
        self.$confirm('确认删除模块 "' + b.name + '" 吗？')
        .then(_ => {
            self._delete(a, b);
        }).catch(_ => {});
      }
    }
});


var bg = new Vue({
    el: "#button-group",
    data(){
        return {
            refreshing: false
        }
    },
    methods: {
        refresh(){
            var self = this;
            this.refreshing = true;
            app.getTableData();
            setTimeout(function(){self.refreshing = false;}, 3000);
        },
        create(){
            let url = "/xman/module";
            window.open(url);
        }
    }
});
