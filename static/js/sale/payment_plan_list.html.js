// created by TomTsong 20200319
document.write("<script language=javascript src='/static/js/common.js'></script>");

// 方便数据导出时候，传递筛选条件
var formQuery = "";
var exporting = false;

// 访问接口，并将获取到的数据重新加载到表格中
function exportDataToFile(fields, fileType, page){
    if (exporting){
        return;
    }
    exporting = true;
    if (!fileType){
        fileType = "";
    }
    if (!fields){
        fileType = "";
    }
    if (!page){
        page = "";
    }
    var query = "fileType=" + encodeURI(fileType) + "&page=" + encodeURI(page) + "&fields=" + encodeURI(fields);
    url = $("#export-file").text().trim() +"?" + formQuery + "&" + query;
    exporting = false;
    var newTab = window.open(url);
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

// 渲染department-1
function renderDepartment1(){
    var Id = "department-1";
    var data = JSON.parse($("#department-data-1").text());
    renderSelect(Id, data);
}

// option发生变化时，联动下一级部门
function changeDepartmentSelect(Id){
    var op = $("#" + Id + " option:selected").val();
    
    // 更改department-input的值
    $("#department-value").val(op);

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
    var data = [["", "--------"]];
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


// // 点击重置按钮后
// $("#resetBtn").click(function(){ 
//     for (var i=2;i<11;i++){
//         $("#department-" + i).empty();
//         $("#id_department-" + i).css("display", "none");
//     }
// })

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

// 向后台发送用户操作记录
function sendUserLog(url){
    if (!url){
        url = $("#user-log-url").text().trim();
    }
    var info = {};
    var message = $("#search-form").serialize();
    var action = "导出";
    info["message"] = message;
    info["action"] = action;
    info["model"] = "客户活跃度统计";
    return userLog(url, info);
}

// 用连线补空
function fillLineToBlank(cellvalue, options, rowObject){
    if (cellvalue === "" || cellvalue === null){
        return "--------";
    }else{
        return cellvalue.split(" ")[0];
    }
}

// 为区总确认日期列和合同截止日期列补空
function fillDbcDate(cellvalue, options, rowObject){
    cellvalue = fillLineToBlank(cellvalue, options, rowObject)
    if (!cellvalue){
        return "--------";
    }
    return new Date(parseInt(cellvalue)).toLocaleDateString().replace("/", "-").replace("/", "-");
}

// 为用户名称列 添加跳转链接
function accountShowLink(cellvalue, options, rowObject){
    if (rowObject["product_type"] == "1"){
        var yqmsAccountJumpUrl = $("#yqms-account-jump-url").text();
        var pas = rowObject["pas"];
        var account_name = rowObject["account_name"];
        var query = "&userid=" + encodeURI(account_name) + "&password=" + pas;
        return "<a href='"
                + yqmsAccountJumpUrl 
                + query
                + "' target='_blank'>"
                + account_name 
                + "</a>"
    }else{
        return cellvalue;
    }    
}

// 为客户名称列 添加跳转链接
function crmCustomerShowLink(cellvalue, options, rowObject){
    var crmCustomerJumpUrl = $("#crm-customer-jump-url").text();
    // var uid = rowObject["uid"];
    var customer_id = rowObject["customer_id"];
    // var customer_name = rowObject["customer_name"];
    return "<a href='"
            + crmCustomerJumpUrl 
            + customer_id
            + "' target='_blank'>"
            // + customer_name 
            + cellvalue
            + "</a>"
}

// 渲染表格中最后一列 操作 operations
function constructOperationCell(cellvalue, options, rowObject){
    if (rowObject["product_type"] == "1"){
        var msuser_jump_url = $("#msuser-jump-url").text();
        var crmuser_jump_url = $("#crmuser-jump-url").text();
        return "<a href='"
                + msuser_jump_url 
                + encodeURI(rowObject["account_name"]) 
                + "' target='_blank'>查看用户</a> | <a href='"
                + crmuser_jump_url 
                + encodeURI(base64("" + rowObject["customer_id"])) 
                + "' target='_blank'>客户画像</a>"
    }else{
        return "--------|--------"
    }    
}

// 千分位
function format(num){
    var sNum=num.toFixed(2)+'',    //将传入的值【四舍五入】保留2位小数
        re=/(\d+)(\d{3})/;
        
    if( /\.\d{3}/.test(num+'') ){
        if(sNum.charAt(0)!='-'){
            //如果传入的值不只两位小数，就向前进1保留2位小数，如：1.2400001 -> 1.25
            sNum=sNum.substring(0,sNum.length-1)+(parseInt(sNum.slice(-1))+1);
        }
    }    //向前进1的情况太多，没考虑周全，比如说0.999 -0.0009
        
    while(re.test(sNum)){
        sNum=sNum.replace(re,'$1,$2');
    }
    
    return sNum;
}

function delformat(sNum){
    return sNum.replace(/,/g,'');
}

function toThousands(cellvalue, options, rowObject){
    if (!cellvalue){
        return "--------";
    }
    return format(cellvalue);
}

function parseOverdueStatus(cellvalue, options, rowObject){
    if (!cellvalue){
        return "--------";
    }
    return {"": "--------", "0": "未逾期", "1": "已逾期"}[cellvalue];
}

// 配置并渲染表格
function configureTable(data){    
    // Configuration for jqGrid Example 1
    for (var i in data.col_model){
        if (data.col_model[i].name == "amount" || data.col_model[i].name == "actualAmount"){
            data.col_model[i].formatter = toThousands;
        }
        else if (data.col_model[i].name == "overdueStatus"){
            data.col_model[i].formatter = parseOverdueStatus;
        }
        // if (data.col_model[i].name == "account_name"){
        //     data.col_model[i].formatter = accountShowLink;
        // }
        // if (data.col_model[i].name == "customer_name"){
        //     data.col_model[i].formatter = crmCustomerShowLink;
        // }
        // if (data.col_model[i].name == "opportunity_name"){
        //     data.col_model[i].formatter = fillLineToBlank;
        // }
        else if (data.col_model[i].name == "planTime"){
            data.col_model[i].formatter = fillDbcDate;
        }
        // if (data.col_model[i].name == "dbcdate10"){
        //     data.col_model[i].formatter = fillDbcDate;
        // }
        // if (data.col_model[i].name == "operations"){
        //     data.col_model[i].formatter = constructOperationCell;
        // }
    }

    function exportCsv(){
        var fields = ['ding_user', 'content', 'notice_type', 'status', 'ctime'].join(",")
        exportDataToFile(fields, "csv", 0);
    }
    // 将exportCsv设置成window的成员函数，否则jqgrid无法调用此函数
    window.exportCsv = exportCsv;

    // 如果有导出数据的权限，便可以看到导出按钮
    var caption = "";
    if (data.export_payment_plan_list_access){
        caption = "<span class='glyphicon glyphicon-new-window' onclick='exportCsv()' title='导出为csv' style='cursor: pointer;'>"
                + "<span class='bold' style='margin-left: 5px;'>导出</span></span>"
    }

    var jqg = $("#table_list_1").jqGrid({
        "data": data.items,
        // topToolbar: true,
        // topToolbarId: "grid-table-top-toolbar",
        // toolbar: [true, "top"],
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
        // 将导出按钮安放到表格头部。这里用了投机取巧的方法，将title-tool-bar的caption写成html，html里面包含onclick事件，以此来达到将导出按钮部署到表格头部。
        'caption': caption,
        hidegrid: false,
        loadComplete: function(gridObject){$("#table_list_1 .ui-jqgrid-title").css("padding-top", "0");}
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

// 数据导出
function reloadTable(url){
    if (!url){
        var query = $("#search-form").serialize();
        formQuery = query;
        url = $("#search-data-api").text().trim() +"?" + query;
    }

    // 核验表单中数据是否合法
    if (!checkForm()){
        console.log("form is not valid.")
        return false;
    }
    $("#submitBtn").attr("disabled", "disabled");
    $("#submitBtn").text("加载中...");

    // 弹出层 —— 加载中特效
    var index = parent.layer.load(0, {shade: false});
    
    $.get(url, function(result, status){
        if (result.code == null || result.code == undefined){
            // window.location.reload();
            return;
        }
        if (result.code < 1){
            alert(result.msg);
        }
        function reloaded(items){
            console.log("table reloaded.");
            $("#table_list_1").jqGrid('clearGridData');
            $("#table_list_1").jqGrid('setGridParam', {
                datatype: 'local',
                data: items,
                page: 1
            }).trigger("reloadGrid");
        };
        // 关闭弹出层
        parent.layer.close(index);
        reloaded(result.data);
        $("#submitBtn").attr("disabled", null);
        $("#submitBtn").text("搜索");
    });
}

// 页面加载完毕后，调用一些函数
$(document).ready(function () {
    $('#data_5 .input-daterange').datepicker({
        keyboardNavigation: false,
        forceParse: false,
        autoclose: true
    });
    // $('#data_6 .input-daterange').datepicker({
    //     keyboardNavigation: false,
    //     forceParse: false,
    //     autoclose: true
    // });
    // renderDepartment1();
    renderTable();
    reloadTable();
});

// 点击搜索按钮，用ajax发起请求，并将数据渲染到表格中
$("#submitBtn").click(function(){
    // renderTable();
    reloadTable();
});