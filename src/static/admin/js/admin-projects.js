/**
 * Created by gdelnegro on 06/09/16.
 */

document.onreadystatechange = function () {
    if (document.readyState === "complete") {
        getProjectPictures()
    }
};

function getProjectId(){
    return document.URL.substring(document.URL.indexOf("projects/")).replace(/\D/g,'');

}

function getCRFToken() {
    return jQuery("#projects_form").find('input[name=csrfmiddlewaretoken]').val();
}

function uploadImage(input){
    var formData = new FormData();
    formData.append('img_id', jQuery("#upload-form-image-id").val())
    formData.append('model', "project");
    formData.append('pk', getProjectId());
    formData.append("img",input.files[0]);
    formData.append('csrfmiddlewaretoken', getCRFToken());
    jQuery.ajax({
        url: "/upload_image/",
        method: "POST",
        data: formData,
        processData: false,
        contentType: false,
        async:false,
        success: function (data) {
            getProjectPictures();
        },
        error: function (reason) {
            console.log(reason);
        }
    });
}

function updateImage(imgId){
    jQuery("#upload-form-image-id").val(imgId);
    jQuery("#upload-form-image").trigger("click");
}

function deleteImage(imgId){
    if (confirm("Deseja excluir?") == true) {
        jQuery.ajax({
            url: "/delete_image/",
            method: "POST",
            data: {
                img_id: imgId,
                model: "project",
                pk: getProjectId(),
                csrfmiddlewaretoken:getCRFToken()
            },
            async: false,
            success: function (data) {
                getProjectPictures();
            },
            error: function (reason) {
                console.log("error", reason)
            }

        });
        return true;
    }
}

function getProjectPictures(){
    jQuery("#images-grid").remove();
    var html = "<div class='form-row' id='images-grid'>";
    html += "<div>";
    html += "<div>";
    html += "</div>";
    html += "<table>";
    jQuery.ajax({
        url: "/api/project/" + getProjectId(),
        async:false,
        success: function (data){
            var result = data.images;
            if(Object.keys(result).length > 0){
                for(var i=0;i<Object.keys(result).length;i++){
                    if(i == 0 || (i % 3 == 0)){
                        html += "<tr>";
                    }
                    html += '<td>';
                    html += '<div class="image-cell">';
                    html += '<div class="image-toolbar">';
                    html += '<a class="" id="'+result[i].id+'" href="#" title="Del" onclick="updateImage(this.id);return false;">';
                    html += '<img src="/static/admin/img/icon-changelink.svg" alt="Update">';
                    html += '</a>';
                    html += '<a class="" id="'+result[i].id+'" href="#" title="Del" onclick="deleteImage(this.id);return false;">';
                    html += '<img src="/static/admin/img/icon-deletelink.svg" alt="Del">';
                    html += '</a>';
                    html += '</div>';
                    html += '<img src="data:'+result[i].mimetype+';base64,'+result[i].image_string+'" width="200px"/>';
                    html += '</div>';
                    html += '</td>';
                    if(i == Object.keys(result).length -1 || (i % 3 == 2)){
                        html += "</tr>";
                    }
                }
            }
        }
    });
    html += "</table>";
    html += "</div>";
    // form for image upload
    html += "<div id='image-upload-form'>";
    html += "<input type='text' name='image_id' id='upload-form-image-id' class='image-upload-form' style='display: none;'>";
    html += "<input type='file' name='image' id='upload-form-image' onchange='uploadImage(this)' class='image-upload-form'  style='display: none;'>";
    html += "</div>";
    // form for image upload
    html += "</div>";
    jQuery(html).insertBefore(".submit-row")
}