// function init_opportunity_Vue(){
//     new Vue({
//         el: '#opportunity',
//         delimiters: ["[[", "]]"],
//         data:{
//             status: 2,
//         	opp_infos:{},
//
//         },
//         methods: {
//             get_opp_infos(){
//                 let url = "/work_platform/task/oppapi";
//                 let self = this;
//                 axios.get(url).then(res => {
//                     if (res.status == 200){
//                         self.opp_infos = res.data;
//                         // console.log(self.opp_infos)
//                     }else{
//                         this.$message.error(res.status);
//                     }
//                 });
//             },
//             show_add_task(id,opp_name){
//                 this.$refs.entityObjectId.name=id[0][0]
//                 this.$refs.entityObjectId.value=opp_name
//                 this.status=1
//             },
//             hidden_add_task(){
//                 this.status=2
//             },
//
//             creat_task(){
//                 var taskName = "taskName="+this.$refs.taskName.value
//                 var planFinishDate = "&planFinishDate="+this.$refs.planFinishDate.value
//                 var planStartDate = "&planStartDate="+this.$refs.planStartDate.value
//                 var ownerId = "&ownerId="+this.$refs.ownerId.value
//                 var startReminder = "&startReminder="+this.$refs.startReminder.value
//                 var finishReminder = "&finishReminder="+this.$refs.finishReminder.value
//                 var entityBelongId = "&entityBelongId="+this.$refs.entityBelongId.value
//                 var entityObjectId = "&entityObjectId="+this.$refs.entityObjectId.name
//                 var description = "&description="+this.$refs.description.value
//                 var memberIds = "&memberIds="+this.$refs.memberIds.value
//                 if(entityBelongId == "&entityBelongId=客户"){
//                      entityBelongId = "&entityBelongId=1"
//                 }else if(entityBelongId == "&entityBelongId=商机"){
//                      entityBelongId = "&entityBelongId=3"
//                 }
//                 if (startReminder == "提醒"){
//                      startReminder = "&startReminder=500"
//                 }else{
//                      startReminder = " "
//                 }
//                 if (finishReminder == "提醒"){
//                      finishReminder = "&finishReminder=500"
//                 }else{
//                      finishReminder = " "
//                 }
//                 var url ="/work_platform/task/addtask?"+taskName+planFinishDate+planStartDate+ownerId+startReminder+finishReminder+entityBelongId+entityObjectId+description+memberIds;
//                 // console.log(url)
//                 axios.get(url).then(res=>{
//                     if (res.status == 200){
//                         // console.log(res.data.res)
//                         if (res.data.res == "success"){
//                             alert("任务创建 成功");
//                         }else{
//                             alert("任务创建 失败");
//                         }
//                     }else{
//                         this.$message.error(res.status);
//                     }
//                 })
//             },
//         },
//
//         created() {
//             this.get_opp_infos();
//
//         },
//     })
// }


function init_record_Vue(uid){
    new Vue({
        el: '#record',
        delimiters: ["[[", "]]"],
        data:{
        	modify_task:{}
        },
        methods: {
            get_opp_infos(uid){
                var url;
                if (uid != "None"){
                     url = "/work_platform/task/logapi?id="+uid ;
                }else{
                     url = "/work_platform/task/logapi";
                    }
                let self = this;
                axios.get(url).then(res => {
                    console.log(Object.keys(res.data.data).length);
                    if (res.status == 200){
                        if(Object.keys(res.data.data).length > 0){
                            this.modify_task = res.data;
                        }else{
                            self.modify_task = "None"
                        }
                    }else{
                        self.modify_task = "None"
                    }
                    // console.log("logapi",this.modify_task)
                });
            },
        },
        created() {
            this.get_opp_infos(uid);
        },
    })
}

//获取商机任务数据
function get_opp_infos(did){
	if (did != "None"){
		var opp_url = "/work_platform/task/oppapi?id="+did ;
	}else{
		var opp_url = "/work_platform/task/oppapi";
		}
    axios.get(opp_url).then(res => {
        if (res.status == 200){
            data_object = res.data.data
            if(data_object.length >0){
                for(var i = 0,len = data_object.length; i < len; i++){
                var div;
                div = '<div class=\"task_list_box border_box\">'+
                        '<div class="list_title flex" >'+data_object[i].oppunity_name+'</div>'+
                        '<div class="last_customer flex">最终客户：'+data_object[i].customer+'</div>'+
                        '<div class="list_txt flex_between">'+
                            '<div class="txt_left flex_1">赢率：'+data_object[i].win_rate+'</div>'+
                            '<div class="txt_right flex_1">销售承若：'+data_object[i].permise+'</div>'+
                        '</div>'+
                        '<div class="list_txt flex_between">'+
                            '<div class="txt_left flex_1">金额：'+data_object[i].money+'元</div>'+
                            '<div class="txt_right flex_1">结单日期：'+data_object[i].close_date+'</div>'+
                        '</div>'+
                        '<div class="list_txt flex_between">'+
							'<div class="txt_right flex_1">商务：'+data_object[i].saler+'</div>'+
                        '</div>'+
                        '<div class="badtips flex">堵点:'+data_object[i].badlabel+'</div>'+
                        '<div class="ops_btn_box"><button class="btn addTask" value="'+data_object[i].oppid+'&'+data_object[i].saler+'" name="'+data_object[i].oppunity_name+'"  >加任务</button></div>'+
                        '</div>'
                $("#opportunity").append(div);//将创建好的td挂载到table下

            $('.addTask').click(function(e){
                $('.dialog').show();
                var opp_value = e.target.value
                var opp_name = e.target.name
				var opp_id = opp_value.split("&")[0]
				var opp_saler = opp_value.split("&")[1]
                var entityObjectId= $('#entityObjectId')
                entityObjectId.attr("value",opp_name)
                entityObjectId.attr("name",opp_id)
				$('#ownerid').attr("value",opp_saler)
            });
            $('.dialog_close,.cancle_btn').click(function(){
                $('.dialog').hide();
                $('#date-wrapper').hide();
                $('#d-mask').hide();
	});

            }
            }else{
				div = '<div class=\"task_list_box border_box\"><div class="list_title flex">暂无数据</div></div>'
            	$("#opportunity").append(div);
            }
        }else{
            data_array =  "failed";
            div = '<div class=\"task_list_box border_box\"><div class="list_title flex">暂无数据</div></div>'
            $("#opportunity").append(div);//将创建好的td挂载到table下
        }
    });
}


function init_task_Vue(uid){
    new Vue({
        el: '#rightPart2',
        delimiters: ["[[", "]]"],
        data:{
        	my_task:{},
        	uid:uid
        },
        methods: {
            get_task_infos(uid) {
                var task_url;
                if (uid != "None"){
                     task_url ="/work_platform/task/taskapi?id="+uid ;
                }else{
                     task_url ="/work_platform/task/taskapi";
                    }
                // event.currentTarget
                // var task_url = "/work_platform/task/taskapi";
                let self = this;
                axios.get(task_url).then(res => {
                    if (res.status == 200) {
                        if(Object.keys(res.data.data).length > 0){
                            self.my_task = res.data;
                        }else{
                            self.my_task = "None"
                        }
                    } else {
                        self.my_task = "None"
                    }
                    // console.log("taskapi",self.my_task)
                });
            },
            click_task_infos(event){
                var day_num = event.currentTarget.innerHTML
                var date_str=this.$refs.curday.innerHTML
                date_all = date_str.split("月")[0]
                date_day = date_str.split("月")[1]
                date_day = date_day.replace("日","")
                date_year = date_all.split("年")[0]
                date_month = date_all.split("年")[1]
                if(Number(date_day) > Number(day_num)){
                    date_month = (Number(date_month) + 1).toString()
                    if(date_month == "13"){
                        date_month = "1"
                    }
                }
                var date = date_year+"-"+date_month+"-"+day_num
                // console.log(date)

                var task_url = "/work_platform/task/taskapi?date="+date+'&id='+this.uid;
                let self = this;
                axios.get(task_url).then(res => {
                    if (res.status == 200){
                        self.my_task = res.data;
                        // console.log(self.my_task)
                    }else{
                        this.$message.error(res.status);
                    }
                });
            }},
        created() {
            this.get_task_infos(uid);
        },
        // watch: {
        //     "my_task": "initTable",
        // }
    })
}


$(function() {

    uid = $("#uid").text()
    init_task_Vue (uid)
    init_record_Vue(uid)
    get_opp_infos(uid)

    $.date('#bTime');
    $.date('#eTime');

    // 创建任务
	$('.create_btn').click(function(e){
		var task_name = "taskName="+$('#task_name').val()
		var bTime = "&planStartDate="+$('#bTime').val()
		var eTime = "&planFinishDate="+$('#eTime').val()
		var b_remind = "&finishReminder="+$('#b_remind').val()
		var e_remind = "&startReminder="+$('#e_remind').val()
		var ownerid = "&ownerId="+$('#ownerid').val()
		var member = "&memberIds="+$('#member').val()
		var blongid = "&entityBelongId="+$('#blongid').val()
		var entityObjectId = "&entityObjectId="+$('#entityObjectId').attr("name")
		var description = "&description="+$('#description').val()

		var url ="/work_platform/task/addtask?"+task_name+eTime+bTime+ownerid+b_remind+e_remind+blongid+entityObjectId+description+member;
		// console.log(url)
		axios.get(url).then(res=>{
			if (res.status == 200){
				// console.log(res.data.res)
				if (res.data.res == "success"){
					alert("任务创建 成功");
				}else{
					alert("任务创建 失败");
				}
			}else{
				this.$message.error(res.status);
			}
		})

	});


    $("#monitor td button").click(function () {
        $(this).addClass('mark1').parent().siblings().children('button').removeClass('mark1');
        // curday = document.getElementById('curday');
        // console.log(curday.innerHTML)
    });

    var cells = document.getElementById('monitor').getElementsByTagName('button');
    var day1 = document.getElementById('curday');
    var day7 = document.getElementById('curday7');
    var clen = cells.length;
    var currentFirstDate;
    var myDate = new Date();
    today = myDate.getDate();//获取当前日期

    var formatDate = function (date) {
        var year = date.getFullYear() + '年';
        var month = (date.getMonth() + 1) + '月';
        var day = date.getDate();
        var week = '(' + ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六'][date.getDay()] + ')';

        return day;
    };

    var addDate = function (date, n) {
        date.setDate(date.getDate() + n);
        return date;
    };
    var setDate = function (date) {
        var week = date.getDay();
        date = addDate(date, week * -1);
        currentFirstDate = new Date(date);

        for (var i = 0; i < clen; i++) {
            cells[i].innerHTML = formatDate(i == 0 ? date : addDate(date, 1));
            if (cells[i].innerHTML == today) {
                cells[i].className = 'mark1';
            }
            ;

            if (date.getMonth() == 0) {
                date_month = 12
            } else {
                date_month = date.getMonth()
            }

            if (cells[6].innerHTML - 7 <= 0) {
                if (date_month == 13) {
                    date_month = 1
                }
                day1.innerHTML = date.getFullYear() + '年' + (date_month) + '月' + cells[0].innerHTML + '日';
            } else {
                if (date_month + 1 == 13) {
                    date_month = 0
                }
                day1.innerHTML = date.getFullYear() + '年' + (date_month + 1) + '月' + cells[0].innerHTML + '日';
            }
            if (date_month + 1 == 13) {
                date_month = 0
            }
            day7.innerHTML = date.getFullYear() + '年' + (date_month + 1) + '月' + cells[6].innerHTML + '日';


        }

    };
    document.getElementById('last-week').onclick = function(){
        setDate(addDate(currentFirstDate,-7));
    };
    document.getElementById('next-week').onclick = function(){
        setDate(addDate(currentFirstDate,7));
    };
    document.getElementById('lastM').onclick = function(){
        setDate(addDate(currentFirstDate,-30));
    };
    document.getElementById('nextM').onclick = function(){
        setDate(addDate(currentFirstDate,30));
    };
    setDate(new Date());

});


// $(function(){
//     $('.ops_btn_box .btn').click(function(){
//         $('#task_dialog').show();
//     });
//
//     $('.dialog_close, .doalog_btns_box .cancle_btn').click(function(){
//         $('#task_dialog').hide();
//     });
//
//
// })