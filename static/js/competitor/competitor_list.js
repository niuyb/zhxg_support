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

// 渲染department-1
function renderDepartment1(){
    // var Id = "#department-1";
    var Id = "#id_industry_1";
    var data = JSON.parse($("#department-data-1").text());
    renderSelect(Id, data);
}

// option发生变化时，联动下一级行业id_industry-1
function changeDepartmentSelect(Id){
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
    var departmentData = JSON.parse($("#department-data").text());
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

// 当商务部门发生变化时，获取相应下级部门，并对下级部门select元素进行渲染
function onDepartmentChange1(){
    changeDepartmentSelect("id_industry-1")
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

// 为区总确认一列补空
function fillLineToBlack(cellvalue, options, rowObject){
    if (cellvalue === "" || cellvalue === null){
        return "--------";
    }else{
        return cellvalue.split(" ")[0];
    }
}



// 渲染表格中最后一列 操作 operations
function constructOperationCell(cellvalue, options, rowObject){
    var competitor_detail_url = $("#competitor-detail").text();
    var competitor_analysis_url = $("#competitor-analysis").text();
    var competitor_name = rowObject["competitor_name"];
    var competitor_id = rowObject["competitor_id"];
    var canChange = $("#canChangeCompetitor").text();
    var canDelete = $("#canDeleteCompetitor").text();
    // console.log(canChange);
    // console.log(canDelete);
    var remark = rowObject["remark"];
    if(canChange=='1'){
        var a =
            "<a href='#'"
            + " data-toggle='modal'  data-target='#modifyCompetitorModal'"
            + "onclick='modify_competitor(\""+competitor_id+"\",\""+competitor_name+"\",\""+remark+"\")'"
            + "> 修改 </a>"
    }else {
        var a = ''
    }
    if(canDelete=='1'){
        var a =
            "<a href='#'"
            + " data-toggle='modal'  data-target='#deleteCompetitorModal'"
            + "onclick='delete_competitor(\""+competitor_id+"\")'"
            + "> 删除 </a>" + a
    }else {
        var a = a
    }

    return "<a href='"
            + competitor_detail_url + "?competitor_name="
            + competitor_name+"'"
            + " target='_blank'>详情 </a>"
            +"<a href='"
            + competitor_analysis_url + "?id="
            + competitor_id+"' target='_blank'> 分析 </a>"
            + a
}

function delete_competitor(competitor_id) {
    //赋值
    $('#delete_competitor_id').val(competitor_id);
}

function delete_competitor_form(competitor_id) {
    var delete_competitor_url = $("#competitor-list-api").text();
    var competitor_id = $.trim($('#delete_competitor_id').val());
    delete_competitor_url = delete_competitor_url+"?id="+competitor_id;
    // 异步提交数据
    $.ajax(
            {
                url: delete_competitor_url,
                type: "delete",
                beforeSend:function()
                {
                    $("#tip").html("<span style='color:blue'>正在处理...</span>");
                    return true;
                },
                success:function(data)
                {
                    if(data.status === 200)
                    {
                        var msg = "删除";
                        $("#tip").html("<span style='color:blueviolet'>恭喜，" +msg+ "成功！</span>");

                        // location.reload();
                        $('#submitBtn').trigger('click');
                    }
                    else
                    {
                        if(data.status === 2)
                        {
                            $("#tip").html("<span style='color:red'>竞品不存在</span>");
                            alert('竞品不存在');
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
                    $('#deleteCompetitorModal').modal('hide');

                }
            });

    return false;
}
function modify_competitor(competitor_id,competitor_name,remark) {
    //赋值
    $('#competitor_id').val(competitor_id);
    $('#competitor_name').val(competitor_name);
    $('#competitor_remark').val(remark);


}

// 修改竞品提交表单
function modify_competitor_form()
{
    var modify_competitor_url = $("#competitor-list-api").text();
    var competitor_name = $.trim($('#competitor_name').val());
    var competitor_id = $.trim($('#competitor_id').val());
    var competitor_remark = $.trim($('#competitor_remark').val());
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

    modify_competitor_url = modify_competitor_url+"?id="+competitor_id+"&name="+competitor_name+"&remark="+competitor_remark;
    // 异步提交数据
    $.ajax(
            {
                url: modify_competitor_url,
                type: "put",
                beforeSend:function()
                {
                    $("#tip").html("<span style='color:blue'>正在处理...</span>");
                    return true;
                },
                success:function(data)
                {
                    if(data.status === 200)
                    {
                        var msg = "修改";
                        $("#tip").html("<span style='color:blueviolet'>恭喜，" +msg+ "成功！</span>");

                        // location.reload();
                        $('#submitBtn').trigger('click');
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
                    $('#modifyCompetitorModal').modal('hide');

                }
            });

    return false;
}


$(function () { $('#modifyCompetitorModal').on('hide.bs.modal', function () {
    $("#competitor_name").val("");
    $("#competitor_remark").val("");
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
        var query_data = $("#competitor-filter-form").serialize();
        var query = decodeURIComponent(query_data,true); //将数据解码
        url = $("#competitor-list-api").text().trim() +"?" + query;
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
    var op = $("#id_industry-2" + " option:selected").val();
    if(op){
        $("#id_industry-2").css("display", "block");
    }
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



