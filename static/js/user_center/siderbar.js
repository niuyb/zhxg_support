// 渲染侧边栏
function renderSiderbar(){
    var url = $("#siderbar-api").text();
    // 获取侧边栏数据
    $.get(url, function(data, status){
        if (data.status == null || data.status == undefined){
            // window.location.reload();
            return;
        }
        if (data.status < 1){
            alert(data.message);
        }
        var sbs = data.siderbar;
        var struct = {};
        for (var k in sbs){
            var v = sbs[k];
            p = v.parent
            if (!(struct[p])){
                struct[p] = {}
            }
            struct[p][k] = {};
        }
        var tree = struct[null];
        for (var k in tree){
            tree[k] = struct[k];
        }
        for (var a in tree){
            var sb = sbs[a];
            var children = tree[a];
            var ele = "";
            if (!children || children.length == 0){
                ele = '<li>'
                        + '<a class="" href="' 
                        + sb.url 
                        + '">'
                        + '<i class="fa '
                        + sb.icon
                        + '"></i>'
                        + '<span class="nav-label">' 
                        + sb.content
                        + '</span>'
                        + '</a>'
                        + '</li>'
            }else{
                ele = '<li> <a href="'
                        + 'javascript:;'// + sb.url
                        + '"><i class="fa '
                        + sb.icon
                        + '"></i> <span class="nav-label">' 
                        + sb.content 
                        + '</span> <span class="fa arrow"></span></a>'
                        + '<ul class="nav nav-second-level">'
                for (var b in children){
                    var cld = sbs[b];
                    ele += ('<li><a class="" href="'
                            + cld.url
                            + '">'
                            + '<i class="fa '
                            + cld.icon
                            + '"></i>'
                            + cld.content
                            + '</a>'
                            + '</li>')
                }
                ele += '</ul></li>'
                
            }
            $("#side-menu").append(ele);
        }
        // document.write("<script language=javascript src='/static/js/plugins/metisMenu/jquery.metisMenu.js'></script>");
        // document.write("<script language=javascript src='/static/js/plugins/pace/pace.min.js'></script>");
    });
}

function monitSiderbar(){
    $(document).ready(function(){
        $("#side-menu a").each(function(){
            $this = $(this);
            if ($this[0].href == String(window.location).split("/")[1]){
                $this.parent().addClass("active");
            }
        })
    })
}
renderSiderbar();
