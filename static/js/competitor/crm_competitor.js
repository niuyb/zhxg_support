// created by
document.write("<script language=javascript src='/static/js/common.js'></script>");

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


// 渲染industry-1
function renderIndustry1(){
    var Id = "#industry-1";
    var data = JSON.parse($("#industry-data-1").text());
    renderSelect(Id, data);
}

// 一级行业发生变化时，联动下一级行业,使用前端的select标签
function changeIndustrySelect1(Id){
    var op = $("#" + Id + " option:selected").val();

    var list = Id.split("-");
    var prefix = list[0];
    var index = parseInt(list[1]);

    var nextDivId = "#id_" + prefix + "-" + (index+1);
    var nextSelectId = "#" + prefix + "-" + (index+1);

    // 先清空所有下级select
    for (var i=index+1;i<3;i++){
        $("#industry-" + i).empty();
        $("#id_" + prefix + "-" + i).css("display", "none");
        }

    // 如果本级选择的有值
    if (op){
        // 下一级select数据加载完之前，禁止改选其他option
        for (var i=0;i<=index;i++){
            $("#industry-" + i).attr("disabled", "disabled");
        }
        // // 首先先清空原select元素正面的options
        // $(nextSelectId).empty();

        //将options逐条渲染之后添到select里面
        var departmentData = JSON.parse($("#industry-data").text());
        var data = [["", "全部"]];
        for (var i in departmentData){
            var js = departmentData[i];
            if (op == js["pid"]){
                var item = [];
                item.push(js["id"]);
                item.push(js["name"]);
                data.push(item);
            }
        }

        // 如果data长度大于1，就渲染下一级行业
        if (data.length > 1){
            data.push(["0", "未知"]);
            // 元素恢复显示，然后加载数据
            $(nextDivId).css("display", "block");

            renderSelect(nextSelectId, data);
        }

        // 下一级select数据加载完之后，解禁其他select
        for (var i=0;i<=index;i++){
            $("#industry-" + i).attr("disabled", null);
        }
        }


}

// option发生变化时，联动下一级行业id_industry-1，使用form.py生成的
function changeIndustrySelect(Id){
    var op = $("#" + Id + " option:selected").val();

    var list = Id.split("-");
    var prefix = list[0]; //id_industry
    var index = parseInt(list[1]); //1
    var lastSelectId = "#id_industry_" + (index-1);

    var nextDivId = "#" + prefix + "-" + (index+1);
    var nextSelectId ="#" + prefix + "_" + (index+1);

    // 如果option改成无了，清空所有下级select
    for (var i=index+1;i<3;i++){
        $("#" + prefix + "_" + i).empty();
        $("#" + prefix + "-" + i).css("display", "none");
    }

    // 下一级select数据加载完之前，禁止改选其他option
    for (var i=0;i<=index;i++){
        $("#" + prefix + "_" + i).attr("disabled", "disabled");
    }
    // 首先先清空原select元素正面的options
    $(nextSelectId).empty();

    //将options逐条渲染之后添到select里面
    var departmentData = JSON.parse($("#industry-data").text());
    var data = [["", "全部"]];
    for (var i in departmentData){
        var js = departmentData[i];
        if (op == js["pid"]){
            var item = [];
            item.push(js["id"]);
            item.push(js["name"]);
            data.push(item);
        }
    }

    // 如果data长度大于1，就渲染下一级行业
    if (data.length > 1){
        data.push(["0", "未知"]);
        // 元素恢复显示，然后加载数据
        $(nextDivId).css("display", "block");

        renderSelect(nextSelectId, data);
    }

    // 下一级select数据加载完之后，解禁其他select
    for (var i=0;i<=index;i++){
        $("#" + prefix + "_" + i).attr("disabled", null);
    }
}

// 当一级行业发生变化时，获取相应二级行业，并对二级行业select元素进行渲染
function onIndustryChange1(){
    changeIndustrySelect("id_industry-1")
}



// 渲染department-1
function renderDepartment1(){
    var Id = "#department-1";
    var data = JSON.parse($("#department-data-1").text());
    renderSelect(Id, data);
}

// 行业的option发生变化时，联动下一级部门
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
    var data = [["", "全部"]];
    for (var i in departmentData){
        var js = departmentData[i];
        if (op == js["dpid"]){
            var item = [];
            item.push(js["did"]);
            item.push(js["name"])
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


// 点击重置按钮后
$("#resetBtn").click(function(){ 
    for (var i=2;i<11;i++){
        $("#department-" + i).empty();
        $("#id_department-" + i).css("display", "none");
    }
    for (var i=2;i<4;i++){
        $("#industry-" + i).empty();
        $("#id_industry-" + i).css("display", "none");
    }
    $("#id_competitor_name").val("")
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

// 为区总确认一列补空
function fillLineToBlack(cellvalue, options, rowObject){
    if (cellvalue === "" || cellvalue === null){
        return "--------";
    }else{
        return cellvalue.split(" ")[0];
    }
}

// 为签单金额一列补空
function moneyToBlack(cellvalue, options, rowObject){
    if (cellvalue === 0 || cellvalue === "0"){
        return "--";
    }else{
        return cellvalue;
    }
}

// 为用户名称列 添加跳转链接
function yqmsAccountShowLink(cellvalue, options, rowObject){
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
}

// 为客户名称列 添加跳转链接
function crmCustomerShowLink(cellvalue, options, rowObject){
    var crmCustomerJumpUrl = $("#crm-customer-jump-url").text();
    var customer_id = rowObject["customer_id"];
    var customer_name = rowObject["customer_name"];
    return "<a href='"
            + crmCustomerJumpUrl 
            + customer_id
            + "' target='_blank'>"
            + customer_name 
            + "</a>"
}

// 渲染表格中最后一列 操作 operations
function constructOperationCell(cellvalue, options, rowObject){
    var crmuser_jump_url = $("#crmuser-jump-url").text();
    var customer_id = rowObject["customer_id"];
    var customer_name = rowObject["customer_name"];
    var competitorId = rowObject["competitorId"];
    var competitorProductId = rowObject["competitorProductId"];
    var competitor_money = rowObject["competitor_money"];
    var service_time_start = rowObject["service_time_start"];
    var service_time_finish = rowObject["service_time_finish"];

    return " <a href='"
            + crmuser_jump_url 
            + encodeURI(base64("" + rowObject["customer_id"])) 
            + "' target='_blank'>客户画像</a>| <a href=''"
            + " data-toggle='modal'  data-target='#connectCompetitorModal'"
            + "onclick='reload_connect_html("+customer_id+",\""+customer_name+"\",\""
            + competitorId+"\",\""+competitorProductId+"\",\""+competitor_money
            + "\",\""+service_time_start+"\",\""+service_time_finish
            +"\")'"
            + "id='connectCompetitor' >关联竞品</a>"
}


// 配置并渲染表格
function configureTable(data){    
    // Configuration for jqGrid Example 1
    for (var i in data.col_model){

        if (data.col_model[i].name == "customer_name"){
            data.col_model[i].formatter = crmCustomerShowLink;
        }
        if (data.col_model[i].name == "competitor_money"){
            data.col_model[i].formatter = moneyToBlack;
        }
        if (data.col_model[i].name == "operations"){
            data.col_model[i].formatter = constructOperationCell;
        }
        // if (data.col_model[i].name == "service_time_start"){
        //     data.col_model[i].formatter = fillLineToBlack;
        // }
        // if (data.col_model[i].name == "service_time_finish"){
        //     data.col_model[i].formatter = fillLineToBlack;
        // }

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
        var query_data = $("#competitor-filter-form").serialize();
        var query = decodeURIComponent(query_data,true); //将数据解码
        url = $("#competitor-api").text().trim() +"?" + query;
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
        $('#connectCompetitorModal').modal('hide');

        reloaded(data.items);
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
    renderDepartment1();
    // renderIndustry1();
    renderTable();
    reloadTable();
});

// 点击搜索按钮，用ajax发起请求，并将数据渲染到表格中
$("#submitBtn").click(function(){
    // renderTable();
    reloadTable();
});

// 当点击无区总确认 复选框 时
$("#id_no_service_time").click(function(){
    var checked = $("#id_no_service_time").prop("checked");
    if (checked == "checked" || checked == true){
        $("#datepicker5 input").attr("disabled", "disabled")
    }else{
        $("#datepicker5 input").attr("disabled", null)
    }
});


// 添加竞品提交表单
function check_competitor_form()
{
    var add_competitor_url = $("#add-competitor-url").text();
    var competitor_name = $.trim($('#competitor_name').val());
    var competitor_remark = $.trim($('#competitor_remark').val());
    // var act     = $.trim($('#act').val());

    if(!competitor_name)
    {
        alert('竞品名称不能为空！');
        return false;
    }
    if(competitor_name.length < 2 )
    {
        alert('竞品名称不能少于2个字符！');
        return false;
    }
    if(competitor_name.length > 50 )
    {
        alert('竞品名称不能多于50个字符！');
        return false;
    }
    if(competitor_remark.length > 200 )
    {
        alert('竞品描述不能多于200个字符！');
        return false;
    }
    var form = $('#form_data').serialize(); //序列化内容，结果为一个字符串
    // console.log("form");
    form = form + '&source_type=2';
    var form_data = decodeURIComponent(form,true); //将数据解码
    // console.log("form_data");
    // alert(form_data);

    // 异步提交数据到competitor/api/add-competitor-url页面
    $.ajax(
            {
                url: add_competitor_url,
                // data:{"form_data":form_data,"act":act},
                data:{"form_data":form_data},
                type: "post",
                beforeSend:function()
                {
                    $("#tip").html("<span style='color:blue'>正在处理...</span>");
                    return true;
                },
                success:function(data)
                {
                    if(data.status === 200)
                    {

                        var msg = "添加";
                        // if(act == "edit") msg = "编辑";
                        $("#tip").html("<span style='color:blueviolet'>恭喜，" +msg+ "成功！</span>");

                        // location.reload();
                    }

                    else
                    {
                        if(data.status === 2)
                        {
                            $("#tip").html("<span style='color:red'>竞品已存在</span>");
                            alert('竞品已存在');
                        }
                    else {
                            $("#tip").html("<span style='color:red'>失败，请重试</span>");
                            alert('操作失败');
                        }
                    }
                },
                error:function()
                {
                    alert('请求出错');
                },
                complete:function()
                {
                    $('#acting_tips').hide();
                    $("#competitor_name").val("");
                    $("#competitor_remark").val("");
                    $('#addCompetitorModal').modal('hide');

                }
            });

    return false;
}

$(function () { $('#addCompetitorModal').on('hide.bs.modal', function () {
    // 关闭时清空edit状态为add
    // $("#act").val("add");
    $("#competitor_name").val("");
    $("#tip").html("<span id=\"tip\"> </span>");
    // location.reload();
})
});


//获取列表客户和竞品信息并放入表单中
function reload_connect_html(customer_id,customer_name,competitorId,competitorProductId,
                             competitor_money,service_time_start,service_time_finish) {
var url =  $("#updateSelectForm-url").text();
$.ajax(
            {
                url: url,
                type: "get",
                success:function(data)
                {
                    if(data.status === 200)
                    {
                        var Id = "#id_competitorId";
                        $(Id).html("");
                        message = data.message;
                        renderSelect(Id, message);
                    }
                },
                error:function()
                {
                    alert('请求出错');
                },
                complete:function()
                {
                    //赋值
                    $('#customer_id').val(customer_id);
                    $('#customer_name').val(customer_name);

                    if(competitor_money!="--"){
                        competitor_money = parseInt(competitor_money.replace(",",""));
                        $('#competitor_money').val(competitor_money);
                    }
                    if(service_time_start!="--"){
                        $('#service_time_start').val(service_time_start);
                    }
                    if(service_time_finish!="--"){
                        $('#service_time_finish').val(service_time_finish);
                    }
                    if(competitorId!="--"){
                        $('#id_competitorId').val(competitorId);
                    }
                    if(competitorProductId!="--"){
                        $('#id_competitorProductId').val(competitorProductId);
                    }

                    $('#customer_name').attr("readonly","readonly");

                }
            });

}

$(function () { $('#connectCompetitorModal').on('hide.bs.modal', function () {
    // 关闭时清空edit状态为add
    $("#id_competitorId").val("");
    $("#id_competitorProductId").val("");
    $("#competitor_money").val("");
    $("#service_time_start").val("------");
    $("#service_time_finish").val("------");
    $("#tip").html("<span id=\"tip\"> </span>");
    // location.reload();
})
});

// 关联竞品提交表单
function connect_competitor_form()
{
    $('#customer_name').attr("readonly",false);
    var connect_competitor_url = $("#connect-competitor-url").text();
    var competitor_name = $.trim($('#id_competitorId').val());
    var competitor_money = $.trim($('#competitor_money').val());

    if(!competitor_name)
    {
        $('#customer_name').attr("readonly","readonly");
        alert('竞品名称不能为空！');
        return false;
    }
    if(!competitor_money)
    {
        $('#customer_name').attr("readonly","readonly");
        alert('签单金额不能为空！');
        return false;
    }

    var form = $('#connect_form_data').serialize(); //序列化内容
    var form_data = decodeURIComponent(form,true); //将数据解码

    // 异步提交数据到competitor/api/add-competitor-url页面
    $.ajax(
            {
                url: connect_competitor_url,
                data:{"form_data":form_data},
                type: "post",
                beforeSend:function()
                {
                    $("#tip").html("<span style='color:blue'>正在处理...</span>");
                    return true;
                },
                success:function(data)
                {
                    if(data.status == 200)
                    {

                        var msg = "关联";
                        $("#tip").html("<span style='color:blueviolet'>恭喜，" +msg+ "成功！</span>");

                        // location.reload();
                        $('#submitBtn').trigger('click');
                        $('#customer_name').attr("readonly","readonly");
                        // $('#connectCompetitorModal').modal('hide');
                    }
                    else {
                        if (data.status === 2) {
                            $("#tip").html("<span style='color:red'>该竞品已关联过，请修改关联信息</span>");
                            alert('该竞品已关联过，请修改关联信息');
                            $('#customer_name').attr("readonly","readonly");
                        }

                    else {
                            $("#tip").html("<span style='color:red'>失败，请重试</span>");
                            alert('操作失败');
                            $('#customer_name').attr("readonly","readonly");
                        }

                }
                },
                error:function()
                {
                    alert('请求出错');
                    $('#customer_name').attr("readonly","readonly");
                },
                complete:function()
                {
                    $('#acting_tips').hide();
                    $('#customer_name').attr("readonly","readonly");
                    // $("#competitor_name").val("");

                }
            });
    return false;
}




