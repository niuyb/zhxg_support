// created by
document.write("<script language=javascript src='/static/js/common.js'></script>");

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


// 点击重置按钮后
$("#resetBtn").click(function(){ 
    for (var i=2;i<11;i++){
        $("#id_industry_" + i).empty();
        $("#id_industry-" + i).css("display", "none");
    }
    // // 清空并隐藏城市和区县   
    // $("#id_customer_county").empty();
    // $("#id_county").css("display", "none");
    // $("#id_customer_city").empty();
    // $("#id_city").css("display", "none");
});

//从页面中获取需要检测的字段（用于提交表单之前，对表单中数据进行检验）
function parseCheckFields(){
    var fieldStr = $("#fields-to-check").text();
    var fields = [];
    if (fieldStr){
        fields = fieldStr.trim().split(",");
    }
    return fields;    
}

// 检测表单中是否含有非法的值
function checkForm(){
    var $o = $("#login-days-input");
    var loginDays = $o.val();
    if (loginDays == null || loginDays == undefined || loginDays == ""){
        $o.val(0);
    }
    var loginDays = parseInt($o.val());
    var minNum = $o.attr("min");
    var maxNum = $o.attr("max");
    if (minNum && (loginDays < parseInt(minNum))){
        return false;
    }
    if (maxNum && (loginDays > parseInt(maxNum))){
        return false;
    }
    return true;
}


$(function () { $('#modifyuser_logModal').on('hide.bs.modal', function () {
    $("#operation_type").val("");
    $("#user_log_remark").val("");
    $("#tip").html("<span id=\"tip\"> </span>");
})
});

// 配置并渲染表格
function configureTable(data){
    // Configuration for jqGrid Example 1
    for (var i in data.col_model){


        if (data.col_model[i].name == "service_time_start"){
            data.col_model[i].formatter = fillLineToBlack;
        }
        if (data.col_model[i].name == "service_time_finish"){
            data.col_model[i].formatter = fillLineToBlack;
        }
        if (data.col_model[i].name == "operations"){
            data.col_model[i].formatter = constructOperationCell;
        }
    }
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
        // $('#table_list_2').setGridWidth(width);
    });
}



// 获取api，访问api，获取数据后，渲染表格
function renderTable() {
    $.jgrid.defaults.styleUI = 'Bootstrap';
    var initData = JSON.parse($("#init-data").text());
    configureTable(initData);
}

// 访问接口，并将获取到的数据重新加载到表格中
function reloadTable(url){
    if (!url){
        var query_data = $("#user_log-filter-form").serialize();
        var query = decodeURIComponent(query_data,true); //将数据解码
//        url = $("#user_log-list-api").text().trim() +"?" + query;
        url = "/user_log/api/get_user_log" +"?" + query;
    }
    // 核验表单中数据是否合法
    if (!checkForm()){
        return false;
    }
    $("#submitBtn").attr("disabled", "disabled");
    $("#submitBtn").text("加载中...");

    // 弹出层 —— 加载中特效
    var index = parent.layer.load(0, {shade: false});

    $.get(url, function(data, status){
        if (data.status == null || data.status == undefined){
            // window.location.reload();
            return;
        }
        if (data.status < 1){
            alert(data.message);
        }
        function reloaded(items){
            $("#table_list_1").jqGrid('clearGridData');
            $("#table_list_1").jqGrid('setGridParam', {
                datatype: 'local',
                data: items,
                page: 1
            }).trigger("reloadGrid");
        };
        // 关闭弹出层
        parent.layer.close(index);

        reloaded(data.items);
        $("#submitBtn").attr("disabled", null);
        $("#submitBtn").text("搜索");
    });
}


// 点击搜索按钮，用ajax发起请求，并将数据渲染到表格中
$("#submitBtn").click(function(){
    // renderTable();
    reloadTable();
});



// 页面加载完毕后，调用一些函数
$(document).ready(function () {
    $('#data_6 .input-daterange').datepicker({
        keyboardNavigation: false,
        forceParse: false,
        autoclose: true
    });
    renderTable();
    reloadTable();
});



