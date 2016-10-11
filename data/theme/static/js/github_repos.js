function get_repos_from_github(){
    var github_api_url = "https://api.github.com/users/victor-gil-sepulveda/repos";
    html_get(github_api_url, process_repo_response);
}

function html_get(url, callback){
    var http_handler = new XMLHttpRequest();
    http_handler.onreadystatechange = function() { 
        if (http_handler.readyState == 4 && http_handler.status == 200)
            callback(http_handler.responseText);
    }
    http_handler.open("GET", url, true);  
    http_handler.send(null);
}

function process_repo_response(response){
    console.log("*")
	console.log(response);
     var repos = JSON.parse(response);
     
     // Order by stars
     repos.sort(function(x,y){return x.stargazers_count > y.stargazers_count;})
     
     // Get interesting stuff from each object
     var pruned_repos = new Array()
     
     var i, repo;
     for ( i = 0; i < repos.length; i++){
        repo = repos[i];
        var new_repo = {};
        new_repo["link"] = repo["html_url"];
        new_repo["stars"] = repo["stargazers_count"];
        new_repo["description"] = repo["description"];
        new_repo["main_language"] = repo["language"];
        html_get(repo["languages_url"], function(resp){
        		console.log(resp);
            	new_repo["all_languages"] = JSON.parse(resp)
            });
     	pruned_repos.push(new_repo);
     }
     
     console.log(pruned_repos);
}
