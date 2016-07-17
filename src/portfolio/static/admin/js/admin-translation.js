/**
 * Created by gdelnegro on 16/07/16.
 */
document.onreadystatechange = function () {
  if (document.readyState === "complete") {
      if (document.URL.indexOf("add") > -1){
        clearValue()
        document.getElementById("id_type").addEventListener("change", updateTag);
        updateTag()
      }
  }
}

function updateTag() {
    clearValue();
    var x = document.getElementById("id_type");
    document.getElementById("id_tag").value = x.value
}

function clearValue(){
    var x = document.getElementById("id_tag")
    x.value=""
}

