/**
 * Created by gdelnegro on 06/09/16.
 */

id = "field-images"
id = "submit-row"
// todo: get all images from project, and build a gallery
// todo: add CRUD methods to pictures

document.onreadystatechange = function () {
    if (document.readyState === "complete") {
        getProjectPictures()
    }
}

function getProjectPictures(){
    var html = "<div class='form-row' id='images-grid'>";
    html += "<div>";
    html += "<div>";
    html += "</div>";
    html += "<table>";
    jQuery.ajax({
        url: "/api/project/1",
        async:false,
        success: function (data){
            var result = data.images;
            if(Object.keys(result).length > 0){
                for(var i=0;i<Object.keys(result).length;i++){
                    if(i == 0){
                        html += "<tr>";
                    }
                    html += '<td>';
                    html += '<div class="image-cell">';
                    html += '<div class="image-toolbar">';
                    html += '<a class="related-widget-wrapper-link add-related" id="" href="#" title="Add">';
                    html += '<img src="/static/admin/img/icon-addlink.svg" alt="Add">';
                    html += '</a>';
                    html += '<a class="related-widget-wrapper-link add-related" id="" href="#" title="Add">';
                    html += '<img src="/static/admin/img/icon-changelink.svg" alt="Add">';
                    html += '</a>';
                    html += '</div>';
                    html += '<img src="data:'+result[i].mimetype+';base64,'+result[i].image_string+'" width="200px"/>';
                    html += '</div>';
                    html += '<td>';
                    if(i == Object.keys(result).length -1){
                        html += "</tr>";
                    }
                    // jQuery(html_).insertBefore(".submit-row")
                }
            }
        }
    });
    html += "</table>";
    html += "</div>";
    html += "</div>";
    jQuery(html).insertBefore(".submit-row")
}