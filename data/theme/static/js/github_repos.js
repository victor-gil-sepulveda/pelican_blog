var pruned_repos = new Array();

function get_repos_from_github(){
    var github_api_url = "https://api.github.com/users/victor-gil-sepulveda/repos";
    return html_get(github_api_url, process_repo_response);
}

function html_get(url, callback){
    var http_handler = new XMLHttpRequest();
    http_handler.onreadystatechange = function(){ 
        if (http_handler.readyState == 4 && http_handler.status == 200){
            callback(http_handler.responseText);
        }
    };
    http_handler.open("GET", url, true);  
    http_handler.send(null);
}

function html_get_languages(url, repo, deferred){
    var http_handler = new XMLHttpRequest();
    http_handler.onreadystatechange = function() { 
        if (http_handler.readyState == 4 && http_handler.status == 200){
            try{
                repo["all_languages"] = JSON.parse(http_handler.responseText);
                deferred.resolve();
            }
            catch(e){
                deferred.reject();
            }
        }
        else{
            deferred.reject();
        }
    };
    http_handler.open("GET", url, true);  
    http_handler.send(null);
}

function process_repo_response(response){
     var repos = JSON.parse(response);
     
     // Order by stars
     repos.sort(function(x,y){return x.stargazers_count > y.stargazers_count;});
     
     // Get interesting stuff from each object
     var i;
     var promises = new Array();
     for ( i = 0; i < repos.length; i++){
        var repo = repos[i];
        var new_repo = {};
        new_repo["name"] = repo["name"];
        new_repo["link"] = repo["html_url"];
        new_repo["stars"] = repo["stargazers_count"];
        new_repo["description"] = repo["description"];
        new_repo["main_language"] = repo["language"];
        var deferred = $.Deferred();
        html_get_languages(repo["languages_url"], new_repo, deferred);
        promises.push(deferred.promise());
     	pruned_repos.push(new_repo);
     }
     
     console.log(pruned_repos);
     
     return promises;
}

$(document).ready(function(){
    $.when.apply(null,get_repos_from_github()).then(function(){
        var source   = $("#repos_template").html();
        var template = Handlebars.compile(source);
        console.log(pruned_repos);
        var context = {repos: pruned_repos};
        var html    = template(context);
        $("#contents-page").html(html);
    });
});
