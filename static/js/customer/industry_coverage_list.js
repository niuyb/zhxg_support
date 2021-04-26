// created by TomTsong 20200108
document.write("<script language=javascript src='/static/js/common.js'></script>");

/*******************************************************************
*
*备注：本js文件中所有department都是行业的意思，改起来会比较麻烦，比较浪费时间，所以不改了
*    
********************************************************************/


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

// option发生变化时，联动下一级行业
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
    for (var i=index+1;i<3;i++){
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
        if (op == js["pid"]){
            var item = [];
            item.push(js["id"]);
            item.push(js["name"])
            data.push(item);
        }
    }

    // 如果data长度大于1，就渲染下一级行业
    if (data.length > 1){
        data.push(["0", "未知"]);
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


// 点击重置按钮后
$("#resetBtn").click(function(){ 
    for (var i=2;i<3;i++){
        $("#department-" + i).empty();
        $("#id_department-" + i).css("display", "none");
    }
})

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

// 用连线补空
function fillLineToBlank(cellvalue, options, rowObject){
    if (cellvalue === "" || cellvalue === null){
        return "--------";
    }else{
        return cellvalue;
    }
}

// 为基数、覆盖数、正式和试用数制作查看详情用的链接
function makeLinkCount(industry1, industry2, state, city, district, coverage, status){
    var baseLink = "/customer/list?";
    industry1 == undefined || industry1 == null ? industry1 = "" : industry1;
    industry2 == undefined || industry2 == null ? industry2 = "" : industry2;
    state == 0 || state == undefined || state == null ? state = "" : state;
    city == 0 || city == undefined || city == null ? city = "" : city;
    district == 0 || district == undefined || district == null ? district = "" : district;
    coverage == undefined || coverage == null ? coverage = "" : coverage;
    status == undefined || status == null ? status = "" : status;
    var arr = [];
    arr.push("industry1=" + industry1);
    arr.push("industry2=" + industry2);
    arr.push("state=" + state);
    arr.push("city=" + city);
    arr.push("district=" + district);
    arr.push("coverage=" + coverage);
    arr.push("status=" + status);
    var query = arr.join("&");
    baseLink += query;
    return baseLink;
}

// 为基数、覆盖、正式、试用等添加链接
function addLinkCount(cellvalue, options, rowObject, coverage, status){
    if (cellvalue == "0"){
        return cellvalue;
    }
    var industry1 = rowObject["industry1_id"];
    var industry2 = rowObject["industry2_id"];
    var state = rowObject["province_id"];
    var city = rowObject["city_id"];
    var district = rowObject["district_id"];
    var url = makeLinkCount(industry1, industry2, state, city, district, coverage, status);
    return "<a style='display: inline-block; width: 100%;' href='"
            + url 
            + "' target='_blank'>"
            + cellvalue
            + "</a>"
}

// 为基数添加链接
function addLinkBaseCount(cellvalue, options, rowObject){
    return addLinkCount(cellvalue, options, rowObject, null, null)
}

// 为基数添加链接
function addLinkHaveCount(cellvalue, options, rowObject){
    return addLinkCount(cellvalue, options, rowObject, 1, null)
}

// 为基数添加链接
function addLinkFormalCount(cellvalue, options, rowObject){
    return addLinkCount(cellvalue, options, rowObject, 1, 2)
}

// 为基数添加链接
function addLinkTrialCount(cellvalue, options, rowObject){
    return addLinkCount(cellvalue, options, rowObject, 1, 1)
}

// 为竞品数字制作查看详情用的链接
function makeLinkCompetitorCount(industry1, industry2, location){
    var baseLink = "/competitor/competitorList?";
    industry1 == undefined || industry1 == null ? industry1 = "" : industry1;
    industry2 == undefined || industry2 == null ? industry2 = "" : industry2;
    location == undefined || location == null ? location = "" : location;
    var arr = [];
    arr.push("industry_1=" + industry1);
    arr.push("industry_2=" + industry2);
    arr.push("customer_province=" + location);
    var query = arr.join("&");
    baseLink += query;
    return baseLink;
}

// 为竞品数字添加链接
function addLinkCompetitorCount(cellvalue, options, rowObject, coverage, status){
    if (cellvalue == "0"){
        return cellvalue;
    }
    var industry_1 = rowObject["industry1_id"];
    var industry_2 = rowObject["industry2_id"];
    var customer_province = rowObject["province_id"];
    var url = makeLinkCompetitorCount(industry_1, industry_2, customer_province);
    return "<a style='display: inline-block; width: 100%;' href='"
            + url 
            + "' target='_blank'>"
            + cellvalue
            + "</a>"
}

// 为客户名称列 添加跳转链接
function crmCustomerShowLink(cellvalue, options, rowObject){
    var crmCustomerJumpUrl = $("#crm-customer-jump-url").text();
    var uid = rowObject["uid"];
    var customer_name = rowObject["customer_name"];
    return "<a href='"
            + crmCustomerJumpUrl 
            + uid 
            + "' target='_blank'>"
            + customer_name 
            + "</a>"
}

// 渲染表格中最后一列 操作 operations
function constructOperationCell(cellvalue, options, rowObject){
    var msuser_jump_url = $("#msuser-jump-url").text();
    var crmuser_jump_url = $("#crmuser-jump-url").text();
    return "<a href='"
            + msuser_jump_url 
            + encodeURI(rowObject["account_name"]) 
            + "' target='_blank'>查看用户</a> | <a href='"
            + crmuser_jump_url 
            + encodeURI(base64("" + rowObject["customer_id"])) 
            + "' target='_blank'>客户画像</a>"
}

// 配置并渲染表格
function configureTable(data){    
    for (var i in data.col_model){
        if (data.col_model[i].name == "base_count"){
            data.col_model[i].formatter = addLinkBaseCount;
        }else if (data.col_model[i].name == "have_count"){
            data.col_model[i].formatter = addLinkHaveCount;
        }else if (data.col_model[i].name == "formal_count"){
            data.col_model[i].formatter = addLinkFormalCount;
        }else if (data.col_model[i].name == "trial_count"){
            data.col_model[i].formatter = addLinkTrialCount;
        }else if (data.col_model[i].name == "competitor_count"){
            data.col_model[i].formatter = addLinkCompetitorCount;
        }
    }

    // 如果有导出数据的权限，便可以看到导出按钮
    var caption = "";
    if (data.export_industry_coverage_list_access){
        caption = "<span class='glyphicon glyphicon-new-window' onclick='exportCsv()' title='导出为csv' style='cursor: pointer;'>"
                + "<span class='bold' style='margin-left: 5px;'>导出</span></span>"
    }

    // Configuration for jqGrid Example 1
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

// 访问接口，并将获取到的数据重新加载到表格中
function reloadTable(url){
    if (!url){
        var query = $("#industry-coverage-filter-form").serialize();
        url = $("#industry-coverage-api").text().trim() +"?" + query;
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

// 页面加载完毕后，调用一些函数
$(document).ready(function () {
    // $('#data_5 .input-daterange').datepicker({
    //     keyboardNavigation: false,
    //     forceParse: false,
    //     autoclose: true
    // });
    // $('#data_6 .input-daterange').datepicker({
    //     keyboardNavigation: false,
    //     forceParse: false,
    //     autoclose: true
    // });
    renderDepartment1();
    renderTable();
    reloadTable();
});

// 点击搜索按钮，用ajax发起请求，并将数据渲染到表格中
$("#submitBtn").click(function(){
    // renderTable();
    reloadTable();
});
