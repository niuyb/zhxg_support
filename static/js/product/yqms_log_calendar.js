function yqmsLogCalendar(){
    var userid = getUrlKey('uid', window.location.href);   // 获取当前页面的url中的uid的值
    var today = new Date();
    today.setDate(today.getDate());
    today = today.toLocaleDateString().split('/').join('-');
    $.post("/product/yqms_accounts/yqms_log_calendar_api",{uid:userid},function(msg){
        // msg = JSON.stringify(msg);   # 将object转为string
        // msg = JSON.parse(msg);   # 将string转为object
        // console.log(typeof msg);
        var calendarEl = document.getElementById('my-calendar');
        var myDate = new Date();
        var now = myDate.getFullYear()+'-'+(myDate.getMonth() + 1)+'-'+myDate.getDate();
        var calendar = new FullCalendar.Calendar(calendarEl, {
            locale :  "zh-cn",
            plugins: ['interaction', 'dayGrid'],
            defaultDate: today,
            editable: true,
            eventLimit: true, // allow "more" link when too many events
            events: msg,
        });
        calendar.render();
    })
}
