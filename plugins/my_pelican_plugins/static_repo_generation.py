from pelican import signals
import urllib2
import json
import sys

def get_github_repos(user_id):
    url = "https://api.github.com/users/{}/repos".format(user_id)
    new_repos = []
    try:
        json_text = urllib2.urlopen(url).read()
        repos = json.loads(json_text)
        for repo in repos:
            new_repo = {}
            name =  repo["name"]
            if len(name) > 20:
                name = name[0:20]+"..."
            new_repo["name"] = name
            new_repo["link"] = repo["html_url"]
            new_repo["stars"] = repo["stargazers_count"]
            description = repo["description"]
            if description is not None and len(description) > 150:
                description = description[0:150]+"..."
            new_repo["description"] = description
            new_repo["main_language"] = repo["language"]
            new_repo["type"] = "github"
            try:
                lang_json_text = urllib2.urlopen(repo["languages_url"]).read()
                new_repo["all_languages"] = json.loads(lang_json_text)
            except:
                print >> sys.stderr, "[ERROR] IMPOSSIBLE TO READ LANG INFO FOR GITHUB REPO: %s in %s "%(repo["name"], repo["languages_url"])
            new_repos.append(new_repo);
    except:
        print >> sys.stderr, "[ERROR] IMPOSSIBLE TO READ OR PROCESS GITHUB REPOSITORIES"
    return new_repos

def get_bitbucket_repos(user_id):
    url = "https://api.bitbucket.org/2.0/repositories/{}".format(user_id)
    new_repos = []
    try:
        json_text = urllib2.urlopen(url).read()
        repos = json.loads(json_text)
        for repo in repos["values"]:
            new_repo = {}
            name =  repo["name"]
            if len(name) >20:
                name = name[0:20]+"..."
            new_repo["name"] = name
            new_repo["link"] = repo["links"]["html"]
            description = repo["description"]
            if description is not None and len(description) > 150:
                description = description[0:150]+"..."
            new_repo["description"] = description
            new_repo["main_language"] = repo["language"]
            new_repo["type"] = "bitbucket"
            new_repos.append(new_repo)
    except:
        print >> sys.stderr, "[ERROR] IMPOSSIBLE TO READ OR PROCESS BITBUCKET REPOSITORIES"
    return new_repos

def add_language_stats(stats_object, new_stats):
    if new_stats is not None:
        for lang in new_stats:
            if not lang in stats_object:
                stats_object[lang] = 0
            stats_object[lang] += new_stats[lang]

def process_stats(stats_object):
    sum = 0.0
    for lang in stats_object:
        sum += stats_object[lang]
    if sum != 0.0:
        for lang in stats_object:
            stats_object[lang] /= sum
            stats_object[lang] *= 100
        # Cluster the "other" languages

def get_repo_info(generator):
    all_repos = []
    if generator.settings["REPOS_DO_PROCESS"]:
        try:
            github_repos = get_github_repos(generator.settings["REPOS_GITHUB_USER"]);
            bitbucket_repos = get_bitbucket_repos(generator.settings["REPOS_BITBUCKET_USER"])
            all_repos.extend(github_repos)
            all_repos.extend(bitbucket_repos)
            generator.context["repositories"] = all_repos
        except KeyError:
            generator.context["repositories"] = []
            print >> sys.stderr, "[ERROR] YOU MUST DEFINE THE REPO IDS IN THE SETTINGS FILE IF USING THIS PLUGIN !! "

        try:
            language_stats = {}
            for repo in all_repos:
                if "all_languages" in repo:
                    add_language_stats(language_stats, repo["all_languages"])
            process_stats(language_stats)
            generator.context["language_stats_labels"] = language_stats.keys()
            generator.context["language_stats_values"] = [language_stats[lang] for lang in language_stats.keys()]
        except:
            generator.context["language_stats_labels"] = []
            generator.context["language_stats_values"] = []
            print >> sys.stderr, "[ERROR] IMPOSSIBLE TO PROCESS LANGUAGE STATISTICS "

def register():
    # http://docs.getpelican.com/en/3.6.3/plugins.html
    signals.page_generator_finalized.connect(get_repo_info)

    
