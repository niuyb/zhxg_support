$(function(){
    //页面加载完成之后执行
    $.jgrid.defaults.styleUI = 'Bootstrap';
    pageInit();
});
function pageInit(){
    $('#downLoad').html('快速分期').removeAttr("disabled");
    var query = $("#search-form").serialize();
    formQuery = query;
    url = '/financial_statements/get_standing_book' +"?" + query;
    //创建jqGrid组件
    $("#table_list_11").jqGrid(
    {
        url : url,//组件创建完成之后请求数据的url
        datatype : "json",//请求数据返回的类型。可选json,xml,txt
        colNames : [ '归档编号', '合同生效日期', '合同编号', '合同类型', '标的/项目名称','客户名称（盖章客户名称）', '合同金额', '实际金额', '备注' ],//jqGrid的列显示名字
        colModel : [ //jqGrid每一列的配置信息。包括名字，索引，宽度,对齐方式.....
             {name : 'filing_number',index : 'filing_number',width : 50}, 
             {name : 'contract_start_date',index : 'filing_date',width : 60}, 
             {name : 'contract_number',index : 'contract_number',width : 80}, 
             {name : 'contract_type',index : 'contract_type',width : 60,align : "left"}, 
             {name : 'subject_matter_name',index : 'subject_matter_name',width : 80,align : "left"}, 
             {name : 'customer_name',index : 'customer_name',width : 140,align : "left"}, 
             {name : 'contract_amount',index : 'contract_amount',width : 50,sortable : false}, 
             {name : 'actual_amount',index : 'actual_amount',width : 50}, 
             {name : 'remarks',index : 'remarks',width : 80}
        ],
        autowidth: true,
        height: "320",
        shrinkToFit: true,
        rowNum : 30,//一页显示多少条
        rowList : [ 10, 20, 30 ],//可供用户选择一页显示多少条
        pager : '#pager_list_11',//表格页脚的占位符(一般是div)的id
        sortname : 'contract_start_date',//初始化的时候排序的字段
        sortorder : "desc",//排序方式,可选desc, asc
        mtype : "get",//向后台请求数据的ajax的类型。可选post,get
        viewrecords : true,
        hidegrid: false,
        loadComplete: function(gridObject){$("#table_list_11 .ui-jqgrid-title").css("padding-top", "0");}
        // caption : "JSON Example"//表格的标题名字
    });
    /*创建jqGrid的操作按钮容器*/
    /*可以控制界面上增删改查的按钮是否显示*/
    // jQuery("#table_list_1").jqGrid('navGrid', '#pager_list_1', {edit : false,add : false,del : false});
}
laydate.render({
    elem: '#star_date', //指定元素
    type: 'datetime'
});
laydate.render({
    elem: '#end_data', //指定元素
    type: 'datetime'
});
$('#downLoad').on('click', function(){
    $('#downLoad').html('正在处理中，请稍后……').attr("disabled",'disabled');
    var jump = $(this).attr('jump');
    var query = $("#search-form").serialize();
    var file_path = $('[name="file_path"]').val()
    url = jump +"?" + query;
    $.ajax({
        type:'get',
        url:url,
        dataType:'json',
        success : function(res){
            if (res.status==1) {
                $('#downLoad').html('处理完毕，请查看附件')
                location=file_path + '/' + res.data;
            }else{
                alert(res.msg);
            }
        }
    })
})