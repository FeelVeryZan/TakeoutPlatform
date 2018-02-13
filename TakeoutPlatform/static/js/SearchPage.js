function onClickBackBtn() {
    window.history.go(-1);
}
function onClickSearchBtn() {
    // 浏览器适配
    var xmlhttp;
    if (window.XMLHttpRequest) {
        xmlhttp = new XMLHttpRequest();                         // code for IE7+, Firefox, Chrome, Opera, Safari
    } else {
        xmlhttp = new ActiveXObject("Microsoft.XMLHTTP");       // code for IE6, IE5
    }
    // 接收到信息后进行的操作
    xmlhttp.onreadystatechange = function() {
        if (xmlhttp.readyState === 4 && xmlhttp.status === 200) {
            var resultBlock = document.getElementById("resultBlock");
            resultBlock.innerHTML = xmlhttp.responseText;
        }
    }
    var text = document.getElementById("searchInput").value;
    var urlGET = "/search/static_refresh/?" + "text=" + text;
    xmlhttp.open("GET", urlGET, true);
    xmlhttp.send();
}
//搜索的排序选项的单选性质
function onChangeSortMethod(i) {
    var searchSortOptContent = new Array("综合排序", "好评优先", "起送价最低", "配送最快");
    var searchSortBtn = document.getElementById("searchSortBtn");
    searchSortBtn.childNodes[0].nodeValue = " " + searchSortOptContent[i] + " ";
    for (var j = 0; j < 4; j ++) {
        var option = document.getElementById("searchSortOpt" + j);
        option.className = "dropdown-" + (i == j ? "" : "un") + "selected";
    }
}
//商家选择的checkbox性质
function onChangeAcceptedSeller(obj) {
    obj.className = obj.className.replace("btn-unselected", "btn-tmp-selected")
                                 .replace("btn-selected", "btn-unselected")
                                 .replace("btn-tmp-selected", "btn-selected");
}
//商家多选区域、优惠活动单选区域，阻值点击一个商家之后dropdown框自己缩回去
$('#searchFilterUi').click(function(e) {
    e.stopPropagation();
});
//优惠活动的单选性质
function onChangeDiscount(i) {
    for (var j = 0; j < 6; j ++) {
        var option = document.getElementById("filterDiscount" + j);
        if (i != j) {
            option.className = option.className.replace("btn-selected", "btn-unselected");
        }
    }
}
//价格区间的初值、范围限制和合法性
function onInputPriceLimit(onInputId) {
    var minPriceInput = document.getElementById("searchFilterMinPrice");
    var minPrice = parseInt(minPriceInput.value);
    var maxPriceInput = document.getElementById("searchFilterMaxPrice");
    var maxPrice = parseInt(maxPriceInput.value);
    minPrice = minPrice < 0 ? 0 : minPrice;
    minPrice = minPrice > 9999 ? 9999 : minPrice;
    maxPrice = maxPrice < 0 ? 0 : maxPrice;
    maxPrice = maxPrice > 9999 ? 9999 : maxPrice;
    if (minPrice > maxPrice) {
        if (onInputId == 0) {
            maxPrice = minPrice;
        } else {
            minPrice = maxPrice;
        }
    }
    minPriceInput.value = isNaN(minPrice) ? "" : minPrice;
    maxPriceInput.value = isNaN(maxPrice) ? "" : maxPrice;
}
//清空筛选器
function searchFilterClear() {
    for (var j = 0; j < 8; j ++) {
        var option = document.getElementById("filterSeller" + j);
        option.className = option.className.replace("btn-selected", "btn-unselected");
    }
    for (var j = 0; j < 6; j ++) {
        var option = document.getElementById("filterDiscount" + j);
        option.className = option.className.replace("btn-selected", "btn-unselected");
    }
    var minPriceInput = document.getElementById("searchFilterMinPrice");
    minPriceInput.value = "";
    var maxPriceInput = document.getElementById("searchFilterMaxPrice");
    maxPriceInput.value = "";
}
//提交筛选器
function searchFilterConfirm() {
    li = document.getElementById("searchFilterLi");
    li.className = li.className.replace(" open", "");
    $("#searchFilterBtn").attr("aria-expanded","false");
}