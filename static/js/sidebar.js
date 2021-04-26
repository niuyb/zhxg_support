$(document).ready(function(){
    var pathname = window.location.pathname;
    if (!pathname || pathname == "/"){
        return false;
    }
    var lis = $("#side-menu li");
    if (lis.length == 0){
        return false;
    }
    // lis.each(function(i, li){
    //     $(li).removeClass("active");
    //     var aes = $(li).children("a");
    //     aes.each(function(a, b){
    //         $(b).css("color", "");
    //     });
    //     var uls = $(li).children("ul");
    //     uls.each(function(i, ul){
    //         $(ul).removeClass("in");
    //         var ls = $(ul).children("li");
    //         ls.each(function(x, y){
    //             var aes = $(y).children("a");
    //             aes.each(function(m, n){
    //                 $(n).css("color", "");
    //             });
    //         });
    //     });
    // });
    lis.each(function(i, li){
        var aes = $(li).children("a");
        if (aes.length == 0){
            return true;
        }
        var a = aes[0];
        // $(a).css("color", "");
        var hh = $(a).attr("href");
        if (hh.indexOf(pathname) != -1){
            $(a).css("color", "white");
            return false;
        }
        var uls = $(li).children("ul");
        if (uls.length == 0){
            return true;
        }
        var ul = uls[0];
        var ls = $(ul).children("li");
        if (ls.length == 0){
            return true;
        }
        ls.each(function(x, y){
            var aes = $(y).children("a")
            if (aes.length == 0){
                return true;
            }
            var a = aes[0];
            var h = $(a).attr("href");
            if (h && h.indexOf(pathname) != -1){
                $(li).addClass("active");
                $(ul).addClass("in");
                $(a).css("color", "white")
                return false;
            }
        })
    })
});
