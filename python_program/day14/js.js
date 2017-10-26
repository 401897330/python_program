/**
 * Created by Administrator on 2017/8/1.
 */
// 遮罩层窗口
var ele=document.getElementById("add");
ele.onclick=function () {
    var ele_fade=document.getElementsByClassName("fade")[0];
    var ele_model=document.getElementsByClassName("model")[0];
    ele_fade.classList.remove("hide");
    ele_model.classList.remove("hide");
};

// 表格删除按钮
var ele_f=document.getElementById("tab");
var ele_del = document.getElementsByClassName("del");
for (var i=0;i<ele_del.length;i++) {
    ele_del[i].onclick=function () {
        var index=this.parentNode.parentNode.rowIndex;
        ele_f.deleteRow(index);
    }
};

// 遮罩层取消按钮
var ele_cancle=document.getElementById("cancle");
ele_cancle.onclick=function () {
    this.parentElement.parentElement.classList.add("hide");
    this.parentElement.parentElement.previousElementSibling.classList.add("hide");
};

//表格增加按钮
var ele_confirm=document.getElementById("confirm");
var ele_f=document.getElementById("tab");
ele_confirm.onclick=function () {
    this.parentElement.parentElement.classList.add("hide");
    this.parentElement.parentElement.previousElementSibling.classList.add("hide");
    var name=document.getElementById("name").value;
    var age=document.getElementById("age").value;
    var cls=document.getElementById("cls").value;

    var tr=document.createElement("tr");
    var enter=new Array();
    enter[0]=document.createTextNode(name);
    enter[1]=document.createTextNode(age);
    enter[2]=document.createTextNode(cls);

    enter[3]=document.createElement("input");
    enter[3].type="button";
    enter[3].value="删除";
    enter[3].className="del";

    enter[4]=document.createElement("input");
    enter[4].type="button";
    enter[4].value="修改";
    enter[4].className="edi";

    for(var i=0;i<enter.length;i++){
        var td=document.createElement("td");
        td.appendChild(enter[i]);
        tr.appendChild(td);
    };
    ele_f.appendChild(tr);
    document.getElementById("name").value="";
    document.getElementById("age").value="";
    document.getElementById("cls").value="";
    var ele_del=document.getElementsByClassName("del");
    for (var i=0;i<ele_del.length;i++) {
        ele_del[i].onclick = function () {
            var index = this.parentNode.parentNode.rowIndex;
            ele_f.deleteRow(index);
        }
    }
    var edi=document.getElementsByClassName("edi");
    for (var i=0;i<edi.length;i++) {
        edi[i].onclick = function () {
            var ele_fade = document.getElementsByClassName("fade")[0];
            var ele_model = document.getElementsByClassName("model")[0];
            ele_fade.classList.remove("hide");
            ele_model.classList.remove("hide");
            var ele_tr = this.parentElement.parentElement;

            var ele_confirm1 = document.getElementById("confirm1");
            ele_confirm1.onclick = function () {
                this.parentElement.parentElement.classList.add("hide");
                this.parentElement.parentElement.previousElementSibling.classList.add("hide");
                var Name = document.getElementById("name").value;
                var Age = document.getElementById("age").value;
                var Cls = document.getElementById("cls").value;

                ele_tr.children[0].innerText = Name;
                ele_tr.children[1].innerText = Age;
                ele_tr.children[2].innerText = Cls;
                document.getElementById("name").value="";
                document.getElementById("age").value="";
                document.getElementById("cls").value="";
            }
        }
    }
};

//表格编辑按钮
var edi=document.getElementsByClassName("edi");
for (var i=0;i<edi.length;i++) {
    edi[i].onclick = function () {
        var ele_fade = document.getElementsByClassName("fade")[0];
        var ele_model = document.getElementsByClassName("model")[0];
        ele_fade.classList.remove("hide");
        ele_model.classList.remove("hide");
        var ele_tr = this.parentElement.parentElement;
        var ele_confirm1 = document.getElementById("confirm1");
        ele_confirm1.onclick = function () {
            this.parentElement.parentElement.classList.add("hide");
            this.parentElement.parentElement.previousElementSibling.classList.add("hide");
            var Name = document.getElementById("name").value;
            var Age = document.getElementById("age").value;
            var Cls = document.getElementById("cls").value;

            ele_tr.children[0].innerText = Name;
            ele_tr.children[1].innerText = Age;
            ele_tr.children[2].innerText = Cls;
            document.getElementById("name").value="";
            document.getElementById("age").value="";
            document.getElementById("cls").value="";
         }
    }
}





