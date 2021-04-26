// created by wucx 20200702
document.write("<script language=javascript src='/static/js/common.js'></script>");

$(document).ready(function () {
    map();

});



function map() {

    var visit_detail = $("#visit_detail").text();
    // alert(visit_detail);
    // 将string类型转为数组对象
    var visit_detail = eval(visit_detail);
    // 创建地图实例
    var map = new AMap.Map("container", {
        zoom: 4,
        // center: [116.4,39.92],
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
    var problem_list = ['1','2','3','4'];
    function isInArray(arr,value){
    for(var i = 0; i < arr.length; i++){
        if(value === arr[i]){
            return true;
        }
    }
    return false;
    }
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
            viaMarker.content = '<p>时间：' + starttime+'</p>';
        }else {
            viaMarker.content = '<p style="color:red;"><b>拜访问题：'+ visit_detail[i].problem_content +'</b></p>';
            viaMarker.content += '<p>时间：' + starttime+'</p>';
        }

        viaMarker.content += '<p>商务：' + salename+'</p>';
        viaMarker.content += '<p>商机：' + opportunityname+'</p>';
        viaMarker.content += '<p>最终客户：' + accountname+'</p>';
        viaMarker.content += '<p>距离：' + distance+' 公里</p>';
        viaMarker.content += '<p>沟通内容：' + visit_detail[i].content +'</p>';
        viaMarker.on('mouseover', infoOpen);
        viaMarker.on('mouseout', infoClose);
        visit_data.push(viaMarker);
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


}


