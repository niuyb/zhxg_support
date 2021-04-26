// 2020-04-26 生成客户、商机假数据

var str = "获取指定字符串个数林景之博客园年月日获取指定字符串个数参考源字符串百度快照获取字符串中特定字符的个数论坛条回复发帖时间年月日年月日盲点如何判断字符串中某个特定字符的个数实现在字符串中提取数字和字母实现在字符串中提取数字和字百度快照获取一个字符串中指定字符串第次出现的位置小哥博客园年月日获取一个字符串中指定字符串第次出现的位置了解类似的获取字符位置的用法是字符串对象是指定的位置位置从开始数百度快照实现统计字符串中特定字符出现个数的方法技巧脚本年月日这篇文章主要介绍了实现统计字符串中特定字符出现个数的方法涉及针对字符串中字符运算操作相关技巧需要的朋友可以参考下脚本之家百度快照里如何统计字符串中的某个字符的个数百度知道个回答回答时间年月日最佳答案可以利用正则表达式进程获取要计算的字符使用百度知道百度快照中寻找一个字符串中某个字符的个数个回答年月日最佳答案获取一个字符串中字母的个数个回答年月日最佳答案更多同站结果如何从中的字符串中提取特定数据问答云社区年月日我的字符串将始终以下列格式返回其中数字代表我需要定位的变化变量腾讯云计算百度快照在字符串中提取数字梦和远方的博客博客年月日提取字符串中的数字方法很多今天讲几种常用的方法提供的方法获取字符串转换数字方法主要有三种转换函数强制类型转换利用变量弱类技术社区百度快照字符串中提取数字的博客博客年月日中的方法传的可以有非数字字符串只要字符串前面就照样运行知道遇到非数字字符停下来比如以下这个例子元等级技术社区百度快照如何使用获取指定字符中某个字符串存在的个数呢下文讲述代码中获取一个字符串在另一个字符串中存在的个数的方法分享如下所示实现思路使用正则表达式替换待检测字符串字符串减少的个数除以待检测百度快照获取指定字符串个数简书获取指定字符串个数前端召唤师关注字数阅读参考简书社区百度快照";

var customers = [];
var opportunities = [];

function genNum(){
    var r = Math.random().toString();
    return r[5];
}

function genName(length){
    var name = "";
    if (length > 0){
        var i = length;
    }else{
        var i = "5";
        for (var x=0; x<10; x++){
            var r = genNum();
            if (r != 0){
                if (r < 5){
                    i = "1" + r;
                    break;
                }else{
                    i = r;
                    break
                }
            }
        }
    }
    for (var x=0; x<i; x++){
        var r = "1";
        var s = genNum() + genNum();
        if (s < 50){
            r += s;
        }else{
            r = s;
        }
        name += str[r];
    }
    return name;
}

function initCustomers(length){
    var columns = [
        "customer_name",
        "customer_level",
        "account_num",
        "saler_name",
        "service_stop_days_left"
        // "last_visit"
    ];
    var customers = [];
    for (var i=0; i<length; i++){
        var customer = {};
        customer["customer_id"] = genNum() + genNum() + genNum() + genNum();
        customer["customer_name"] = genName();
        customer["customer_level"] = ["正式", "重点", "开发"][("1" + genNum()) % 3];
        customer["account_num"] = "1" + genNum();
        customer["saler_name"] = genName(3);
        var days = genNum() + genNum() + genNum();
        days = parseInt(days);
        customer["service_stop_days_left"] = days;
        var year = "2020";
        var month = "1";
        var day = "01";
        var num = genNum();
        if (num != 0){
            month = "0" + num;
        }
        if (num > 5){
            year = "2019";
        }
        var num = genNum();
        if (num < 3){
            day = "0" + genNum();
        }else if(num < 6){
            day = "1" + genNum();
        }else{
            day = "2" + genNum();
        }
        customer["last_visit"] = year + "-" + month + "-" + day;
        customers.push(customer);
    }
    return customers;
}

function initOpportunities(length){
    var columns = [
        "opportunity_name",
        "customer_name",
        "opportunity_money",
        "win_rate",
        "quzong_ok",
        // "last_visit",
        "saler_name"
    ];
    var arr = [];
    for (var i=0; i<length; i++){
        var item = {};
        item["opportunity_id"] = genNum() + genNum() + genNum() + genNum();
        item["opportunity_name"] = genName();
        item["customer_name"] = genName();
        item["opportunity_money"] = parseInt(genNum() + genNum() + genNum() + genNum() + genNum() + genNum());
        item["win_rate"] = parseInt(genNum() + genNum()).toString() + "%";

        var year = "2020";
        var month = "1";
        var day = "01";
        var num = genNum();
        if (num != 0){
            month = "0" + num;
        }
        var num = genNum();
        if (num < 3){
            day = "0" + genNum();
        }else if(num < 6){
            day = "1" + genNum();
        }else{
            day = "2" + genNum();
        }
        item["quzong_ok"] = year + "-" + month + "-" + day;

        var year = "2020";
        var month = "1";
        var day = "01";
        var num = genNum();
        if (num != 0){
            month = "0" + num;
        }
        if (num > 5){
            year = "2019";
        }
        var num = genNum();
        if (num < 3){
            day = "0" + genNum();
        }else if(num < 6){
            day = "1" + genNum();
        }else{
            day = "2" + genNum();
        }
        // item["last_visit"] = year + "-" + month + "-" + day;
        item["saler_name"] = genName(3);
        arr.push(item);
    }
    return arr;
}
