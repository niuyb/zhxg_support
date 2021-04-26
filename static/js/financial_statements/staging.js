$(function(){
    //页面加载完成之后执行
    $.jgrid.defaults.styleUI = 'Bootstrap';
    pageInit();
});
function pageInit(){
    var query = $("#search-form").serialize();
    formQuery = query;
    url = '/financial_statements/getStagingList' +"?" + query;
    //创建jqGrid组件
    $("#table_list_11").jqGrid(
    {
        url : url,//组件创建完成之后请求数据的url
        datatype : "json",//请求数据返回的类型。可选json,xml,txt
        colNames : [ '开票类型', '发票审批通过时间', '最终客户名称', '开票项目', '合同类型','合同编号', '订单实际负责人', '省份', '合同开始日期', '合同结束日期','赠送开始日期', '赠送结束日期' ],//jqGrid的列显示名字
        colModel : [ //jqGrid每一列的配置信息。包括名字，索引，宽度,对齐方式.....
             {name : 'entityType',index : 'entityType',width : 30}, 
             {name : 'customItem43__c',index : 'customItem43__c',width : 40}, 
             {name : 'customItem66__c',index : 'customItem66__c',width : 80}, 
             {name : 'customItem6',index : 'customItem6',width : 100,align : "left"}, 
             {name : 'customItem30__c',index : 'customItem30__c',width : 60,align : "left"}, 
             {name : 'customItem37__c',index : 'customItem37__c',width : 120,align : "left"}, 
             {name : 'customItem53__c',index : 'customItem53__c',width : 60,sortable : false}, 
             {name : 'customItem34__c',index : 'customItem34__c',width : 80}, 
             {name : 'customItem28__c',index : 'customItem28__c',width : 30}, 
             {name : 'customItem29__c',index : 'customItem29__c',width : 60},
             {name : 'customItem50__c',index : 'customItem50__c',width : 120},
             {name : 'customItem48__c',index : 'customItem48__c',width : 80}
        ],
        autowidth: true,
        height: "320",
        shrinkToFit: true,
        rowNum : 30,//一页显示多少条
        rowList : [ 10, 20, 30 ],//可供用户选择一页显示多少条
        pager : '#pager_list_11',//表格页脚的占位符(一般是div)的id
        sortname : 'customItem43__c',//初始化的时候排序的字段
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