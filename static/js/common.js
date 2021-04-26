// created by TomTsong 20200108

//输出base64编码
function base64 (s) { return window.btoa(s) }

//表单提交时，检测必填字段
function checkFormCommon(fields){
    for (var i in fields){
        var field = fields[i];
        var Id = "#id_" + field;
        if (!$(Id).val()){
            return false;
        }
    }
    return true;
}

// 向后台发送用户操作记录
function sendUserLog(url, info){
    var js = [];
    for (var k in info){
        var v = info[k];
        js.push(encodeURIComponent(k) + "=" + encodeURIComponent(v));
    } 
    var query = js.join("&")
    url += "?" + query
    $.get(url, function(data, status){if (data.status < 1){
            console.log(data.message);
        }
    });
}

// 数字换成三位逗号的形式，例如：1,000,000,000
function toThousands(num) {
    var num = parseInt(num || 0).toString(),
    result = '';
    while (num.length > 3) {
        result = ',' + num.slice( - 3) + result;
        num = num.slice(0, num.length - 3);
    }
    if (num) {
        result = num + result;
    }
    return result;
}

/*
*js格式化数字代码
*
*value: 要格式化的数字值
*scale: 最多保留几位小数
*zeroed: 是否保留尾0
*percented: 是否转称百分比形式
*
*/
function formatNumber(value, scale, zeroed, percented) {
    if (value == null) return percented ? '0%': 0;
    var mr = ('' + value).match(/^\d+\.?\d*$/);
    if (!mr) return percented ? '0%': 0;
    mr = (percented ? (value = Number(mr[0]) * 100) + '': mr[0]).split('.');
    // console.info(mr);
    if (mr.length == 1) return (zeroed ? (mr[0] + ((function() {
        var r = '.';
        for (var i = 0; i < scale; i++) {
            r += '0';
        }
        return r;
    } ()))) : mr[0]) + (percented ? '%': '');
    var mr_l = mr[0],
    mr_r = mr[1];
    if (mr_r.length == scale) return (zeroed ? (mr_l + '.' + mr_r) : (value + '').replace(/\.*0+$/, '')) + (percented ? '%': '');
    else if (mr_r.length < scale) return (zeroed ? value + ((function() {
        var r = '';
        for (var i = 0; i < scale - mr_r.length; i++) {
            r += '0';
        }
        return r;
    })()) : (value + '').replace(/\.*0+$/, '')) + (percented ? '%': '');
    else {
        var _s = mr_r.substr(0, scale + 1);
        _s = _s.charAt(scale) > 4 ? (Number(_s.substring(0, scale)) + 1) + '': _s.substring(0, scale);
        if (_s.length == (scale + 1)) {
            mr_l = (Number(mr_l) + Number(_s.charAt(0))) + '';
            _s = _s.substring(1);
        }
        return (zeroed ? (mr_l + '.' + _s) : (mr_l + (_s.match(/^0*$/) ? '': ('.' + _s.replace(/0+$/, ''))))) + (percented ? '%': '');
    }
};

/*
*js数字千分位格式化代码
*
*value: 要格式化的数字值
*seperator: 千分位符号
*digitNum: 保留几位小数
*/

function formatNumber2(value, seperator, digitNum) {

    var initV = value;
    if ((value = ((value = value + "").replace(/^\s*|\s*$|,*/g, ''))).match(/^\d*\.?\d*$/) == null) return initV;
    value = digitNum >= 0 ? (Number(value).toFixed(digitNum) + "") : value;
    var r = [],
    tl = value.split(".")[0],
    tr = value.split(".")[1];
    tr = typeof tr != "undefined" ? tr: "";
    if (seperator != null && seperator != "") {
        while (tl.length >= 3) {
            r.push(tl.substring(tl.length - 3));
            tl = tl.substring(0, tl.length - 3);
        }
        if (tl.length > 0) r.push(tl);
        r.reverse();
        r = r.join(seperator);
        return tr == "" ? r: r + "." + tr;
    }
    return value;
};

// 从当前窗口链接中获取参数
function getUrlKey(name, url){
    return decodeURIComponent((new RegExp('[?|&]' + name + '=' + '([^&;]+?)(&|#|;|$)').exec(url) || [, ""])[1].replace(/\+/g, '%20')) || null
}

// 表格渲染过程中用到的通用formatter，将空字符串替换成你想要的值
function nullStrFormatter(str, to){
    // to: if str is "", replace str to `to`
    if (to === undefined){
        to = "----";
    }
    if (!str){
        str = to;
    }
    return str;
}

function NumberRange(min, max){
    this.min = min;
    this.max = max;
}

function DateRange(start, end){
    this.start = start;
    this.end = end;
}

function stringToDate(str){
    if (!str){
        return 0
    }

    // 兼容火狐
    str = str.split(" ")[0];
    str = str.replace("年", "/").replace("月", "/").replace("日", "").replace(/-/g, "/");
    
    var date = new Date(str);
    return date;
}

function stringToDateTime(str){
    if (!str){
        return 0
    }

    // 兼容火狐
    str = str.replace("年", "/").replace("月", "/").replace("日", "").replace(/-/g, "/");
    
    var date = new Date(str);
    return date;
}

function toYearMonthString(){
    let thetime = new Date();
    return thetime.getFullYear() + "/" + (thetime.getMonth() + 1);
}

function countDays(from, to){
    if (typeof from == "string"){
        if (/^\d{8}$/.test(from)){
            from = from.substr(0, 4) + "/" + from.substr(4, 2) + "/" + from.substr(6, 2);
        }
    }
    if (typeof to == "string"){
        if (/^\d{8}$/.test(to)){
            to = to.substr(0, 4) + "/" + to.substr(4, 2) + "/" + to.substr(6, 2);
        }
    }
    if (!from){
        from = new Date().toLocaleDateString();
    }
    from = stringToDate(from)
    if (!to){
        to = new Date().toLocaleDateString();
    }
    to = stringToDate(to)
    return (to - from) / 1000 / 3600 / 24
}

/**
 * common.js中定义了CommonLocation类，
 * 类中实现了通用的获取省、市、县的方法，
 * 调用时，只需要实例化CommonLocation
 */
function CommonLocation(){
    let self = this;
    self.states = null;
    self.cities = null;
    self.districts = null;
    self.parse = function(ID){
        let text = $("#" + ID).text();
        let js = JSON.parse(text);
        return js;
    };
    self.parseStates = function(){
        return self.parse("states")
    };
    self.parseCities = function(){
        return self.parse("cities")
    };
    self.parseDistricts = function(){
        return self.parse("districts")
    };
    self.getStates = function(){
        if (!self.states){
            self.states = self.parseStates()
        }
        let states = [];
        for (let state of self.states){
            let item = [state.lid, state.lname];
            states.push(item)
        }
        return states;
    };
    self.getCities = function(pid){
        if (!self.cities){
            self.cities = self.parseCities()
        }
        let cities = [];
        for (let city of self.cities){
            if (city.pid == pid){
                let item = [city.lid, city.lname];
                cities.push(item);
            }
        }
        return cities;
    };
    self.getDistricts = function(pid){
        if (!self.districts){
            self.districts = self.parseDistricts()
        }
        let districts = [];
        for (let district of self.districts){
            if (district.pid == pid){
                let item = [district.lid, district.lname];
                districts.push(item);
            }            
        }
        return districts;
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

// 多级联动通用的监听select变化的方法
function onSelectChange(prefix, index, getNextSelData){
    /**
     * prefix: 前坠，多级联运的元素div, select等元素的id里面加上统一的前坠，方便控制
     * index: 索引，代表当前是第几级select发生了变化
     * getNextSelData: 函数，用于获取下一级select的options数据
     */

    let curSel = "#" + [prefix, "select", index].join("-");
    let op = $(curSel + " option:selected").val();

    let lastSel = "#" + [prefix, "select", index-1].join("-");
    
    // 存储当前select的value
    let input = "#" + [prefix, "input"].join("-");
    $(input) && $(input).val(op);

    // 如果当前select的value是空，保存上一级select的value
    if (!op){
        let _op = $(lastSel + " option:selected").val();
        $(input) && $(input).val(_op);
    }
    let nextDiv = "#" + [prefix, "div", index+1].join("-");
    let nextSel = "#" + [prefix, "select", index+1].join("-");

    // 因为option发生了变化，所以先清空所有下级select
    for (let i=index+1; i<10; i++){
        let sel = "#" + [prefix, "select", i].join("-");
        let div = "#" + [prefix, "div", i].join("-");
        $(sel).empty();
        $(div).css("display", "none");
    }

    // 下一级select数据加载完之前，禁止改选其他option
    for (var i=0; i<=index; i++){
        let sel = "#" + [prefix, "select", i].join("-");
        $(sel).attr("disabled", "disabled");
    }

    // 首先先清空原select元素下面的options
    $(nextSel).empty();

    //将options逐条渲染之后添到select里面
    if (op){
        let nextSelData = getNextSelData(op);
        nextSelData = completeOptions(nextSelData);
        $(nextDiv).css("display", "block");
        renderSelect(nextSel, nextSelData);
    }
    
    // 下一级select数据加载完之后，解禁其他select
    for (var i=0; i<=index; i++){
        let sel = "#" + [prefix, "select", i].join("-");
        $(sel).attr("disabled", null);
    }
}

// 当点击表单重置按钮时，多级联动会出现下级select不隐藏的问题，调用此函数隐藏下级select
function commonSelectReset(prefix){
    let sel = [prefix, "select", 1].join("-");
    $("#" + sel + " option[value='']").prop("selected", "selected");
    onSelectChange(prefix, 1, null);
}

// 比较两个json是否相等
function compareTwoObjects(a, b){
    let ok = true;
    if (a.length !== b.length){
        ok = false;
    }else{
        for (let k in a){
            if (!(k in b)){
                ok = false;
                break;
            }
            let av = a[k];
            let bv = b[k];
            if (av !== bv){
                ok = false;

                if ((typeof av === "object") && (typeof bv === "object")){
                    ok = compareTwoObjects(av, bv);
                }
                if (!ok){
                    break;
                }
            }
        }
    }
    return ok;
}

function zeroRedFormatter(rowData, index, pagingIndex) {
    var field = this.field;
    return rowData[field] == 0 ? '<span style="color:red;font-weight: bold;">' + 0 + '</span>': toThousands(rowData[field]);
}

function simpleRateFormatter(rowData, index, pagingIndex){
    var field = this.field;
    return rowData[field] == 0 ? '<span style="color:red;font-weight: bold;">' + 0 + '</span>': rowData[field] + "%";
}

function dateToString(date){ 
  var year = date.getFullYear(); 
  var month =(date.getMonth() + 1).toString(); 
  var day = (date.getDate()).toString();  
  if (month.length == 1) { 
      month = "0" + month; 
  } 
  if (day.length == 1) { 
      day = "0" + day; 
  }
  var dateTime = year + "-" + month + "-" + day;
  return dateTime; 
}
