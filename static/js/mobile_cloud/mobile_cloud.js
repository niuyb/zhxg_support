$('#submit_to_crm').on('click', function(){
    var arr = new Array()
    var status = 0;
    $('[the-id=data_table]').each(function(k,v){
        tmp = new Object()
        tmp['account_code'] = $(this).find('[name=account_code]').val();
        tmp['industry1'] = $(this).find('[name=industry1] option:selected').val();
        tmp['industry2'] = $(this).find('[name=industry2] option:selected').val();
        arr.push(tmp);
        if ($(this).find('[name=industry2] option:selected').val() == '') {
            alert('行业信息不完整，请选择客户行业');
            status = 1;
            return false;
        }
    })
    var data = JSON.stringify(arr);
    var file_name = $('[name="file_name"]').val()
    var file_path = $('[name="file_path"]').val()
    var jump = $(this).attr('jump');
    if (arr.length>0 && status != 1) {
        $('#submit_to_crm').html('正在处理中，请稍后……').attr("disabled",'disabled');
        var dataId=$('[the-id=yqms]').find("option:selected").val();
        $.ajax({
            type:'post',
            url:jump,
            data:{data:data,file_name:file_name},
            dataType:'json',
            success : function(res){
                if (res.status==1) {
                    $('#submit_to_crm').html('处理完毕，请查看附件')
                    location=file_path + '/' + res.data;
                }else{
                    $('#submit_to_crm').html('确定提交销售易').removeAttr("disabled");
                    alert(res.msg);
                }
            }
        })
    }
})