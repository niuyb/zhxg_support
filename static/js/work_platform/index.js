
// 清空corpId
sessionStorage.setItem("corpId", null);

// 清空sessionStorage中的侧边导航信息，以免后端更新了，而前端无法更新的情况
sessionStorage.setItem("sidebarItems", null);

let curUrl = document.location.toString();
let corpId = curUrl.split("corpId=")[1];

sessionStorage.setItem("corpId", corpId);

var app = new Vue({
    el: "#main",
    delimiters: [ "[[", "]]" ],
    mixins: [ sidebarMixin ],
}); 