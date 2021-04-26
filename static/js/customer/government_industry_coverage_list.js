// created by TomTsong 20200108
document.write("<script language=javascript src='/static/js/common.js'></script>");

/*******************************************************************
*
*备注：本js文件中所有department都是行业的意思，改起来会比较麻烦，比较浪费时间，所以不改了
*    
********************************************************************/

// 点击重置按钮后
$("#resetBtn").click(function(){ 
    for (var i=2;i<3;i++){
        $("#department-" + i).empty();
        $("#id_department-" + i).css("display", "none");
    }
    commonSelectReset("location")
})

var commonLocation = new CommonLocation();

function completeOptions(options){
    options.unshift(["", "--------"]);
    // options.push([0, "空白"]);
    return options;
}

function renderStates(){
    let Id = "location-select-1";
    let data = commonLocation.getStates();
    data = completeOptions(data);
    renderSelect(Id, data);
}

//从页面中获取需要检测的字段（用于提交表单之前，对表单中数据进行检验）
function parseCheckFields(){
    var fieldStr = $("#fields-to-check").text();
    var fields = [];
    if (fieldStr){
        fields = fieldStr.trim().split(",");
    }
    return fields;    
}

function checkForm(){
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
    arr.push("xtype=" + 1);
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
    var state = rowObject["state_id"];
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
        }else if (data.col_model[i].name == "state_name"){
            data.col_model[i].formatter = fillLineToBlank;
        }else if (data.col_model[i].name == "city_name"){
            data.col_model[i].formatter = fillLineToBlank;
        }else if (data.col_model[i].name == "district_name"){
            data.col_model[i].formatter = fillLineToBlank;
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
    if (checkForm && !checkForm()){
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
    renderStates();
    renderTable();
    reloadTable();
});

// 点击搜索按钮，用ajax发起请求，并将数据渲染到表格中
$("#submitBtn").click(function(){
    // renderTable();
    reloadTable();
});
