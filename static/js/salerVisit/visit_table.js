// created by wucx 20200702
document.write("<script language=javascript src='/static/js/common.js'></script>");

$(document).ready(function () {
    $('#data_5 .input-daterange').datepicker({
        keyboardNavigation: false,
        forceParse: false,
        autoclose: true
    });
    renderDepartment1();
    renderTable();
    reloadTable();
    // map();

});

// 渲染department-1
function renderDepartment1() {
    var Id = "#department-1";
    var data = JSON.parse($("#department-data-1").text());
    renderSelect(Id, data);
}

// 当商务部门发生变化时，获取相应下级部门，并对下级部门select元素进行渲染
function onDepartmentChange1(){
    changeDepartmentSelect("id_department-1")
}
function onDepartmentChange2(){
    changeDepartmentSelect("id_department-2")
}
function onDepartmentChange3(){
    changeDepartmentSelect("id_department-3")
}
function onDepartmentChange4(){
    changeDepartmentSelect("id_department-4")
}
function onDepartmentChange5(){
    changeDepartmentSelect("id_department-5")
}
function onDepartmentChange6(){
    changeDepartmentSelect("id_department-6")
}
function onDepartmentChange7(){
    changeDepartmentSelect("id_department-7")
}
function onDepartmentChange8(){
    changeDepartmentSelect("id_department-8")
}
function onDepartmentChange9(){
    changeDepartmentSelect("id_department-9")
}
function onDepartmentChange10(){
    changeDepartmentSelect("id_department-10")
}

// option发生变化时，联动下一级部门
function changeDepartmentSelect(Id){
    var op = $("#" + Id + " option:selected").val();

    // 更改department-input的值
    $("#department-value").val(op);
    $("#department-value0").val(op);

    var list = Id.split("-");
    var prefix = list[0];
    var index = parseInt(list[1]);
    var lastSelectId = "#department-" + (index-1);

    var nextDivId = "#" + prefix + "-" + (index+1);
    var nextSelectId = "#department-" + (index+1);

    // 如果option改成无了，清空所有下级select
    for (var i=index+1;i<11;i++){
        $("#department-" + i).empty();
        $("#" + prefix + "-" + i).css("display", "none");
    }
    if (!op){
        // 更改department-input的值
        var dep = $(lastSelectId + " option:selected").val();
        $("#department-value").val(dep);
        $("#department-value0").val(dep);
        return;
    }

    // 下一级select数据加载完之前，禁止改选其他option
    for (var i=0;i<=index;i++){
        $("#department-" + i).attr("disabled", "disabled");
    }
    // 首先先清空原select元素正面的options
    $(nextSelectId).empty();

    //将options逐条渲染之后添到select里面
    var departmentData = JSON.parse($("#department-data").text());
    var data = [["", "全部"]];
    for (var i in departmentData){
        var js = departmentData[i];
        if (op == js["dpid"]){
            var item = [];
            item.push(js["did"]);
            item.push(js["name"]);
            data.push(item);
        }
    }

    // 如果data长度大于1，就渲染下一级部门
    if (data.length > 1){
        // 元素恢复显示，然后加载数据
        $(nextDivId).css("display", "block");

        renderSelect("#department-" + (index+1), data);
    }

    // 下一级select数据加载完之后，解禁其他select
    for (var i=0;i<=index;i++){
        $("#department-" + i).attr("disabled", null);
    }
}


// 渲染select
function renderSelect(Id, data){
    for (var i in data){
        var vn = data[i];
        var option = "<option value=" + vn[0] + ">" + vn[1] + "</option>";
        if (Id.indexOf("#") !== 0){
            Id = "#" + Id;
        }
        $(Id).append(option);
    }
}

// 点击搜索按钮，用ajax发起请求，并将数据渲染到表格中
$("#map_submitBtn").click(function(){
    // renderTable();
    reloadTable();
});

// 点击重置按钮后
$("#map_resetBtn").click(function(){
    $('#department-value').val("");
    for (var i=2;i<11;i++){
        $("#department-" + i).empty();
        $("#id_department-" + i).css("display", "none");
    }
    try{
        $("#saler_name0").css("display", "none");
        $("#saler_name0").attr("disabled", "disabled");
        $("#department-value0").css("display", "none");
        $("#department-value0").attr("disabled", "disabled");
    }catch (e){
        console.log(e);
    }
    $("#saler_name").css("display", "block");
    $("#saler_name").attr("disabled", false);
    $("#saler_name").val("");
    $("#department-value").css("display", "block");
    $("#department-value").attr("disabled", false);
    $("#department-value").val("");
    // console.log($("#saler_name").val());
});

// 点击导出按钮
function exportDataToExcel() {
    var query = $("#export_condition").text();
    var url = $("#export_data").text().trim() +"?" + query;
    window.open(url);
}


// 检测表单中是否含有非法的值
function checkForm(){

    return true;
}

// 配置并渲染表格
function configureTable(data){
    $("#table_list_1").jqGrid({
        "data": data.items,
        datatype: "local",
        height: "620",
        autowidth: true,
        shrinkToFit: true,
        rowNum: data.row_num,
        rowList: data.row_list,
        colNames: data.col_names,
        colModel: data.col_model,
        pager: "#pager_list_1",
        viewrecords: true,
        // caption: "jqGrid 示例1",
        hidegrid: false
    });

    // Add responsive to jqGrid
    $(window).bind('resize', function () {
        var width = $('.jqGrid_wrapper').width();
        $('#table_list_1').setGridWidth(width);
    });
}

// 获取api，访问api，获取数据后，渲染表格
function renderTable() {
    $.jgrid.defaults.styleUI = 'Bootstrap';
    var initData = JSON.parse($("#init-data").text());
    configureTable(initData);
}




// 访问接口，并将获取地图的数据
function reloadTable(url){
    if (!url){
        var query_data = $("#visit-filter-form").serialize();
        var query = decodeURIComponent(query_data,true); //将数据解码
        url = $("#visit_detail-api").text().trim() +"?" + query;
        url = url + '&type=detail_table'

    };
    // 核验表单中数据是否合法
    if (!checkForm()){
        return false;
    }
    $("#export_condition").text(query);
    $("#map_submitBtn").attr("disabled", "disabled");
    $("#map_submitBtn").text("加载中...");

    // 弹出层 —— 加载中特效
    var index = parent.layer.load(0, {shade: false});

    $.get(url, function(data, status){
        if (data.status == null || data.status == undefined){
            // window.location.reload();
            return;
        }
        if (data.status < 1){
            alert(data.message);

            $("#map_submitBtn").attr("disabled", null);
            $("#map_submitBtn").text("搜索");
        }

        // 关闭弹出层
        parent.layer.close(index);
        function reloaded(items){
            $("#table_list_1").jqGrid('clearGridData');
            $("#table_list_1").jqGrid('setGridParam', {
                datatype: 'local',
                data: items,
                page: 1
            }).trigger("reloadGrid");
        };


        reloaded(data.items);
        $("#map_submitBtn").attr("disabled", null);
        $("#map_submitBtn").text("搜索");
        // console.log(data);
        reloadStaffSort(data.staff_visit_count);
    });
}


function reloadStaffSort(items) {
    document.getElementById("staff_visit_detail").innerHTML = '';
    var query = $("#export_condition").text();
    var url = $("#visit_detail-table").text().trim() +"?" + query;
    url = url + '&type=detail_table';
    var li_content = "";
    for (var i=0;i<items.length;i++) {

        li_content = li_content
                    + "<li>"
                    +  (i+1) + '. '
                    +  '<a  href='+url.replace(/saler=&/,'saler='+items[i].salename +'&')+'>'+items[i].salename + ': '
                    +  items[i].count
                    +  ' 次 <\/a>'
                    +  "<\/li>";


    }
    document.getElementById("staff_visit_detail").innerHTML += li_content;
    // console.log(li_content);


        }
