/**
 * Created by gdelnegro on 16/07/16.
 */
document.onreadystatechange = function () {
  if (document.readyState === "complete") {
      document.getElementById('id_tag').readOnly = true;
      jQuery(".field-last_tag").children('div').children('p').text("");
      toggleFields();
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
    var text = x.options[x.selectedIndex].text;
    getLastTag(jQuery.trim(text.split("-", 1)));
}

function clearValue(){
    var x = document.getElementById("id_tag")
    x.value="";
}

function getLastTag(translationTag){
    jQuery.ajax({
        url: "/api/last_translation_tag/"+translationTag+"/",
        context: document.body,
        success: function(data){
            var result = data.result;
            if(Object.keys(result).length > 0){
                // '<div class="form-row field-last_tag"> <div> <label>Last tag:</label> <p>TTP038</p> </div> </div>'
                var tag = translationTag+(parseInt(result['last_id'])+1)
                jQuery(".field-last_tag").children('div').children('p').text(result['last_tag']);
                jQuery("#id_tag").val(tag);
                if (result['has_tooltip']){
                    // enable tooltip fields
                    toggleFields();
                }
            }else{
                var tag = translationTag+"1"
                jQuery(".field-last_tag").children('div').children('p').text(" - ");
                jQuery("#id_tag").val(tag);
                //check if has tooltip
                if (checkTooltip()){
                    // enable tooltip fields
                    toggleFields();
                }
            }
        }
    });
}

function checkTooltip(){
    jQuery.ajax({
        url: "/api/translation_type/",
        data: {id: document.getElementById("id_type").value},
        context: document.body,
        success: function (data) {
            var result=data[0];
            return result['has_tooltip']
        }
    });
}

function toggleFields(){
    jQuery(".field-tooltip_tag").toggle();
    jQuery(".field-tooltip_text").toggle();
}

