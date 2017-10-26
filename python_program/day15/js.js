/**
 * Created by Administrator on 2017/8/1.
 */
// 表格删除按钮
$(".del").click(function () {
    var $p=$(this).parent().parent();
    $p.remove();
});


// 遮罩层取消按钮
$("#cancle").click(function () {
    $(this).parent().parent().addClass("hide").prev().addClass("hide");
});


//表格增加按钮
$("#add").click(function () {
    $(".fade").removeClass("hide");
    $(".model").removeClass("hide");
    $("#confirm").click(function () {
        $(this).parent().parent().addClass("hide").prev().addClass("hide");
        var $new=$("<tr>");
        $new.append($("<td>").append($("#name").val()));
        $new.append($("<td>").append($("#age").val()));
        $new.append($("<td>").append($("#cls").val()));
        $new.append('<td><input type="button" value="删除" class="del"></td>');
        $new.append('<td><input type="button" value="修改" class="edi"></td>');
        $("#tab").append($new);
        $("#name").val("");
        $("#age").val("");
        $("#cls").val("");
        $("#confirm").unbind('click');
    });

    $("#tab").on("click",".del",function () {
        var $p=$(this).parent().parent();
        $p.remove();
    });
    $("#tab").on("click",".edi",function () {
        $(".fade").removeClass("hide");
        $(".model").removeClass("hide");
        var $tds = $(this).parent().prevAll();
        $("#name").val($tds.eq(3).text());
        $("#age").val($tds.eq(2).text());
        $("#cls").val($tds.eq(1).text());
        $("#confirm").click(function () {
            $(this).parent().parent().addClass("hide").prev().addClass("hide");
            $tds.eq(3).replaceWith($("<td>").append($("#name").val()));
            $tds.eq(2).replaceWith($("<td>").append($("#age").val()));
            $tds.eq(1).replaceWith($("<td>").append($("#cls").val()));
            $("#name").val("");
            $("#age").val("");
            $("#cls").val("");
            $("#confirm").unbind('click');
        });
    });
});


//表格编辑按钮
$(".edi").click(function () {
    $(".fade").removeClass("hide");
    $(".model").removeClass("hide");
    var $tds = $(this).parent().prevAll();
    $("#name").val($tds.eq(3).text());
    $("#age").val($tds.eq(2).text());
    $("#cls").val($tds.eq(1).text());
    $("#confirm").click(function () {
        $(this).parent().parent().addClass("hide").prev().addClass("hide");
        $tds.eq(3).replaceWith($("<td>").append($("#name").val()));
        $tds.eq(2).replaceWith($("<td>").append($("#age").val()));
        $tds.eq(1).replaceWith($("<td>").append($("#cls").val()));
        $("#name").val("");
        $("#age").val("");
        $("#cls").val("");
        $("#confirm").unbind('click');
    });
});
