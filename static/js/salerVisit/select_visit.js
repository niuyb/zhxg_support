// created by wucx 20200702
document.write("<script language=javascript src='/static/js/common.js'></script>");

$(document).ready(function () {
    $('#data_5 .input-daterange').datepicker({
        keyboardNavigation: false,
        forceParse: false,
        autoclose: true
    });
    renderDepartment1();
    reloadMapData();
    // map();

});

// 渲染department-1
function renderDepartment1() {
    var Id = "#department-1";
    var data = JSON.parse($("#department-data-1").text());
    renderSelect(Id, data);
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

// 点击搜索按钮，用ajax发起请求，并将数据渲染到表格中
$("#map_submitBtn").click(function(){
    // renderTable();
    reloadMapData();
});

// 点击重置按钮后
$("#map_resetBtn").click(function(){
    for (var i=2;i<11;i++){
        $("#department-" + i).empty();
        $("#id_department-" + i).css("display", "none");
    }

    $("#saler_name").val("")
});


// 检测表单中是否含有非法的值
function checkForm(){

    return true;
}


// 访问接口，并将获取地图的数据
function reloadMapData(url){
    if (!url){
        var query_data = $("#visit-filter-form").serialize();
        var query = decodeURIComponent(query_data,true); //将数据解码
        url = $("#visit_detail-api").text().trim() +"?" + query;
        url = url + '&type=detail_map'

    }

    // 核验表单中数据是否合法
    if (!checkForm()){
        return false;
    }
    $("#map_submitBtn").attr("disabled", "disabled");
    $("#map_submitBtn").text("加载中...");

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

        // 关闭弹出层
        parent.layer.close(index);

        ul_detail_data(data.items);
        select_map(data.items);
        $("#map_submitBtn").attr("disabled", null);
        $("#map_submitBtn").text("搜索");
    });
}

// 渲染地图
function select_map(visit_detail) {

    // var visit_detail = $("#visit_detail").text();
    // // 将string类型转为数组对象
    // var visit_detail = eval(visit_detail);
    // 创建地图实例
     //创建地图
    var map = new AMap.Map('container', {
        zoom: 4,
        center: [102.342785, 35.312316],
        resizeEnable: true
    });
   // 创建一个 icon
    var endIcon_red = new AMap.Icon({
        size: new AMap.Size(25, 34),
        //image: '//a.amap.com/jsapi_demos/static/demo-center/icons/dir-marker.png',
        image: "../static/img/位置红.png"
        //imageSize: new AMap.Size(135, 40),
        //imageOffset: new AMap.Pixel(-95, -3)
    });
    var endIcon_blue = new AMap.Icon({
        size: new AMap.Size(25, 34),
        //image: '//a.amap.com/jsapi_demos/static/demo-center/icons/dir-marker.png',
        image: "../static/img/位置蓝.png"
        //imageSize: new AMap.Size(135, 40),
        //imageOffset: new AMap.Pixel(-95, -3)
    });
    var visit_data = [];
    var path = [];
    var path_detail = [];
    var problem_list = ['1','2','3','4'];
    // 设置鼠标浮动后的窗口
    var infoWindow = new AMap.InfoWindow({offset: new AMap.Pixel(0, -30)});
    for (var i=0;i<visit_detail.length;i++) {

        var lng = visit_detail[i].longitude;
        var lat = visit_detail[i].latitude;
        if(lng==null ||lng=="" || lng=="undefined" ||lat==null || lat=="" || lat=="undefined"){
            continue;
        }
        var starttime = visit_detail[i].starttime;
        var salename = visit_detail[i].salename;
        var accountname = visit_detail[i].accountname;
        var opportunityname = visit_detail[i].opportunityname;
        var distance = visit_detail[i].distance;
        var problem_type = visit_detail[i].problem_type;
        if(isInArray(problem_list,problem_type)){
                var icon=endIcon_red;
        }else {
            var icon=endIcon_blue;
        }
        // 以 icon URL 的形式创建一个途经点
        var viaMarker = new AMap.Marker({
            position: new AMap.LngLat(parseFloat(lng), parseFloat(lat)),
            // 将一张图片的地址设置为 icon
            //icon: '//a.amap.com/jsapi_demos/static/demo-center/icons/dir-via-marker.png',
            icon: icon,
            // 设置了 icon 以后，设置 icon 的偏移量，以 icon 的 [center bottom] 为原点
            offset: new AMap.Pixel(-16, -30)
        });

        if(icon==endIcon_blue){
            content = '<p>序号：' + (i+1) +'</p>';
        }else {
            content = '<p style="color:red;"><b>拜访问题：'+ visit_detail[i].problem_content +'</b></p>';
            content += '<p>序号：' + (i+1)+'</p>';
        }

        // content = '<p>序号：' + (i+1)+'</p>';
        content += '<p>时间：' + starttime+'</p>';
        content += '<p>商务：' + salename+'</p>';
        content += '<p>商机：' + opportunityname+'</p>';
        content += '<p>最终客户：' + accountname+'</p>';
        content += '<p>距离：' + distance+' 公里</p>';
        content += '<p>沟通内容：' + visit_detail[i].content+'</p>';
        viaMarker.content = content;
        viaMarker.on('mouseover', infoOpen);
        viaMarker.on('mouseout', infoClose);
        visit_data.push(viaMarker);
        path.push([parseFloat(lng), parseFloat(lat)]);
        path_detail.push(content)
        // console.log(lng,lat);
    };
    // 将 markers 添加到地图
    map.add(visit_data);
    function infoClose(e) {
        infoWindow.close(map, e.target.getPosition());
    }
    function infoOpen(e) {
        infoWindow.setContent(e.target.content);
        infoWindow.open(map, e.target.getPosition());
    }

    // AMapUI.load(['ui/misc/PathSimplifier', 'lib/$'], function(PathSimplifier, $) {
    //
    //     if (!PathSimplifier.supportCanvas) {
    //         alert('当前环境不支持 Canvas！');
    //         return;
    //     }
    //
    //     var pathSimplifierIns = new PathSimplifier({
    //         //zIndex: 100,
    //         autoSetFitView:false,
    //         map: map, //所属的地图实例
    //
    //         getPath: function(pathData, pathIndex) {
    //
    //             return pathData.path;
    //         },
    //         getHoverTitle: function(pathData, pathIndex, pointIndex) {
    //
    //             if (pointIndex >= 0) {
    //                 //point
    //                 content = pathData.name + '，第' + (pointIndex+1) + '个拜访的客户\n';
    //                 content += pathData.path_detail[pointIndex];
    //                 return content ;
    //             }
    //
    //             return pathData.name + '，拜访数量' + pathData.path.length;
    //         },
    //         renderOptions: {
    //
    //             renderAllPointsIfNumberBelow: 100 //绘制路线节点，如不需要可设置为-1
    //         }
    //     });
    //
    //     window.pathSimplifierIns = pathSimplifierIns;
    //
    //     //设置数据
    //     pathSimplifierIns.setData([{
    //         name: '本时段',
    //         path: path,
    //         path_detail: path_detail
    //     }]);
    //
    //     //对第一条线路（即索引 0）创建一个巡航器
    //     var navg1 = pathSimplifierIns.createPathNavigator(0, {
    //         loop: true, //循环播放
    //         speed: 1000000 //巡航速度，单位千米/小时
    //     });
    //
    //     navg1.start();
    // });

}


function isInArray(arr,value){
for(var i = 0; i < arr.length; i++){
    if(value === arr[i]){
        return true;
    }
}
return false;
}

// 渲染右侧详情数据
function ul_detail_data(visit_detail) {
    var problem_list = ['1','2','3','4'];
    document.getElementById("ul_visit_detail").innerHTML = '<p><b>共'+visit_detail.length +'条拜访记录</b><\/p>';
    for (var i=0;i<visit_detail.length;i++) {
        var li_content = "";
        if(isInArray(problem_list,visit_detail[i].problem_type)){
            var con_img = "<img src=\"../static/img/警报.png\"><p style=\"color:red;\"><b>拜访问题：" + visit_detail[i].problem_content + "<\/b><\/p>"
        }else {
            var con_img = "<img src=\"../static/img/足迹2蓝色.png\">"
        }
        li_content = "<li>"
                    +  con_img
                    +  "<p>序号：<b>"+(i+1) + "<\/b><\/p>"
                    +  "<p>时间：<b>"+visit_detail[i].starttime + "<\/b><\/p>"
                    +  "<p>商务："+visit_detail[i].salename + "<\/p>"
                    +  "<p>商机："+visit_detail[i].opportunityname + "<\/p>"
                    +  "<p>最终客户："+visit_detail[i].accountname + "<\/p>"
                    +  "<p>打卡地："+visit_detail[i].location +"<\/p>"
                    +  "<p>距离客户："+visit_detail[i].distance+"公里<\/p>"
                    +  "<p style=\"margin-bottom: 10px\">沟通内容："+visit_detail[i].content+"<\/p>"
                    +  "<hr style=\"border: 1px dashed #ff0000;\">"
                    +  "<\/li>";
        document.getElementById("ul_visit_detail").innerHTML += li_content;
        // console.log(li_content);

    }
    // console.log($("#ul_visit_detail").text());

}

