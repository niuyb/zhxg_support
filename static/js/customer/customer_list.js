// created by TomTsong 20200225

document.write("<script language=javascript src='/static/js/common.js'></script>");

/*******************************************************************
*
*备注：本js文件中所有department都是行业的意思，改起来会比较麻烦，比较浪费时间，所以不改了
*    
********************************************************************/

/**
 * common.js中定义了CommonLocation类，
 * 类中实现了通用的获取省、市、县的方法，
 * 调用时，只需要实例化CommonLocation
 */
commonLocation = new CommonLocation();

//当前表格中的数据
var tableData = [];
//当前选中的项
var selectedData = [];
//当前筛选条件
var currentQuery = "";

// 渲染department-1
function renderDepartment1(){
    var Id = "department-1";
    var data = JSON.parse($("#department-data-1").text());
    renderSelect(Id, data);
}

function completeOptions(options){
    options.unshift(["", "--------"]);
    options.push([0, "未知"]);
    return options;
}

function renderStates(){
    let Id = "location-select-1";
    let data = commonLocation.getStates();
    data = completeOptions(data);
    renderSelect(Id, data);
}

// option发生变化时，联动下一级行业
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
    for (var i=index+1;i<3;i++){
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
    for (var i=2;i<3;i++){
        $("#department-" + i).empty();
        $("#id_department-" + i).css("display", "none");
    }
    commonSelectReset("location")
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
//二维码弹窗
//弹窗显示
function openQrcode(id){
    $('#qrcode').html('')
    //二维码渲染
    var qrcode = new QRCode(document.getElementById("qrcode"), {
        width : 200,
        height : 200
    });
    let api = `/customer/get_uuid/api?account_id=${id}`;
    $.get(api, function(data, status){
        if(data.code == 200 && data.data){
            let str = `http://${window.location.host}/questionaire/index.html?id=1${data.data}`;
            qrcode.makeCode(str);
            $('#qrcodeInput').val(str)
            //打开弹窗
            $('#qrcodeModal').modal('show')
        }else{
            alert('服务器发生错误！')
        }
    });
}
function enterSyn(){
    let id = $('#enterId').val()
    let api = `/customer/get_uuid/api?account_id=${id}`;
    // 弹出层 —— 加载中特效
    var index = parent.layer.load(0, {shade: false});
    $.get(api, function(data, status){
        if(data.code == 200 && data.data){
            let str = `http://${window.location.host}/questionaire/index.html?id=1${data.data}`;
            // 关闭弹出层
            parent.layer.close(index);
            window.open(str)
        }else{
            // 关闭弹出层
            parent.layer.close(index);
            alert('服务器发生错误！')
        }
    });
}
//syn同步弹窗
//弹窗显示

//时间获取
function getTime(){
    const date = new Date(),
    h = date.getHours(),
    m = date.getMinutes();
    let hLast,hNext;
    if(m > 29){
        hLast = h
        hNext = h == 23 ? 0 : h + 1
    }else{
        hLast = h == 0 ? 23 : h - 1 
        hNext = h
    };
    $('#synList').html(`注：上次客户数据自动同步时间为${hLast}点30分，下一次自动同步时间为${hNext}点30分。如果需查看最新客户，请手动同步客户。`)

}
function openSyn(){
    //搜索栏清空
    $('#synSearch').val('');
    //时间获取
    getTime();
    //打开弹窗
    $('#synModal').modal('show')
}
// 回车搜索触发
$('#synSearch').keyup(function(event){
    if(event.keyCode == 13 || event.keyCode == 108){
        synSearchF();
        event.preventDefault();
    }
})
// 搜索同步信息
function synSearchF(){
    let keyWords = $('#synSearch').val();
    if(keyWords === ''){
        getTime();
        alert('关键字不能为空');
        return
    }
    let api = `/customer/get_finalaccount/api?key=${keyWords}`;
    $('#synList').html(`加载中...`)
    $.get(api, function(data, status){
        if(data.code == 200 && data.data){
            $('#synList').html('')
            for(let i = 0; i<data.data.length; i++){
                let f = i == 0 ? "checked='checked'" : "";
                let cfc = i%2 == 0 ? "background:#cfc" : ""; 
                let app =   `<div style="display:flex;align-items:center;margin:4px 0;${cfc}">
                                <input type="radio" name="synRadio" style="margin:0 8px" ${f} value="${data.data[i].id}" attr="${data.data[i].account_name}" status="${data.data[i].status}">
                                <div style="font-size:16px">${data.data[i].account_name}</div>`
                if(data.data[i].status){
                    app = app + '<i style="margin-left:10px">此客户已存在客户列表中</i></div>'
                }else{
                    app = app + '</div>'
                }
                $('#synList').append(app)
            }
        }else if(data.code == 201){
            $('#synList').html(`该关键字没有匹配的客户...`)
        }else{
            $('#synList').html(`搜索失败...`)
        }
    });
}
// 开始同步 
function synStart(){
    let dom = $('input[name=synRadio]:checked')
    let name = dom.attr('attr')
    console.log(name)
    let id = dom.val();
    let status = dom.attr('status');
    let api = `/customer/sync_account_data/api?id=${id}&status=${status}`
    $('#synList').html(`同步中...`)
    $.get(api, function(data, status){
        if(data.code == 200){
            alert('同步成功');
            $('#synModal').modal('hide');
            $('#account_name').val(name)
            reloadTable();
        }else{
            alert('同步失败')
            synSearchF()
        }
    });
}
// 用连线补空
function fillLineToBlank(cellvalue, options, rowObject){
    if (cellvalue === "" || cellvalue === null){
        return "--------";
    }else{
        return cellvalue;
    }
}

function hasBinded(){
    var taskId = "";
    try{
        taskId = $("#theTaskId").text();
    }catch(e){
        console.log(e);
    }

    if (!taskId){
        console.log("taskId is null.");
        return;
    }

    var tip = document.getElementById("tip");
        
    var api = "/work_platform/wechat/result?task_id=" + taskId;

    $.get(api, function(data, status){
        if (data.code === 1 || data.code === 0 ){
            clearInterval(inter);
            $("#waiting").remove();
            tip.innerHTML = "<span style='color: red;'>微信群成功绑定</span>";
        }

        if (data.code === 1){
            setTimeout(function(){
                $("#closeBtn").click();
            }, 1500);            
        }
        return;

    });

}

function uploadQrCode(that){
    var file = document.getElementById("qrCode");
    var tip = document.getElementById("tip");
    if (!(file.files) || !(file.files[0])){
        tip.innerHTML = "<span style='color: red;'>请添加微信群二维码</span>";
        return false;
    }

    var form = document.getElementById("uploadForm");
    var formData = new FormData(form);

    $("uploadModal").css("background-color", "gray");

    var div = '<div id="waiting" style="position: fixed; top: 0; width: 100vw; left: 0; height: 100vh; overflow: hidden; background: transparent; z-index: 9999;">' +
            '<div class="box" style="color: red; position: absolute; top: 50%; left: 50%;"><h2>正在进行绑定：<span class="clock">20</span>秒</h2></div>' +
            '<div id="theTaskId" style="display: none;"></div>' +
            '<script>' +
                'var t = 20;' +
                'var time = document.getElementsByClassName("clock")[0];' +     
                'function fun() {' +
                    'if ((t -2) % 3 === 2){' +
                        'hasBinded();' +
                    '}' +
                    't--;' + 
                    'time.innerHTML = t;' +
                    'if(t <= 0) {' +
                        'clearInterval(inter);' +
                        'tip.innerHTML = "<span style=\'color: red;\'>请求超时！</span>";' +
                        '$("uploadModal").css("background-color", "");' +
                        '$("#waiting").remove();' +
                    '}' +
                '}' + 
                'var inter = setInterval("fun()", 1000);' +
            '</script>' +
            '</div>';

    $('body').append(div);

    $.ajax({
        type : 'post',
        url : "/work_platform/wechat",
        dataType : 'json',
        data : formData,
        contentType: false,
        processData: false,
        success : function(res){

            tip.innerHTML = "<span style='color: red;'>" + res.error + "</span>";
            if (res.code === 1){
                var taskId = res.data.taskId;
                $("#theTaskId").text(taskId + "");
            }else{                
                try{
                    clearInterval(inter);
                }catch(e){
                    console.log(e)
                }

                $("uploadModal").css("background-color", "");

                $("#waiting").remove();
            }                
        },
        error:function(XMLHttpRequest, textStatus){               
            try{
                clearInterval(inter);
            }catch(e){
                console.log(e)
            }

            $("uploadModal").css("background-color", "");
            $("#waiting").remove();
            tip.innerHTML = "<span style='color: red;'>服务器发生错误！</span>";
        }
    });

    return false;
}

function renderUploadModal(title, customerId, customerName, wechatGroupName, qrCodeStr){

     function clearImages(id){
        var file = document.getElementById("qrCode");
        var code = document.getElementById("showQrCode");
        file.value = "";
        file.files = null;
        code.innerHTML = '<img class="img-bg" src="/static/img/webuploader.png" />';
     }

    var cid = $("#customerId");

    $("#myModalLabel").text(title);
    $("#customerId").val(customerId);
    $("#customerName").val(customerName);
    document.getElementById("tip").innerHTML = "";

    if (wechatGroupName){
        //
        //某些操作，例如控制修改微信群的按钮
        //

    }else{
        wechatGroupName = customerName + "-微信群";
    }

    $("#wechatGroupName").val(wechatGroupName);

    if (cid !== customerId){
        clearImages();
    }    

    // $("#submitBtn").attr("disabled", "disabled");
    // $("#submitBtn").prop("disabled", "disabled");
}



// 操作列：绑定微信群，上传微信群二维码、创建账号
function toBindWechatGroup(cellvalue, options, rowObject){
    var customerId = rowObject.id;
    var customerName = rowObject.customer_name;
    var wechatGroupName = rowObject.wechat_group_name || "";
    let canCreate = rowObject.has_opp == 1 ? true : false
    let canOpenQrcode = rowObject.has_syc == 1 ? false : true 

    var wechatGroupStatus = rowObject.wechat_group_status || 0;
    var wechatGroupCtime = rowObject.wechat_group_ctime || "";
    wechatGroupCtime = wechatGroupCtime.replace(/\-/g, '/');

    var qrCodeStr = rowObject.qr_code_str || "";
    // var title = "";
    var title2 = "创建账号";
    var title3 = "查看调研表";
    var title4 = "发送调研表"
    // if (wechatGroupStatus === 1 || wechatGroupStatus === 3){
    //     title = "修改微信群";
    // }else{
    //     title = "绑定微信群";
    // }
//    var html4 = "<a style='margin-right: 5px;' a href='#'" +
//             " class = 'removeTitle' "+
//             " data-toggle='modal'  data-target='#uploadModal'" +
//             " onclick='renderUploadModal(\"" +
//             title +
//             "\", \"" +
//             customerId +
//             "\", \"" +
//             customerName +
//             "\", \"" +
//             wechatGroupName +
//             "\", \"" +
//             qrCodeStr +
//             "\")'>" + title + "</a>";
    let html =  canCreate?
                `<a style='margin-right:5px;'onclick='get_opp_infos("${customerId}")' the-id='targetmodel' href='#'>${title2}</a>`:
                `<span style='margin-right:5px;color:#aaa' the-id='targetmodel' title='请先创建商机'>${title2}</span>`
    var html2 = "<a style='margin-right: 5px;' onclick='checkSurvey( \"" +
            customerId +
            "\", \"" +
            "\")' the-id='targetmodel' a href='#'" +
            " class = 'removeTitle' "+
            " >" + title3 + "</a>";
    let html3 = canOpenQrcode?
                `<a style='margin-right:5px;'onclick='openQrcode("${customerId}")' the-id='targetmodel' href='#'>${title4}</span>`:
                `<span style='margin-right:5px;color:#aaa' the-id='targetmodel'>${title4}</span>`
;
    return html + html2 + html3
}
//查看调研表
function checkSurvey(id){
    let api = ` /customer/get_uuid/api?account_id=${id}`;
    $.get(api, function(data, status){
        if(data.code == 200 && data.data){
            let target = `http://${window.location.host}/questionaire/index.html?id=0${data.data}`
            console.log(target)
            window.open(target)
        }else{
            alert('服务器发生错误！')
        }
    });
}
//复制调研表
function copyUrl(){
    $('#qrcodeInput').select();
    document.execCommand("copy");
    alert('复制成功！')
}

// 创建账号入口验证、返回数据
function get_opp_infos(customerId){
    // 隐藏默认隐藏的项，并将输入框置空
    $('#be_hidden').hide();
    $('#agent_div').hide();
    $('[the-id=agentResult]').hide();
    $('#region_lock_word_id').hide();
    $('#agent_name').val('');
    $('#region_lock_word').val('');
    // 将更多按钮显示
    $('#more_btn').show();
    // 移除生成账号的不可点击的属性
    $('#addAccountBtn').removeAttr('disabled');

    // 首先，同步CRM信息
    // var sync_url = "/customer/sync_crm/api?account_id=" + customerId;

    // 弹出层 —— 加载中特效
    var index = parent.layer.load(0, {shade: false});

    // $.get(sync_url, function(data){
        // 关闭弹出层
        parent.layer.close(index);
        // if (data.code != 1){
        //     alert('同步CRM数据失败,请联系管理员！')
        //     return false;
        // }else {
            // 同步CRM信息成功时，检查客户是否存在商机
            var api = "/customer/list_opp?account_id=" + customerId;
            $.get(api, function(data){
                if (data.status != 1) {
                    alert('该客户名下还没有商机，请先在Cloudcc中创建商机！')
                    return false;
                }else {
                    $('#uploadModal2').modal('show');

                    // 当客户存在商机且同步CRM信息成功时，拿客户建账号需要的信息
                    var url = "/customer/get_account/api?product_id=yqms&account_id=" + customerId;
                    // console.log(url);
                    $.get(url, function(data){
                        if (data.status != 1){
                            alert('获取创建账号基础数据失败,请联系管理员！')
                            return false;
                        }else {
                            // 设置客户名称、客户id、登录名、密码、绑定手机、关键词数、代理商默认值
                            $('#accountName').val(data.acc_data.account_name);
                            $('#accountId').val(data.acc_data.account_id);
                            $('#loginName').val(data.acc_data.login_name);
                            $('#password').val(data.acc_data.password);
                            $('#phone').val(data.acc_data.phone);
                            $('#word_num').val(data.acc_data.word_num);
                            $('#agent_name').val(data.acc_data.agent_name);

                            if (data.acc_data.update_timestamp == ''){
                                $('#addAccountTip').html(`注：距离上次客户数据自动同步时间超过一天，修改信息后请进行同步。`)
                            }else{
                                $('#addAccountTip').html(`注：上次客户数据自动同步时间为${data.acc_data.update_timestamp}，修改信息后请进行同步。`)
                            }


                            // 设置一级行业、二级行业默认值
                            var industry1_name = data.acc_data.industry1;
                            if(industry1_name == null){
                                industry1_name = '';
                            }
                            industry1 = '<option selected value='+data.acc_data.industry1_id+'>'+industry1_name+'</option>';
                            $('#industry1').html(industry1);

                            var industry2_name = data.acc_data.industry2;
                            if(industry2_name == null){
                                industry2_name = '';
                            }
                            industry2 = '<option selected value='+data.acc_data.industry2_id+'>'+industry2_name+'</option>';
                            $('#industry2').html(industry2);

                            // 设置所属地域、客户地域默认值
                            var state_name = data.acc_data.state;
                            if(state_name == null){
                                state_name = '';
                            }
                            var city_name = data.acc_data.city;
                            if(city_name == null){
                                city_name = '';
                            }
                            var district_name = data.acc_data.district;
                            if(district_name == null){
                                district_name = '';
                            }
                            var state_id = data.acc_data.state_id;
                            if(state_id == null){
                                state_id = '';
                            }
                            var city_id = data.acc_data.city_id;
                            if(city_id == null){
                                city_id = '';
                            }
                            let district_id = data.acc_data.district_id?data.acc_data.district_id:''
                            state_area_belongs = '<option selected value='+state_id+'>'+state_name+'</option>';
                            $('#state_area_belongs').html(state_area_belongs);
                            city_area_belongs = '<option selected value='+city_id+'>'+city_name+'</option>';
                            $('#city_area_belongs').html(city_area_belongs);
                            district_area_belongs = '<option selected value='+district_id+'>'+district_name+'</option>';
                            $('#district_area_belongs').html(district_area_belongs);
                            state_account_area = '<option selected value='+state_id+'>'+state_name+'</option>';
                            $('#state_account_area').html(state_account_area);
                            city_account_area = '<option selected value='+city_id+'>'+city_name+'</option>';
                            $('#city_account_area').html(city_account_area);
                            // district_account_area = '<option selected value='+district_id+'>'+district_name+'</option>';
                            district_account_area = `<option selected value=${district_id}>${district_name}</option>`;
                            $('#district_account_area').html(district_account_area);

                            // 设置客户类型默认值
                            account_type = '<option selected value='+data.acc_data.account_type_id+'>'+data.acc_data.account_type+'</option>';
                            $('#account_type').html(account_type);
                            // 设置版本选择默认值
                            version = '<option selected value='+data.acc_data.version_id+'>'+data.acc_data.version+'</option>';
                            $('#version').html(version);

                            // 设置商机名称下拉框
                            opp_num = data.opp_data.length
                            // console.log(opp_num);
                            var opp_name = '';
                            for(var num = 0; num < opp_num; num++){
                                // console.log(data.opp_data[num].opp_name);
                                opp_name += '<option value='+data.opp_data[num].opp_id+'>'+data.opp_data[num].opp_name+'</option>';
                                $('#opp_name').html(opp_name);
                            }
                            $('#opp_owner').val(data.opp_data[0].opp_owner);

                            // 设置账号类型下拉框
                            zh_type_num = data.acc_data.zh_type.length
                            var zh_type = '';
                            for(var num = 0; num < zh_type_num; num++){
                                zh_type += '<option value='+data.acc_data.zh_type[num].zh_type_id+'>'+data.acc_data.zh_type[num].zh_type+'</option>';
                                $('#zh_type').html(zh_type);
                            }

                            // 设置主题版本默认值
                            if($('#zh_type').val() == '4'){
                                var templateType_id = '4';
                                var templateType_name = '代理商版';
                            }else {
                                var templateType_id = '0';
                                var templateType_name = '蓝白版';
                            }
                            templateType = '<option selected value='+templateType_id+'>'+templateType_name+'</option>';
                            $('#templateType').html(templateType);

                            // 设置check_phone提示信息
                            var check_phone = data.acc_data.check_phone;
                            if (check_phone != null){
                                var check_phone_info = check_phone;
                                $('#check_phone_info').val(check_phone_info);
                            }else {
                                $('#check_phone_info').val('');
                            }
                        }
                    });
                }
            });
        // }
    // });
}

// 初始化form表单
function initForm(){
    var formData = JSON.parse($("#form-dict").text());
    var industry1 = formData["industry1"];
    var industry2 = formData["industry2"];
    var state = formData["state"];
    var city = formData["city"];
    var district = formData["district"];
    var coverage = formData["coverage"];
    var status = formData["status"];
    if (industry1 != null && industry1 != undefined){
        $("#department-1 option[value='" + industry1 + "']").prop("selected", "selected");
        onDepartmentChange1();
        if (industry2 != null && industry2 != undefined){
            $("#department-2 option[value='" + industry2 + "']").prop("selected", "selected");
        }
    }
    
    if (state != null && state != undefined){
        $("#location-select-1 option[value='" + state + "']").prop("selected", "selected");
        onSelectChange("location", 1, commonLocation.getCities);
    }
    
    if (city != null && city != undefined){
        $("#location-select-2 option[value='" + city + "']").prop("selected", "selected");
        onSelectChange("location", 2, commonLocation.getDistricts);
    }
    
    if (district != null && district != undefined){
        $("#location-select-3 option[value='" + district + "']").prop("selected", "selected")
    }
}

function GetJqGridRowIndx($id){
    var indexes = [];
    $($id + " tr.success").each(function(a, b){
        indexes.push(b.id);
    });
    return indexes;
}

// 配置并渲染表格
function configureTable(data){       
    for (var i in data.col_model){
        if (data.col_model[i].name == "state"){
            data.col_model[i].formatter = fillLineToBlank;
        }
        if (data.col_model[i].name == "city"){
            data.col_model[i].formatter = fillLineToBlank;
        }
        if (data.col_model[i].name == "district"){
            data.col_model[i].formatter = fillLineToBlank;
        }
        if (data.col_model[i].name == "industry1_name"){
            data.col_model[i].formatter = fillLineToBlank;
        }
        if (data.col_model[i].name == "industry2_name"){
            data.col_model[i].formatter = fillLineToBlank;
        }
        if (data.col_model[i].name == "operations"){
            var formatter = operationsFunc;
            if (data.access.push_wechat_message){
                formatter = operationsFunc2;
            }
            data.col_model[i].formatter = formatter;
        }
    }

    // 如果有导出数据的权限，便可以看到导出按钮
    var caption = "";
    // if (data.access.export_customer_list){
    //     caption += "<span style='padding-right: 15px;'><span style='height: 29px; cursor: pointer;' class='glyphicon glyphicon-new-window' onclick='exportCsv()' title='导出为csv'>"
    //             + "<span class='bold' style='margin-left: 5px; cursor: pointer;'>导出</span></span></span>"
    // }

    if (data.access.push_wechat_message){
        caption += "<span style='padding-right: 15px;'><span style='height: 29px; cursor: pointer;' class='glyphicon glyphicon-leaf' title='批量推送'>"
                + "<span class='bold' style='margin-left: 5px; cursor: pointer;'><a href='#' data-toggle='modal' data-target='#messageModal'" 
                + " onclick='pushWechatMessageToSome()'>批量推送</a></span></span></span>"
    }

    if (data.access.push_wechat_message){
        caption += "<span style='padding-right: 15px;'><span style='height: 29px; cursor: pointer;' class='glyphicon glyphicon-send'' title='全部推送'>"
                + "<span class='bold' style='margin-left: 5px; cursor: pointer;'><a href='#' data-toggle='modal' data-target='#messageModal'" 
                + " onclick='pushWechatMessageToAll()'>全部推送</span></span></span>"
    }

    var SelectRowIndx;

    // Configuration for jqGrid Example 1
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
        // 将导出按钮安放到表格头部。这里用了投机取巧的方法，将title-tool-bar的caption写成html，html里面包含onclick事件，以此来达到将导出按钮部署到表格头部。
        'caption': caption,
        hidegrid: false,
        loadComplete: function(gridObject){$("#table_list_1 .ui-jqgrid-title").css("padding-top", "0");
        //去掉父级title
        $('a.removeTitle').parent().attr('title','')
        },

        multiselect: true,
        onSelectRow: function(){
            selectedData = [];
            SelectRowIndx = GetJqGridRowIndx("#" + this.id);
            if (SelectRowIndx){
                for (var item of tableData){
                    for (var i of SelectRowIndx){
                        if (String(item.id) === String(i)){
                            selectedData.push(item);
                        }
                    }
                }
            }
        },
        gridComplete: function(){
            $("#" + this.id).jqGrid('setSelection', SelectRowIndx);
        }
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
function reloadTable(url,fisrt = 0){
    if (!url){
        var query = $("#customer-list-filter-form").serialize();
        currentQuery = query;

        url = $("#customer-list-api").text().trim() +"?" + query;
    }
    if (fisrt == 1){
        url = url + `&is_first=1`
    }
    // 核验表单中数据是否合法
    if (!checkForm()){
        return false;
    }
    $("#submitBtn").attr("disabled", "disabled");
    $("#submitBtn").text("加载中");

    // 弹出层 —— 加载中特效
    var index = parent.layer.load();

    $.get(url, function(data, status){

        tableData = [];
        selectedData = [];

        if (data.status == null || data.status == undefined){
            // window.location.reload();
            return;
        }

        if (data.status < 1){
            alert(data.message);
        }

        tableData = data.items;
        
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
    // $('#data_5 .input-daterange').datepicker({
    //     keyboardNavigation: false,
    //     forceParse: false,
    //     autoclose: true
    // });
    // $('#data_6 .input-daterange').datepicker({
    //     keyboardNavigation: false,
    //     forceParse: false,
    //     autoclose: true
    // });
    renderDepartment1();
    renderStates();
    initForm();
    renderTable();
    reloadTable(null,1);
});

// 点击搜索按钮，用ajax发起请求，并将数据渲染到表格中
$("#submitBtn").click(function(){
    // renderTable();
    reloadTable();
});

function operationsFunc(cellvalue, options, rowObject){
    var html = "";
    html += toBindWechatGroup(cellvalue, options, rowObject);
    return html;
}

function operationsFunc2(cellvalue, options, rowObject){
    var html = operationsFunc(cellvalue, options, rowObject);
    html += toPushWechatMessage(cellvalue, options, rowObject);
    return html;
}

function toPushWechatMessage(cellvalue, options, rowObject){
    var title = "微信群推送";
    var customerIds = rowObject.id;
    var customerNames = rowObject.customer_name;

    var wechatGroupStatus = rowObject.wechat_group_status || 0;
    var wechatGroupCtime = rowObject.wechat_group_ctime || "";
    wechatGroupCtime = wechatGroupCtime.replace(/\-/g, '/');

    if (wechatGroupStatus === 1 && wechatGroupCtime && new Date() - (new Date(wechatGroupCtime)) > 25 * 60 * 60 * 1000){
        return _pushWechatMessage(title, customerIds, customerNames);
    }

    return "";    
}

function _pushWechatMessage(title, customerIds, customerNames){

    if (customerIds && typeof customerIds !== "object"){
        customerIds = [customerIds];
    }

    if (!customerIds){
        customerIds = "";
    }

    if (typeof customerIds === "object"){
        customerIds = customerIds.join(",");
    }

    if (typeof customerNames === "object"){
        customerNames = customerNames.join(",")
    }
    
    customerNames = customerNames.substr(0, 100) + "...";

    var typ = 1; // 1, 给1个微信群推送消息 2，给多个微信群推送消息 3，给当前筛选条件下的所有微信群推送消息
    var html = "<a href='#'" + 
            " data-toggle='modal'  data-target='#messageModal'" + 
            " onclick='renderMessageModal(\"" +
            title +
            "\", \"" +
            customerIds +
            "\", \"" +
            customerNames +
            "\", \"" +
            typ +
            "\")'>" + title + "</a>";
            
    return html
}

function clearMessageForm(){
    $("#messageTitle").val("");
    $("#messageTitle").text("");
    $("#messageContent").val("");
    $("#messageContent").text("");
    $("#messageUrl").val("");
    $("#messageUrl").text("");
}

function setMessageForm(title, content, url){
    $("#messageTitle").val(title);
    $("#messageContent").val(content);
    $("#messageUrl").val(url);
}

function pushWechatMessage(that){   

    var form = document.getElementById("messageForm");
    var message = $("#messageContent").val();
    if (!message){
        document.getElementById("tip").innerHTML = "消息内容不能为空";
        return false;
    }
    var formData = new FormData(form);
    
    currentQuery = currentQuery.replace(/wechat_group=\d*/g, "wechat_group=3");
    
    $.ajax({
        type : 'post',
        url : "/work_platform/wechat/group/message/push?" + currentQuery,
        dataType : 'json',
        data : formData,
        contentType: false,
        processData: false,
        success : function(res){

            tip.innerHTML = "<span style='color: red;'>" + res.error + "</span>";
            if (res.code === 1){
                document.getElementById("tip").innerHTML = "推送任务已成功生成。"
                setTimeout(function(){
                    $("#messageModal").modal('hide');
                }, 2000);
                
                clearMessageForm();

            }else{ 

                $("messageModal").css("background-color", "");
                document.getElementById("tip").innerHTML = res.error;
            }                
        },
        error:function(XMLHttpRequest, textStatus){  

            $("messageModal").css("background-color", "");

            tip.innerHTML = "<span style='color: red;'>服务器发生错误！</span>";
        }
    });

    return false;
}

function pushWechatMessageToSome(){
    var title = "微信群批量推送";
    var customerIds = GetJqGridRowIndx("#table_list_1");
    var err = "";
    if (customerIds.length === 0){
        err = "您未选中任何客户";
    }

    var selectedData = [];
    for (var item of tableData){
        for (var i of customerIds){
            if (item.id == i){
                selectedData.push(item);
            }
        }
    }
    var customerNames = [];
    for (var item of selectedData){
        //customerIds.push(item.id);
        customerNames.push(item.customer_name);
    }
    var typ = 2;
    renderMessageModal(title, customerIds, customerNames, typ, err);
}

function pushWechatMessageToAll(){
    var title = "微信群全部推送";
    var customerIds = null;
    var customerNames = "全部";
    var typ = 3;
    renderMessageModal(title, customerIds, customerNames, typ);
}

function renderMessageModal(title, customerIds, customerNames, typ, err){     

    if (!customerIds || customerIds.length === 0){
        customerIds = "";
    }
    
    if (typeof customerIds === "object"){
        customerIds = customerIds.join(",")
    }

    if (!customerNames || customerNames.length === 0){
        customerNames = "";
    }

    if (typeof customerNames === "object"){
        customerNames = customerNames.join(",  ")
    }

    $("#messageSubmitBtn").attr("disabled", "");
    $("#messageSubmitBtn").prop("disabled", "");

    $("#messageModalLabel").text(title);
    $("#customerIds").val(customerIds);
    $("#customerNames").val(customerNames);
    $("#pushType").val(typ);

    if (!err){
        err = "";
    }

    if (err){ 
        $("#messageSubmitBtn").attr("disabled", "disabled");
        $("#messageSubmitBtn").prop("disabled", "disabled");
    }
    document.getElementById("tip").innerHTML = err;
    
}


// 创建账号弹框-代理商搜索按钮
$("#agentSearch").click(function(){
    var search_content = $('#agent_name').val();
    var url = '/customer/agent/api?agent_name=' + search_content;
    $.get(url,function(data){
        if (data) {
            var str='';
            for (var i = 0; i < data.data.length; i++) {
                str+='<li style="line-height:30px;" data-id="'+data.data[i].agent_id+'">'+data.data[i].agent_name+'</li>';
            }
            $('[the-id=agentResult]').html(str).show();
        }

    })
});

// 快速建账号-选择代理商搜索结果点击事件
$('[the-id="agentResult"]').on('click','li',function(){
    var ka_name = $(this).text();
    var ka_id = $(this).attr('data-id');
    if (ka_name && ka_name != '暂无数据') {
        console.log(ka_name)
        console.log(ka_id)
        $('#agent_name').val(ka_name).attr('data-id',ka_id);
        // $('#agent_name').attr('data-id',ka_id);
        $(this).parent().hide().html('');
    }
});

// 创建账号弹框-CRM修改按钮
$("#crmEditBtn").click(function(){
    var customerId = $('#accountId').val();
    var url = "/customer/get_crm_Id/api?account_id=" + customerId;
    $.get(url, function (data) {
            // var url = 'https://k8mm3cmt3235c7ed72cede6e.cloudcc.com/query.action?vr=inno&showOverview=true&obj=001';
            if (data["code"] === 200){
                var url = 'https://k8mm2bmtada55ce305401dc1.cloudcc.com/queryframe.action?vr=inno&id=' + data['data']['crm_id'] +'&m=query'
            }
            else {
                var url = 'https://k8mm2bmtada55ce305401dc1.cloudcc.com/queryframe.action?vr=inno&id=&m=query'
            }
            window.open(url)
        }
    )
    // var url = 'https://k8mm3cmt3235c7ed72cede6e.cloudcc.com/query.action?vr=inno&showOverview=true&obj=001';
    // window.open(url);
});

// 创建账号弹框-更多按钮
$("#moreBtn").click(function(){
    // 展示默认隐藏的项
    $('#be_hidden').show();
    // 将更多按钮隐藏
    $('#more_btn').hide();
});

// 创建账号弹框-代理商是否显示、主题版本是否更换为代理商版、锁定地域词是否显示
$("#zh_type").on('change', function(){
    if($('#zh_type').val() == '4'){
        $('#agent_div').show();
        templateType = '<option selected value='+'4'+'>'+'代理商版'+'</option>';
        $('#templateType').html(templateType);

        if($('#state_account_area').val() == 'null'){
            $('#region_lock_word_id').show();
        }else {

            $('#region_lock_word_id').hide();
            $('#region_lock_word').val('');
        }
    }else {
        $('#agent_div').hide();
        $('#agent_name').val('');
        $('#region_lock_word_id').hide();
        $('#region_lock_word').val('');
    }
});

// 创建账号弹框-选择商机后修改商机负责人
$("#opp_name").on('change', function(){
    // 当商机更改时，重新拿该客户所有的商机信息
    var customerId = $('#accountId').val();
    var url = "/customer/opp_owner/api?account_id=" + customerId;
    $.get(url, function(data){
        var opp_id = $('#opp_name').val();
        $('#opp_owner').val(data.data[opp_id]);
    });
});

// 快速建帐号-生成账号按钮(直接调PHP接口)
// $('#addAccountBtn').click(function(){
//     var url = "/customer/get_environment/api";
//     $.get(url, function(data){
//         var envi = data.data;
//         if(envi == 'product'){
//             var domain_support = 'support';
//         }else {
//             var domain_support = 'support-beta';
//         }
//         var add_account_url = 'http://'+domain_support+'.istarshine.com/Api/doAddAccount';
//         console.log(add_account_url)
//
//     // var add_account_url = "/customer/add_account_php/api";
//
//         var crmName = $('#accountName').val();
//         var addCrmUid = $('#accountId').val();
//         var opportunityName = $('#opp_name').text();
//         var opportunityId = $('#opp_name').val();
//         var logName = $('#loginName').val();
//         var pasd = $('#password').val();
//         var classify = $('#zh_type').val();
//         var agent_id = $('#agent_name').attr("data_id");
//         var classpid = $('#industry1').val();
//         var classid = $('#industry2').val();
//         var province_id = $('#state_account_area').val();
//         var city_id = $('#city_account_area').val();
//         var county_id = $('#district_account_area').val();
//         var ssdiyu = $('#state_area_belongs').val();
//         var ss_city = $('#city_area_belongs').val();
//         var ss_county = $('#district_area_belongs').val();
//         var xiaoshou = $('#maintainer').val();
//         var templateType = $('#templateType').val();
//         var leixing = $('#account_type').val();
//         var banben = $('#version').val();
//         var keywordnum = $('#word_num').val();
//         var region_lock_word = $('#region_lock_word').val();
//         var bindphone = $('#phone').val();
//         var check_phone_info = $('#check_phone_info').val();
//
//         if (crmName == '') {
//             alert('客户名称不能为空');
//             return false;
//         } else if(addCrmUid == '') {
//             alert('客户ID获取失败，请刷新页面后重试');
//             return false;
//         } else if(opportunityName == '') {
//             alert('请选择商机名称');
//             return false;
//         } else if(opportunityId == '') {
//             alert('商机ID获取失败，请刷新页面后重试');
//             return false;
//         } else if(logName == '') {
//             alert('账号名称不能为空');
//             return false;
//         } else if(pasd == '') {
//             alert('密码不能为空');
//             $('[name=addPasd]').focus();
//             return false;
//         } else if(classify == '') {
//             alert('账号类型不能为空')
//             return false;
//         } else if(classpid == '') {
//             alert('请选择一级行业')
//             return false;
//         } else if(classid == '') {
//             alert('请选择二级行业')
//             return false;
//         } else if(ssdiyu == '') {
//             alert('请选择所属地域')
//             return false;
//         }else if(xiaoshou == '') {
//             alert('维护人不能为空')
//             return false;
//         } else if (keywordnum == 0 || keywordnum == null || keywordnum == '') {
//             alert('关键词不能为空')
//             return false;
//         } else if (classify == '4' && province_id == '' && region_lock_word == '') {
//             alert('请填写锁定地域词');
//             return false;
//         } else if (classify == '4' && leixing == '4' && company_lock_word == '') {
//             alert('请填写锁定关键词');
//             return false;
//         } else if (check_phone_info != ''){
//             alert(check_phone_info);
//             return false;
//         }else {
//             var re = /^(?=.*[a-zA-Z])(?=.*\d)(?=.*[#@!~%^*$\(\)\-+\|\\\{\}\[\]<>\?\/\_\=])[a-zA-Z\d#@!~%^*$\(\)\-+\|\\\{\}\[\]<>\?\/\_\=]{8,16}$/; //验证特殊符号
//             if (!re.test(pasd)) {
//                 alert('密码为字母+数字+特殊符号组合，8～16位字符！')
//                 $('[name=addPasd]').focus();
//                 return false;
//             }
//             if (pasd.length < 8) {
//                 alert('密码不能少于八位');
//                 $('[name=addPasd]').focus();
//                 return false;
//             }
//             var reg2 = /^[\u4e00-\u9fa5a-z0-9]+$/gi; //验证特殊符号
//             if (!reg2.test(logName)) {
//                 alert('账号名称不能有特殊字符');
//                 $('[name=addLogName]').focus();
//                 return false;
//             }
//             if (classify == 4 && !agent_id) {
//                 alert('请搜索代理商并选择');
//                 $('#addAccount').find('[name=addClassify]').focus();
//                 return false;
//             }
//             $('#addAccountBtn').attr('disabled','disabled');
//             $.ajax({
//                 header: "Access-Control-Allow-Origin: *",
//                 type : "post",
//                 url: add_account_url,
//                 dataType: 'json',
//                 data : {
//                     crmName:crmName,
//                     crmUid:addCrmUid,
//                     opportunityName:opportunityName,
//                     opportunityId:opportunityId,
//                     logName:logName,
//                     pasd:pasd,
//                     classify:classify,
//                     agent_id:agent_id,
//                     classpid:classpid,
//                     classid:classid,
//                     province_id:province_id,
//                     city_id:city_id,
//                     county_id:county_id,
//                     ssdiyu:ssdiyu,
//                     ss_city:ss_city,
//                     ss_county:ss_county,
//                     xiaoshou:xiaoshou,
//                     templateType:templateType,
//                     kusex:leixing,
//                     userLeve:banben,
//                     keywordnum:keywordnum,
//                     region_lock_word:region_lock_word,
//                     bindphone:bindphone
//                 },
//
//                 success:function(res){
//                     if (res.status == 1) {
//                         alert('创建成功');
//                         location.reload();
//                     } else {
//                         $('#addAccountBtn').removeAttr('disabled');
//                         alert(res.msg);
//                     }
//                 }
//             });
//         }
//         return false;
//     });
// });


// 快速建帐号-生成账号按钮(调python接口)
$('#addAccountBtn').click(function(){
    // 弹出层 —— 加载中特效
    // var index = parent.layer.load(3);
    $('#addAccountBtn').hide()
    $('#addAccountBtnLoading').show()
    var add_account_url = "/customer/add_account_php/api";
    var crmName = $('#accountName').val();
    var addCrmUid = $('#accountId').val();
    var opportunityName = $('#opp_name option:selected').text();
    var opportunityId = $('#opp_name option:selected').val();
    var logName = $('#loginName').val();
    var pasd = $('#password').val();
    var classify = $('#zh_type').val();
    var agent_id = $('#agent_name').attr("data_id");
    var classpid = $('#industry1').val();
    var classid = $('#industry2').val();
    var province_id = $('#state_account_area').val();
    var city_id = $('#city_account_area').val();
    var county_id = $('#district_account_area').val();
    var ssdiyu = $('#state_area_belongs').text();
    var ss_city = $('#city_area_belongs').text();
    var ss_county = $('#district_area_belongs').text();
    var xiaoshou = $('#maintainer').val();
    var templateType = $('#templateType').val();
    var leixing = $('#account_type').val();
    var banben = $('#version').val();
    var keywordnum = $('#word_num').val();
    var region_lock_word = $('#region_lock_word').val();
    var bindphone = $('#phone').val();
    var check_phone_info = $('#check_phone_info').val();
    if (classid && classid == 36){
        // 二级行业-高校id(cloudcc为36，老后台为73)
        classid = 73;
    }else if (classid && classid == 7){
        // 二级行业-交通局id(cloudcc为7，老后台为9)
        classid = 9;
    }else if (classid && classid == 17){
        // 二级行业-政府办id(cloudcc为17，老后台为19)
        classid = 19;
    }else if (classid && classid == 6){
        // 二级行业-检察院id(cloudcc为6，老后台为8)
        classid = 8;
    }else if (classid && classid == 4){
        // 二级行业-纪检委id(cloudcc为4，老后台为6)
        classid = 6;
    }else if (classid && classid == 34){
        // 二级行业-市场监督管理局id(cloudcc为34，老后台为66)
        classid = 66;
    }


    if (crmName == '') {
        alert('客户名称不能为空');
        return false;
    } else if(addCrmUid == '') {
        alert('客户ID获取失败，请刷新页面后重试');
        return false;
    } else if(opportunityName == '') {
        alert('请选择商机名称');
        return false;
    } else if(opportunityId == '') {
        alert('商机ID获取失败，请刷新页面后重试');
        return false;
    } else if(logName == '') {
        alert('账号名称不能为空');
        return false;
    } else if(pasd == '') {
        alert('密码不能为空');
        $('[name=addPasd]').focus();
        return false;
    } else if(classify == '') {
        alert('账号类型不能为空')
        return false;
    } else if(classpid == '') {
        alert('请选择一级行业')
        return false;
    } else if(classid == '') {
        alert('请选择二级行业')
        return false;
    } else if(ssdiyu == '') {
        alert('请选择所属地域')
        return false;
    }else if(xiaoshou == '') {
        alert('维护人不能为空')
        return false;
    } else if (keywordnum == 0 || keywordnum == null || keywordnum == '') {
        alert('关键词不能为空')
        return false;
    } else if (classify == '4' && province_id == '' && region_lock_word == '') {
        alert('请填写锁定地域词');
        return false;
    } else if (classify == '4' && leixing == '4' && company_lock_word == '') {
        alert('请填写锁定关键词');
        return false;
    } else if (check_phone_info != ''){
        alert(check_phone_info);
        return false;
    }else {
        var re = /^(?=.*[a-zA-Z])(?=.*\d)(?=.*[#@!~%^*$\(\)\-+\|\\\{\}\[\]<>\?\/\_\=])[a-zA-Z\d#@!~%^*$\(\)\-+\|\\\{\}\[\]<>\?\/\_\=]{8,16}$/; //验证特殊符号
        if (!re.test(pasd)) {
            alert('密码为字母+数字+特殊符号组合，8～16位字符！')
            $('[name=addPasd]').focus();
            return false;
        }
        if (pasd.length < 8) {
            alert('密码不能少于八位');
            $('[name=addPasd]').focus();
            return false;
        }
        var reg2 = /^[\u4e00-\u9fa5a-z0-9]+$/gi; //验证特殊符号
        if (!reg2.test(logName)) {
            alert('账号名称不能有特殊字符');
            $('[name=addLogName]').focus();
            return false;
        }
        if (classify == 4 && !agent_id) {
            alert('请搜索代理商并选择');
            $('#addAccount').find('[name=addClassify]').focus();
            return false;
        }
        $('#addAccountBtn').attr('disabled','disabled');
        $.ajax({
            headers: "Access-Control-Allow-Origin: *",
            type : "post",
            url: add_account_url,
            dataType: 'json',
            data : {
                crmName:crmName,
                crmUid:addCrmUid,
                opportunityName:opportunityName,
                opportunityId:opportunityId,
                logName:logName,
                pasd:pasd,
                classify:classify,
                agent_id:agent_id,
                classpid:classpid,
                classid:classid,
                province_id:province_id,
                city_id:city_id,
                county_id:county_id,
                ssdiyu:ssdiyu,
                ss_city:ss_city,
                ss_county:ss_county,
                xiaoshou:xiaoshou,
                templateType:templateType,
                kusex:leixing,
                userLeve:banben,
                keywordnum:keywordnum,
                region_lock_word:region_lock_word,
                bindphone:bindphone
            },

            success:function(res){
                // 关闭弹出层
                // parent.layer.close(index);
                $('#addAccountBtnLoading').hide();
                $('#addAccountBtn').show();
                // console.log('res====', res);
                if (res.data && res.data.status == 1) {
                    // 关闭弹框
                    $('#uploadModal2').modal('hide');
                    if (res.create_notice && res.create_notice.code == 200){
                        $('#createdSucModalLabel')[0].style.display = 'inline'
                        $('#createdSucLabel')[0].style.display = 'none'
                    }else {
                        $('#createdSucModalLabel')[0].style.display = 'none'
                        $('#createdSucLabel')[0].style.display = 'inline'
                    }
                    $('#enterId').val(addCrmUid);
                    let uname = $('#maintainer').val()
                    let params = `userid=${res.data.uname}&password=${res.data.passwd}&type=logintype&loguser=${uname}`;
                    $('#enterSecretaryUrl').val(params);
                    let has_syc = res.data.has_syc == 1?true:false
                    hasSyc(has_syc)
                    $('#createdSucModal').modal('show');
                    // 调接口通知2组已经创建了一个秘书账号（传参：token、userId）
                    // var url = "/customer/get_environment/api";
                    // $.get(url, function(data) {
                    //     var envi = data.data;
                    //     if (envi == 'product') {
                    //         // 线上端口
                    //         var port_number = '30002';
                    //     } else {
                    //         // beta端口
                    //         var port_number = '32002';
                    //     }
                    //     var create_url = "http://192.168.223.230:" + port_number + "/user/create";
                    //     var headers = {
                    //         "token": "emh4Zy1zdXBwb3J0",
                    //         "userId": res.data.result
                    //     }
                    //     // console.log(create_url)
                    //     // console.log(headers)
                    //     $.ajax({
                    //         type: "post",
                    //         url: create_url,
                    //         headers: headers,
                    //         success: function (res2) {
                    //             console.log(res2)
                    //         }
                    //     });
                    // });

                    // window.location.reload(true);
                } else {
                    // 关闭弹出层
                    // parent.layer.close(index);
                    $('#addAccountBtnLoading').hide();
                    $('#addAccountBtn').show();
                    $('#addAccountBtn').removeAttr('disabled');
                    alert(res.data.msg);
                }
            }
        });
    }
    return false;
});
//模态框判断是否显示调研表提示
function hasSyc(h){
    if(h == 1){
        $('#hasSyc')[0].style.display = 'block'
        $('#noSyc')[0].style.display = 'none'
    }else{
        $('#hasSyc')[0].style.display = 'none'
        $('#noSyc')[0].style.display = 'block'
    }
}

//进入舆情秘书
function enterSecretary(){
    let params = $('#enterSecretaryUrl').val();
    let url = window.location.host == 'support20-beta.istarshine.com'? 
            `http://yqms-beta-g3.istarshine.com/Login/doLogin?${params}`:
            `http://yqms.istarshine.com/Login/doLogin?${params}`
    window.open(url);
}

// 创建账号弹框-同步CRM按钮
$("#crmSyncBtn").click(function(){
    var customerId = $('#accountId').val();
    var sync_url = "/customer/sync_crm/api?account_id=" + customerId;
    var index = parent.layer.load(0, {shade:0.2,content: '<br><br><div style="color:#000;width:200px;font-size:18px;margin-left:-36px;font-weight:400">同步客户信息中...</div>'});
    $.get(sync_url, function(data) {
        if (data.code != 1) {
            alert('同步CRM数据失败,请联系管理员！')
            return false;
        }else {
            // 关闭弹出层
            parent.layer.close(index);
            // 重新打开创建账号弹框
            get_opp_infos(customerId);
        }
    });

});
