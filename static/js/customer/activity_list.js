// created by TomTsong 20200108
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
    url = $("#activity-export-file").text().trim() +"?" + formQuery + "&" + query;
    exporting = false;
    var newTab = window.open(url);
    // newTab.location.href = url;
    // newTab.close();

    // $.get(url, function(result, status){
    //     if (result.status !== 1){
    //         exporting = false;
    //         // window.location.reload();
    //         return;
    //     }
    //     let uri = 'data:text/csv;charset=utf-8,\ufeff' + encodeURIComponent(result.data);
    //     //通过创建a标签实现
    //     let link = document.createElement("a");
    //     link.href = uri;
    //     //对下载的文件命名
    //     link.download =  "客户活跃度统计.csv";
    //     document.body.appendChild(link);
    //     link.click();
    //     document.body.removeChild(link);
    //     exporting = false;
    // });
}

// 当省份发生变化时，获取相应城市，并对城市select元素进行渲染
function onProvinceChange(){
    var province = $("#id_customer_province option:selected").val();
    // 将城市、区县select清空并隐藏
    $("#id_customer_county").empty();
    $("#id_county").css("display", "none");
    $("#id_customer_city").empty();
    $("#id_city").css("display", "none");
    // 如果省份为空，直接返回
    if (!province){
        return
    }
    // 当加载城市信息时，禁止更改省份
    $("#id_customer_province").attr("disabled", "disabled");
    var url = $("#cities-api").text() + "?pid=" + province;
    $.get(url, function(data, status){
        // 元素恢复显示，然后加载数据
        $("#id_city").css("display", "block");
        // 首先先清空原select元素正面的options
        $("#id_customer_city").empty();
        //将options逐条渲染之后添到select里面
        for (var index in data){
            var vn = data[index];
            var option = "<option value=" + vn[0] + ">" + vn[1] + "</option>";
            $("#id_customer_city").append(option);
        }       
        // 城市信息加载完毕之后，解禁省份 
        $("#id_customer_province").attr("disabled", null);
    });    
}

// 当城市发生变化时，获取相应城市，并对城市select元素进行渲染
function onCityChange(){
    var city = $("#id_customer_city option:selected").val();
    if (!city){
        // 如果城市为空，就将区县select清空并隐藏
        $("#id_customer_county").empty();
        $("#id_county").css("display", "none");
        return
    }
    // 当加载区县信息时，禁止更改省份和城市
    $("#id_customer_province").attr("disabled", "disabled");
    $("#id_customer_city").attr("disabled", "disabled");

    var url = $("#counties-api").text() + "?pid=" + city;
    $.get(url, function(data, status){
        // 元素恢复显示，然后加载数据
        $("#id_county").css("display", "block");
        // 首先先清空原select元素正面的options
        $("#id_customer_county").empty();
        //将options逐条渲染之后添到select里面
        for (var index in data){
            var vn = data[index];
            var option = "<option value=" + vn[0] + ">" + vn[1] + "</option>";
            $("#id_customer_county").append(option);
        }
        // 区县信息加载完毕之后，解禁省份和城市           
        $("#id_customer_province").attr("disabled", null);
        $("#id_customer_city").attr("disabled", null);
    });    
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
    // 首先先清空原select元素下面的options
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


// option发生变化时，联动下一级行业
function changeIndustrySelect(Id){
    var op = $("#" + Id + " option:selected").val();

    var list = Id.split("-");
    var prefix = list[0];
    var index = parseInt(list[1]);
    var lastSelectId = "#industry-" + (index-1);

    var nextDivId = "#" + prefix + "-" + (index+1);
    var nextSelectId = "#industry-" + (index+1);

    // 如果option改成无了，清空所有下级select
    for (var i=index+1;i<11;i++){
        $("#industry-" + i).empty();
        $("#" + prefix + "-" + i).css("display", "none");
    }

    // 下一级select数据加载完之前，禁止改选其他option
    for (var i=0;i<=index;i++){
        $("#industry-" + i).attr("disabled", "disabled");
    }
    // 首先先清空原select元素下面的options
    $(nextSelectId).empty();

    //将options逐条渲染之后添到select里面
    var departmentData = JSON.parse($("#industry-data").text());
    var data = [["", "--------"]];
    for (var i in departmentData){
        var js = departmentData[i];
        if (op == js["pid"]){
            var item = [];
            item.push(js["id"]);
            item.push(js["name"]);
            data.push(item);
        }
    }

    // 如果data长度大于1，就渲染下一级部门
    if (data.length > 1){
        // 元素恢复显示，然后加载数据
        $(nextDivId).css("display", "block");

        renderSelect("#industry-" + (index+1), data);
    }
    
    // 下一级select数据加载完之后，解禁其他select
    for (var i=0;i<=index;i++){
        $("#industry-" + i).attr("disabled", null);
    }
}

// 当一级行业发生变化时，获取相应二级行业，并对二级行业select元素进行渲染
function onIndustryChange1(){
    changeIndustrySelect("id_industry-1")
}

// 点击重置按钮后
$("#resetBtn").click(function(){ 
    for (var i=2;i<11;i++){
        $("#department-" + i).empty();
        $("#id_department-" + i).css("display", "none");
    }
    // // 清空并隐藏城市和区县   
    // $("#id_customer_county").empty();
    // $("#id_county").css("display", "none");
    // $("#id_customer_city").empty();
    // $("#id_city").css("display", "none");
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

// 向后台发送客户活跃度统计的用户操作记录
function activityUserLog(url){
    if (!url){
        url = $("#user-log-url").text().trim();
    }
    var info = {};
    var message = $("#activity-filter-form").serialize();
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
    return cellvalue.split(" ")[0];
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
    }else if (rowObject["product_type"] == "2"){
        var tsgzAccountJumpUrl = $("#tsgz-account-jump-url").text();
        var pas = rowObject["pas"];
        var account_name = rowObject["account_name"];
        var query = "&loginName=" + encodeURI(account_name) + "&password=" + pas;
        return "<a href='"
                + tsgzAccountJumpUrl 
                + query
                + "' target='_blank'>"
                + account_name 
                + "</a>"
    }else if (rowObject["product_type"] == "3"){
        return "<a href='javascript:void(0);' the-id='wp_alert_btn' org-id='"+rowObject["uid"]+"'>"+cellvalue+"</a>"
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
    }else if (rowObject["product_type"] == "2"){
        var tsgz_user_jump_url = $("#tsgz-user-jump-url").text();
        var crmuser_jump_url = $("#crmuser-jump-url").text();
        return "<a href='"
                + tsgz_user_jump_url 
                + encodeURI(rowObject["account_name"]) 
                + "' target='_blank'>查看用户</a> | <a href='"
                + crmuser_jump_url 
                + encodeURI(base64("" + rowObject["customer_id"])) 
                + "' target='_blank'>客户画像</a>"
    }else if (rowObject["product_type"] == "3"){
        var wp_user_jump_url = $("#wp-user-jump-url").text();
        var crmuser_jump_url = $("#crmuser-jump-url").text();
        return "<a href='"
                + wp_user_jump_url 
                + encodeURI(rowObject["account_name"]) 
                + "' target='_blank'>查看用户</a> | <a href='"
                + crmuser_jump_url 
                + encodeURI(base64("" + rowObject["customer_id"])) 
                + "' target='_blank'>客户画像</a>"
    }else{
        return "--------|--------"
    }    
}

function json2csv(json) {
    var csv = [];
    for (var i in json) {
        var item = json[i];
        var temp = [];	
        for (var k in item){
            var v = item[k];
            if (v == undefined || v == null){
                v = "";
            }
            temp.push(v)
        }
        temp.pop(); // 移除最后一列operations
        csv.push(temp.join(','));
    };
    // csv.shift();
    return csv.join('\n');
}

function table2csv(table) {
    var csv = [];
    $(table).find('tr').each(function() {
        var temp = [];	
        $(this).find('td').each(function() {
            temp.push($(this).html());
        })
        temp.shift(); // 移除第一个
        csv.push(temp.join(','));
    });
    csv.shift();
    return csv.join('\n');
}

// csv转sheet对象
function csv2sheet(csv) {
    var sheet = {}; // 将要生成的sheet
    csv = csv.split('\n');
    csv.forEach(function(row, i) {
        row = row.split(',');
        if(i == 0) sheet['!ref'] = 'A1:'+String.fromCharCode(65+row.length-1)+(csv.length-1);
        row.forEach(function(col, j) {
            sheet[String.fromCharCode(65+j)+(i+1)] = {v: col};
        });
    });
    return sheet;
}

// 将一个sheet转成最终的excel文件的blob对象，然后利用URL.createObjectURL下载
function sheet2blob(sheet, sheetName) {
    sheetName = sheetName || 'sheet1';
    var workbook = {
        SheetNames: [sheetName],
        Sheets: {}
    };
    workbook.Sheets[sheetName] = sheet;
    // 生成excel的配置项
    var wopts = {
        bookType: 'xlsx', // 要生成的文件类型
        bookSST: false, // 是否生成Shared String Table，官方解释是，如果开启生成速度会下降，但在低版本IOS设备上有更好的兼容性
        type: 'binary'
    };
    var wbout = XLSX.write(workbook, wopts);
    var blob = new Blob([s2ab(wbout)], {type:"application/octet-stream"});
    // 字符串转ArrayBuffer
    function s2ab(s) {
        var buf = new ArrayBuffer(s.length);
        var view = new Uint8Array(buf);
        for (var i=0; i!=s.length; ++i) view[i] = s.charCodeAt(i) & 0xFF;
        return buf;
    }
    return blob;
}

/**
 * 通用的打开下载对话框方法，没有测试过具体兼容性
 * @param url 下载地址，也可以是一个blob对象，必选
 * @param saveName 保存文件名，可选
 */
function openDownloadDialog(url, saveName)
{
    var yes = 0;
    if(typeof url == 'object' && url instanceof Blob)
    {
        url = URL.createObjectURL(url); // 创建blob地址
        yes = 1;
    }
    var aLink = document.createElement('a');
    aLink.href = url;
    aLink.download = saveName || ''; // HTML5新增的属性，指定保存文件名，可以不要后缀，注意，file:///模式下不会生效
    var event;
    if(window.MouseEvent) event = new MouseEvent('click');
    else
    {
        event = document.createEvent('MouseEvents');
        event.initMouseEvent('click', true, false, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
    }
    aLink.dispatchEvent(event);
    if (yes){
        URL.revokeObjectURL(url);
    }
}

// 配置并渲染表格
function configureTable(data){    
    // Configuration for jqGrid Example 1
    for (var i in data.col_model){
        if (data.col_model[i].name == "account_name"){
            data.col_model[i].formatter = accountShowLink;
        }
        if (data.col_model[i].name == "customer_name"){
            data.col_model[i].formatter = crmCustomerShowLink;
        }
        if (data.col_model[i].name == "opportunity_name"){
            data.col_model[i].formatter = fillLineToBlank;
        }
        if (data.col_model[i].name == "industry_l1"){
            data.col_model[i].formatter = fillLineToBlank;
        }
        if (data.col_model[i].name == "industry_l2"){
            data.col_model[i].formatter = fillLineToBlank;
        }
        if (data.col_model[i].name == "dbcdate15"){
            data.col_model[i].formatter = fillDbcDate;
        }
        if (data.col_model[i].name == "dbcdate10"){
            data.col_model[i].formatter = fillDbcDate;
        }
        if (data.col_model[i].name == "operations"){
            data.col_model[i].formatter = constructOperationCell;
        }
    }
    
    // // 导出excel
    // function exportCsv(){
    //     var col_json = {};
    //     for (var i in data.col_model){
    //         if (data.col_model[i].name !== "operations"){
    //             col_json[data.col_model[i].name] = data.col_names[i];
    //         }
    //     }
    //     var str = "";
    //     var heads = [];
    //     for (var k in col_json){
    //         heads.push(col_json[k]);
    //     }        
    //     str += heads.join(",");
    //     var items = $("#table_list_1").jqGrid('getGridParam', "data");
    //     for (var i in items){
    //         str += "\n";
    //         var row = [];
    //         for (var k in col_json){
    //             var v = items[i][k];
    //             if (v == null || v == undefined){
    //                 v = "";
    //             }
    //             row.push(v + "\t");
    //         }
    //         str += row.join(",");
    //     }
    //     let uri = 'data:text/csv;charset=utf-8,\ufeff' + encodeURIComponent(str);
    //     //通过创建a标签实现
    //     let link = document.createElement("a");
    //     link.href = uri;
    //     //对下载的文件命名
    //     link.download =  "活跃度统计.csv";
    //     document.body.appendChild(link);
    //     link.click();
    //     document.body.removeChild(link);
    //     activityUserLog();
    // }
    
    // // 导出excel（当前table页中的数据）
    // function exportCsv(){
    //     // var items = $("#table_list_1").jqGrid('getGridParam', "data");
    //     // var sheet = XLSX.json_to_sheet(items);
    //     var csv = table2csv($("#table_list_1"));
	// 	var sheet = csv2sheet(csv);
	// 	var blob = sheet2blob(sheet);
	// 	openDownloadDialog(blob, '客户活跃度统计.xlsx');
    //  activityUserLog();
    // }
    
    // // 导出excel（后台一次性加载过来的全部数据）
    // function exportCsv(){
    //     var col_json = {};
    //     for (var i in data.col_model){
    //         if (data.col_model[i].name !== "operations"){
    //             col_json[data.col_model[i].name] = data.col_names[i];
    //         }
    //     }
    //     var csv = [];
    //     var heads = [];
    //     for (var k in col_json){
    //         heads.push(col_json[k]);
    //     }
    //     csv.push(heads.join(","));
    //     var items = $("#table_list_1").jqGrid('getGridParam', "data");
    //     for (var i in items){
    //         var row = [];
    //         for (var k in col_json){
    //             var v = items[i][k];
    //             if (v == null || v == undefined){
    //                 v = "";
    //             }
    //             row.push(v + "\t");
    //         }
    //         csv.push(row.join(","));
    //     }
    //     csv = csv.join("\n");
    //     // var items = $("#table_list_1").jqGrid('getGridParam', "data");
    //     // var csv = json2csv(items);
	// 	var sheet = csv2sheet(csv);
	// 	var blob = sheet2blob(sheet);
	// 	openDownloadDialog(blob, '客户活跃度统计.xlsx');
    //     activityUserLog();
    // }

    function exportCsv(){
        var fields = ['account_name', 'customer_name', 'opportunity_name', 
                'dbcdate15', 'dbcdate10', 'saler', 'department_name', 
                'account_status', 'customer_province', 'login_days'].join(",")
        exportDataToFile(fields, "csv", 0);
    }
    // 将exportCsv设置成window的成员函数，否则jqgrid无法调用此函数
    window.exportCsv = exportCsv;

    // 如果有导出数据的权限，便可以看到导出按钮
    var caption = "";
    if (data.export_activity_data_access){
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

    // // 添加工具栏lui_table_list_1
    // jqg.navGrid('#pager_list_1', {edit:false, add:false, del:false, search:false, refresh:false});

    // // 如果有导出数据的权限，便可以看到导出按钮
    // if (data.export_activity_data_access){
    //     jqg.navButtonAdd('#pager_list_1', {
    //         position: 'last', 
    //         title: '导出为Excel文件', 
    //         caption: '导出', 
    //         onClickButton: exportCsv
    //     });
    // }

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
        var query = $("#activity-filter-form").serialize();
        formQuery = query;
        url = $("#activity-api").text().trim() +"?" + query;
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
    $('#data_4 .input-daterange').datepicker({
        keyboardNavigation: false,
        forceParse: false,
        autoclose: true
    });
    $('#data_5 .input-daterange').datepicker({
        keyboardNavigation: false,
        forceParse: false,
        autoclose: true
    });
    $('#data_6 .input-daterange').datepicker({
        keyboardNavigation: false,
        forceParse: false,
        autoclose: true
    });
    renderDepartment1();
    renderTable();
    reloadTable();
});

// 点击搜索按钮，用ajax发起请求，并将数据渲染到表格中
$("#submitBtn").click(function(){
    // renderTable();
    reloadTable();
});

// 当点击无区总确认 复选框 时
$("#id_no_quzong_ok").click(function(){
    var checked = $("#id_no_quzong_ok").prop("checked");
    if (checked == "checked" || checked == true){
        $("#datepicker5 input").attr("disabled", "disabled")
    }else{
        $("#datepicker5 input").attr("disabled", null)
    }
})
$('#table_list_1').on('click','[the-id=wp_alert_btn]',function(){
    $('#wpModalLabel').find('span').html($(this).text());
    var wp_account_url = $('#wp-account-url').text();
    var org_id = $(this).attr('org-id');
    $.ajax({
        url:wp_account_url,
        type:'get',
        data:{org_id:org_id},
        dateType:'json',
        success:function(res){
            var wp_account_jump_url = $('#wp-account-jump-url').text();
            var str = '';
            str += '<tr>';
            str += '<th>账号名称</th>';
            str += '<th>状态</th>';
            str += '</tr>';
            $.each(res,function(index,arr){
                str += '<tr>';
                str += '<td><a href="'+wp_account_jump_url+'&loginName='+encodeURI(arr['login_name'])+'&loginPasswd='+arr['login_pwd']+'" target="_blank">'+arr['login_name']+'</a></td>';
                if (arr['status'] == 1) {
                    str += '<td>开启</td>';
                } else {
                    str += '<td>关闭</td>';
                }
                str += '</tr>';
            })
            $('#mobal-data').html(str)
        }
    });
    $('#wp-modal').modal();
})