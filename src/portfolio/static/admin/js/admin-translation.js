/**
 * Created by gdelnegro on 16/07/16.
 */
document.onreadystatechange = function () {
  if (document.readyState === "complete") {
      jQuery(".field-last_tag").children('div').children('p').text("");
      if (document.URL.indexOf("add") > -1){
        clearValue();
        document.getElementById("id_type").addEventListener("change", updateTag);
      }
  }
}

function updateTag() {
    clearValue();
    var x = document.getElementById("id_type");
    document.getElementById("id_tag").value = x.value
    getLastTag(x.value);
}

function clearValue(){
    var x = document.getElementById("id_tag")
    x.value=""
}

function getLastTag(translationType){
    jQuery.ajax({
        url: "/api/translation?type="+translationType,
        context: document.body,
        success: function(data){
            if(data.count > 0){
                jQuery(".field-last_tag").children('div').children('p').text(data.results[0]['last_tag']);
            }
        }
    });
}

