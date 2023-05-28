

function getProjects() {
        $.get(window.location.origin + '/list_projects', {}, function(result){
             $("#projectname").empty();
            $.each(result.data, function( index, value ) {
              $('#projectname').append("<option value='" + value + "'>");
            });
          })
   }


function setProjects() {
        let project = $('#project').val()
        $.post(window.location.origin + '/set_project', {'projectname':project}, function(result){
            console.log(result)
          })
   }