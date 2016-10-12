var pruned_repos = new Array();

function process_github_repos(repos){
     // Order by stars
     repos.sort(function(x,y){return x.stargazers_count < y.stargazers_count;});
     
     // Get interesting stuff from each object
     var i;
     var name;
     var promises = new Array();
     for ( i = 0; i < repos.length; i++){
        var repo = repos[i];
        if(!repo.fork){
            var new_repo = {};
            name =  repo["name"];
            if (name.length >20){
                name = name.substring(0,19)+"...";
            }
            new_repo["name"] = name;
            new_repo["link"] = repo["html_url"];
            new_repo["stars"] = repo["stargazers_count"];
            description = repo["description"];
            if(!!description && description.length > 150){
                description = description.substring(0,150)+"...";
            }
            new_repo["description"] = description;
            new_repo["main_language"] = repo["language"];
            new_repo["type"] = "github";
            
            promises.push($.getJSON( repo["languages_url"], function( data ) {
                new_repo["all_languages"] = data;
            }));
            
         	pruned_repos.push(new_repo);
         }
     }
     
     console.log(pruned_repos);
     return promises;
}

function get_repos_from_github(){
    var GITHUB_API_URL = "https://api.github.com/users/victor-gil-sepulveda/repos";
    $.getJSON(GITHUB_API_URL)
    .done(function( data ) {
        var promises = process_github_repos(data);
        
        $.when.apply($, promises).then(function(){
            var source   = $("#repos_template").html();
            var template = Handlebars.compile(source);
            var context = {repos: pruned_repos};
            var html    = template(context);
            $("#contents-page").html(html);
        });
    })
    .fail(function(){console.log("Failed to retrieve Github repositories");});
}

function process_bitbucket_repos(repos){

     // Get interesting stuff from each object
     var i;
     var name;
     for ( i = 0; i < repos["values"].length; i++){
        var repo = repos["values"][i];
        if(!repo.fork){
            var new_repo = {};
            name =  repo["name"];
            if (name.length >20){
                name = name.substring(0,19)+"...";
            }
            new_repo["name"] = name;
            new_repo["link"] = repo["links"]["html"];
            description = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vestibulum sit amet dolor eget auctor. Pellentesque vestibulum, sem ut eleifend iaculis, ex orci egestas dui, a fermentum libero eros vel velit. Proin eros dui, sagittis et maximus a, feugiat vel leo. Suspendisse pretium justo vel leo sed. "//repo["description"];
            if(!!description && description.length > 150){
                description = description.substring(0,150)+"...";
            }
            new_repo["description"] = description;
            new_repo["main_language"] = "fakalang";//repo["language"];
            new_repo["type"] = "bitbucket";
         	pruned_repos.push(new_repo);
         }
     }
     
     console.log(pruned_repos);
}

function get_repos_from_bitbucket(){
    var BITBUCKET_API_URL = "https://api.bitbucket.org/2.0/repositories/victor_gil_sepulveda";
    $.getJSON(BITBUCKET_API_URL)
    .done(function( data ) {
        process_bitbucket_repos(data);
        var source   = $("#repos_template").html();
        var template = Handlebars.compile(source);
        var context = {repos: pruned_repos};
        var html    = template(context);
        $("#contents-page").append(html);
    })
    .fail(function(){console.log("Failed to retrieve Bitbucket repositories");});
}

$(document).ready(function(){
    console.log("ok");
    get_repos_from_github();
    get_repos_from_bitbucket();
});
