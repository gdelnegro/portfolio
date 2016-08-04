/**
 * Created by gdelnegro on 16/07/16.
 */
document.onreadystatechange = function () {
  if (document.readyState === "complete") {
      document.getElementById('id_tag').readOnly = true;
      document.getElementById('id_auxiliary_tag').readOnly = true;
      jQuery(".field-last_tag").children('div').children('p').text("");
      if (document.URL.indexOf("add") > -1){
          toggleFields();
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
    document.getElementById("id_auxiliary_tag").value="";
    jQuery('[id*=" field-auxiliary_text_"]').val("");
}

function getLastTag(translationTag){
    jQuery.ajax({
        url: "/api/last_translation_tag/"+translationTag+"/",
        context: document.body,
        success: function(data){
            var result = data.result;
            if(Object.keys(result).length > 0){
                var tag = translationTag+(parseInt(result['last_id'])+1)
                jQuery(".field-last_tag").children('div').children('p').text(result['last_tag']);
                jQuery("#id_tag").val(tag);
                if (result['has_auxiliary_text']){
                    if (jQuery(".field-auxiliary_tag").css("display") != "block"){
                        toggleFields();
                    }
                    jQuery("#id_auxiliary_tag").val(result['auxiliary_tag']+(parseInt(result['last_id'])+1))
                }
            }else{
                var tag = translationTag+"1"
                jQuery(".field-last_tag").children('div').children('p').text(" - ");
                jQuery("#id_tag").val(tag);
                //check if has tooltip
                var translationTypeDetails = getTranslationTypeDetails();
                console.log(translationTypeDetails)
                if (translationTypeDetails[0]){
                    // enable tooltip fields
                    if (jQuery(".field-auxiliary_tag").css("display") != "block"){
                        toggleFields();
                    }
                    jQuery("#id_auxiliary_tag").val(translationTypeDetails[1]+"1")
                }else{
                    if (jQuery(".field-auxiliary_tag").css("display") == "block"){
                        toggleFields();
                    }
                }
            }
        }
    });
}

function getTranslationTypeDetails(){
    var flag = false;
    var auxiliary_tag = null;
    jQuery.ajax({
        url: "/api/translation_type/",
        data: {id: document.getElementById("id_type").value},
        context: document.body,
        async: false,
        success: function (data) {
            flag = data[0]['has_auxiliary_text'];
            if (flag){
                auxiliary_tag = data[0]['auxiliary_tag'];
            }
        }
    });
    return [flag, auxiliary_tag];
}

function toggleFields(){
    clearValue();
    jQuery(".field-auxiliary_tag").toggle();
    jQuery('[class*=" field-auxiliary_text_"]').parents(".ui-tabs").toggle();
}

