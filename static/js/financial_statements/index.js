$(function(){
    //页面加载完成之后执行
    $.jgrid.defaults.styleUI = 'Bootstrap';
    pageInit();
});
function pageInit(){
    var query = $("#search-form").serialize();
    formQuery = query;
    url = '/financial_statements/getlist' +"?" + query;
    //创建jqGrid组件
    $("#table_list_11").jqGrid(
    {
        url : url,//组件创建完成之后请求数据的url
        datatype : "json",//请求数据返回的类型。可选json,xml,txt
        colNames : [ '序号', '发票类别', '合同号', '开票日期', '发票号码','购方名称', '发票金额', '合计金额', '税率', '合计税额','主要商品名称', '备注' ],//jqGrid的列显示名字
        colModel : [ //jqGrid每一列的配置信息。包括名字，索引，宽度,对齐方式.....
             {name : 'serial_number',index : 'serial_number',width : 30}, 
             {name : 'invoice_category',index : 'invoice_category',width : 40}, 
             {name : 'contract_number',index : 'contract_number',width : 80}, 
             {name : 'billing_date',index : 'billing_date',width : 100,align : "left"}, 
             {name : 'invoice_number',index : 'invoice_number',width : 60,align : "left"}, 
             {name : 'purchaser_name',index : 'purchaser_name',width : 120,align : "left"}, 
             {name : 'invoice_amount',index : 'invoice_amount',width : 60,sortable : false}, 
             {name : 'total_amount',index : 'total_amount',width : 80}, 
             {name : 'tax_rate',index : 'tax_rate',width : 30}, 
             {name : 'total_tax',index : 'total_tax',width : 60},
             {name : 'commodity_name',index : 'commodity_name',width : 120},
             {name : 'remarks',index : 'remarks',width : 80}
        ],
        autowidth: true,
        height: "320",
        shrinkToFit: true,
        rowNum : 30,//一页显示多少条
        rowList : [ 10, 20, 30 ],//可供用户选择一页显示多少条
        pager : '#pager_list_11',//表格页脚的占位符(一般是div)的id
        sortname : 'serial_number',//初始化的时候排序的字段
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