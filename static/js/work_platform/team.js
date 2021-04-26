
//处理echarts中图表的字体大小问题
function getDpr(){
	var dpr = $('html').attr('data-dpr');
	if (dpr == 1) {
		return 12;
	}else if (dpr == 2) {
		return  20;
	}else {
		return 32;
	}
}

//获取商机任务数据
function get_opp_infos(did){
	if (did != "None"){
		var opp_url = "/work_platform/task/oppapi?depart="+did ;
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
							'<div class="txt_right flex_1" >商务：'+data_object[i].saler+'</div>'+
                        '</div>'+
                        '<div class="badtips flex">堵点:'+data_object[i].badlabel+'</div>'+
                        '<div class="ops_btn_box"><button class="btn addTask" value="'+data_object[i].oppid+'&'+data_object[i].saler +'&'+data_object[i].leader_name+'" name="'+data_object[i].oppunity_name+'" leader="'+data_object[i].leader_name+'" >加任务</button></div>'+
                        '</div>'
                $("#opportunity").append(div);//将创建好的td挂载到table下

            $('.addTask').click(function(e){
                $('.dialog').show();
                var opp_value = e.target.value
                var opp_name = e.target.name
				var opp_id = opp_value.split("&")[0]
				var opp_saler = opp_value.split("&")[1]
				var leader_name =opp_value.split("&")[2]
                var entityObjectId= $('#entityObjectId')
                entityObjectId.attr("value",opp_name)
                entityObjectId.attr("name",opp_id)
				$('#ownerid').attr("value",opp_saler)
				$('#member').attr("value",leader_name)
                // entityObjectId.attr("name",opp_id)
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

function get_depart_infos(did,level){
		if (did != "None"){
			var depart_url ="/work_platform/team/departapi?depart="+did+"&level="+level;
		}else{
			var depart_url ="/work_platform/team/departapi";
		}
	    axios.get(depart_url).then(res => {
			if (res.status == 200) {
				data_object = res.data.data
				type = res.data.type
				if(type == "province"){
					for(var i = 0,len = data_object.length; i < len; i++){
						var div;
						div = '<div class="task_list_box border_box">'+
								'<div class="list_txt flex_between">'+
									'<div class="txt_left flex_1">人员：<a href="/work_platform/task/per?uid='+data_object[i].id+'" style="color: blue" >'+data_object[i].name+'</a></div>'+
									'<div class="txt_right flex_1">部门：'+data_object[i].depart_name+'</div>'+
								'</div>'+
								'<div class="list_txt flex_between">'+
									'<div class="txt_left flex_1">任务数：'+data_object[i].task_num+'</div>'+
									'<div class="txt_right flex_1">客户数：'+data_object[i].account_num+'</div>'+
								'</div>'+
								'<div class="list_txt flex_between">'+
									'<div class="txt_left flex_1">任务覆盖客户数：'+data_object[i].cover_num+'</div>'+
									'<div class="txt_right flex_1">完成任务数：'+data_object[i].complete_num+'</div>'+
								'</div>'+
								'<div class="list_txt flex_between">'+
									'<div class="txt_left flex_1">延期任务数：'+data_object[i].delay_num+'</div>'+
									'<div class="txt_right flex_1">删除任务数：'+data_object[i].delete_num+'</div>'+
								'</div>'+
							  '</div>'
						$("#team_department").append(div);
					}
				}
				else{
					var depart_level = 0
					if(type=="department"){depart_level = 1;}else if(type=="region"){ depart_level=0; }else{return}
					for(var i = 0,len = data_object.length; i < len; i++){
						var div;
						div = '<div class="task_list_box border_box">'+
								'<div class="list_txt flex_between">'+
									'<div class="txt_left flex_1">部门：<a href="/work_platform/task?level='+depart_level+'&depart='+data_object[i].departId+'" style="color: blue">'+data_object[i].depart_name+'</a></div>'+
									'<div class="txt_center flex_1">本周任务：'+data_object[i].task_num+'</div>'+
									'<div class="txt_right flex_1">客户数：'+data_object[i].account_num+'</div>'+
								'</div>'+
								'<div class="list_txt flex_between">'+
									'<div class="txt_left flex_1">任务覆盖客户数：'+data_object[i].cover_num+'</div>'+
									'<div class="txt_center flex_1">完成数：'+data_object[i].complete_num+'</div>'+
								'</div>'+
								'<div class="list_txt flex_between">'+
									'<div class="txt_left flex_1">延期任务数：'+data_object[i].delay_num+'</div>'+
									'<div class="txt_right flex_1">删除任务数：'+data_object[i].delete_num+'</div>'+
								'</div>'+
							   '</div>'
						$("#team_department").append(div);
					}
				}
			}
			else{
            data_array =  "failed";
            div = '<div class=\"task_list_box border_box\"><div class="list_title flex">暂无数据</div></div>'
            $("#team_department").append(div);//将创建好的td挂载到table下
        	}
		})
}

//获取饼图数据
function get_pei_infos(did,type){
	if (did != "None" && type != "None"){
		var pei_url ="/work_platform/team/peiapi?depart="+did+"&type="+type;
	}else if(did != "None" && type == "None"){
		var pei_url ="/work_platform/team/peiapi?depart="+did;
	} else if(did == "None" && type != "None"){
		var pei_url ="/work_platform/team/peiapi?&type="+type;
	} else{
		var pei_url ="/work_platform/team/peiapi";
	}
	axios.get(pei_url).then(res => {
		data_object = res.data.data
		top_infos = res.data.top
		var pei=$("#pei_infos")
		pei.empty()
		var div
		// = '<div class="dialog_title flex_v_center"><span>任务详情</span><span class="dialog_close_pie">&times;</span></div>'
		for(var i = 0,len = data_object.length; i < len; i++){
			if(i==0){div_1 = '<div class="dialog_title flex_v_center"><span>任务统计</span><span class="dialog_close_pie">&times;</span></div>'}else{div_1=""}
			div =div_1+
				'<div class="task_list_box border_box">'+
					'<div class="list_txt flex_between">'+
						'<div class="txt_left flex_1">人员：<a href="/work_platform/task/per?uid='+data_object[i].id+'" style="color: blue">'+data_object[i].name+'</a></div>'+
						'<div class="txt_right flex_1">部门：'+data_object[i].depart_name+'</div>'+
					'</div>'+
					'<div class="list_txt flex_between">'+
						'<div class="txt_left flex_1">任务数：'+data_object[i].task_num+'</div>'+
						'<div class="txt_right flex_1">完成任务数：'+data_object[i].complete_num+'</div>'+
					'</div>'+
					'<div class="list_txt flex_between">'+
						'<div class="txt_right flex_1">客户数：'+data_object[i].account_num+'</div>'+
						'<div class="txt_left flex_1">任务覆盖客户数：'+data_object[i].cover_num+'</div>'+
					'</div>'+
					'<div class="list_txt flex_between">'+
						'<div class="txt_left flex_1">延期任务数：'+data_object[i].delay_num+'</div>'+
						'<div class="txt_right flex_1">删除任务数：'+data_object[i].delete_num+'</div>'+
					'</div>'+
				  '</div>'
			pei.append(div);
			$('.dialog_close_pie').click(function(){
				var dialog_pie = $('.dialog_pie')
				dialog_pie.hide();
				$("#pei_infos").empty()
				// dialog_pie.attr("value","hide")
			});

		}

		$('#team_name').text("团队名称："+top_infos["departName"])
		$('#team_leader').text("管理人员："+top_infos["name"])
		$('#team_num').text("团队任务数："+top_infos["task_num"])
		$('#team_per').text("人均任务数："+top_infos["saler_num"])

        // echarts 饼图
        var pieBox = echarts.init(document.getElementById('pieBox'));
        pieBoxOption = {
            legend: [{
                left: 'left',
                itemWidth:	20,  // 设置宽度
                itemHeight: 10,  // 高
                // itemGap: 5, //间距
                // x: '20%',
                y: '10%',
                data:['任务数为0'],
				textStyle: {
                    //文字样式
                    // color: "#B4CEFF",
                     fontSize: "10"
                },
            },{
				left: 'left',
                itemWidth:	20,  // 设置宽度
                itemHeight: 10,  // 高
				y: '40%',
				data:['任务数大于5'],
				textStyle: {
					 fontSize: "10"
				}
			},{
				left: 'left',
                itemWidth:	20,  // 设置宽度
                itemHeight: 10,  // 高
				y: '70%',
				data:['任务数大于0小于5'],
				textStyle: {
                     fontSize: "10"
				}
			}],
            series : [
                {
                    name: '访问来源',
                    type: 'pie',
                    radius: [0, '80%'],
                    label: {
                        show:false,
                        // position:'inner',
                        // fontSize: getDpr()
                    },
                    data:[     // 数据数组，name 为数据项名称，value 为数据项值
                        {value:top_infos["total_0"], name:'任务数为0',id:"0"},
                        {value:top_infos["total_2"], name:'任务数大于5',id:"2"},
                        {value:top_infos["total_1"], name:'任务数大于0小于5',id:"1"}
                    ]
                }
            ]
        }

		pieBox.setOption(pieBoxOption);
		// echarts 点击事件
		pieBox.on('click', function (params) {
			pei.empty()
			var dialog_pie=$('.dialog_pie')
			var div = '<div style="color: #333;font-size: .24rem;padding: .06rem .3rem;"><span>加载中...</span></div>'
			pei.append(div)
			get_pei_infos(id,params.data.id)
			dialog_pie.show();
			// dialog_pie.attr("value","show")
		});


	})
}

// 加载后执行
$(function() {
	var app = new Vue({
		el: "#main",
		mixins: [ sidebarMixin, listMixin ],
		data(){
			return{
				show_sort_btn:false,
				show_filter_btn:false,
				show_search_btn:false,
				show_add_btn:false,
				show_back_btn:false,
			}
		},
		methods: {
		}
	});

	level = $('#level').text()
	id = $('#departid').text()
	get_depart_infos(id, level)
	get_opp_infos(id)

	get_pei_infos(id, "None")


	$.date('#bTime');
	$.date('#eTime');
	// 创建任务
	$('.create_btn').click(function (e) {
		var task_name = "taskName=" + $('#task_name').val()
		var bTime = "&planStartDate=" + $('#bTime').val()
		var eTime = "&planFinishDate=" + $('#eTime').val()
		var b_remind = "&finishReminder=" + $('#b_remind').val()
		var e_remind = "&startReminder=" + $('#e_remind').val()
		var ownerid = "&ownerId=" + $('#ownerid').val()
		var member = "&memberIds=" + $('#member').val()
		var blongid = "&entityBelongId=" + $('#blongid').val()
		var entityObjectId = "&entityObjectId=" + $('#entityObjectId').attr("name")
		var description = "&description=" + $('#description').val()

		var url = "/work_platform/task/addtask?" + task_name + eTime + bTime + ownerid + b_remind + e_remind + blongid + entityObjectId + description + member;
		axios.get(url).then(res => {
			if (res.status == 200) {
				if (res.data.res == "success") {
					alert("任务创建 成功");
				} else {
					alert("任务创建 失败");
				}
			} else {
				this.$message.error(res.status);
			}
		})

	});


})

// //阻止事件向上传递
// function stopEvent(event){
// 　　var e=arguments.callee.caller.arguments[0] || event;//这里是因为除了IE有event其他浏览器没有所以要做兼容
// 　　if(window.event){ //这是IE浏览器
// 　　　　e.cancelBubble=true;//阻止冒泡事件
// 　　　　e.returnValue=false;//阻止默认事件
// 　　}else if(e && e.stopPropagation){ //这是其他浏览器
// 　　　　e.stopPropagation();//阻止冒泡事件
// 　　　　e.preventDefault();//阻止默认事件
// 　　}
// }


//阻止事件向上传递
function stopFunc(e) {
	e.stopPropagation ? e.stopPropagation() : e.cancelBubble = true;
}


function point(event){
	var id = "#" +event.id.toString().split("_")[1]
	var pei_height = $(id).offset().top;
	window.scrollTo(0,pei_height-60);
}

