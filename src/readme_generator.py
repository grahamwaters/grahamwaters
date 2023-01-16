import random
from tqdm import tqdm
import os
import random

import requests



def collect_badges_fromdir(directory="./data/prompts/specific_topics"):
    # Create dynamic badges for middle section
    badges = []
    badge_texts = []
    badge_count = len(os.listdir(directory))
    for i in tqdm(range(badge_count)):
        badge_color = random.choice(
            [
                "brightgreen",
                "green",
                "yellowgreen",
                "darkred",
                "lightblue",
                "darkgreen",
                "purple",
                "yellow",
                "orange",
                "red",
                "blue",
                "lightgrey",
                "success",
                "important",
                "critical",
                "informational",
                "inactive",
                "blueviolet",
                "ff69b4",
                "9cf",
            ]
        )
        # get the name of the file
        badge_filename = os.listdir(directory)[i]  # get the name of the file
        badge_text = badge_filename.replace(".md", "")  # remove the .md extension
        badge_text_two = badge_text.replace(" ", "_")  # replace spaces with underscores
        badge_link = f"./{directory}/{badge_text_two}.md"
        while " " in badge_text:
            badge_text = badge_text.replace(" ", "_")
        if badge_text not in badge_texts:
            badge = f"[![{badge_text}](https://img.shields.io/badge/{badge_text}-{badge_color})]({badge_link})"
            badges.append(badge)  # add the badge to the list
        badge_texts.append(
            badge_text.replace("_", " ")
        )  # add the badge text to the list
    # concatenate the badges together then return the concatenated string
    # badges = "\n".join(badges)
    return badges

def get_repos(username, type, per_page):
    url = f'https://api.github.com/users/{username}/{type}?per_page={per_page}'
    repos = requests.get(url).json()
    return repos

def collect_badges(username):
    badges = []
    badge_texts = []
    repos = get_repos(username=username, type="repos", per_page=500)
    repos_I_star = get_repos(username=username, type="starred", per_page=500)
    repos.extend(repos_I_star)
    repos_I_watch = get_repos(username=username, type="watched", per_page=500)
    repos.extend(repos_I_watch)
    repos_I_follow = get_repos(username=username, type="following", per_page=5000)
    repos.extend(repos_I_follow)
    repos_I_forked = get_repos(username=username, type="forks", per_page=500)
    repos.extend(repos_I_forked)
    # remove duplicates
    repos = [repo for repo in repos if repo not in repos[:repos.index(repo)]
    ]
    badge_count = len(repos)
    for i in tqdm(range(badge_count)):
        badge_color = random.choice(
            [
                "brightgreen",
                "green",
                "darkred",
                "lightblue",
                "darkgreen",
                "purple",
                "orange",
                "red",
                "blue",
                "lightgrey",
                "success",
                "important",
                "critical",
                "informational",
                "inactive",
                "blueviolet",
                "ff69b4",
                "9cf",
            ]
        )
        repo = repos[i]
        try:
            badge_text = repo['name']
        except KeyError:
            badge_text = repo['login'] # if the repo is a user then use the login name
        except TypeError: # if the repo is None then skip it
            continue
        except Exception as e:
            print(e)
            continue
        badge_link = repo['html_url']
        while " " in badge_text:
            badge_text = badge_text.replace(" ", "_")
        if badge_text not in badge_texts:
            badge = f"[![{badge_text}](https://img.shields.io/badge/{badge_text}-{badge_color})]({badge_link})"
            badges.append(badge)  # add the badge to the list
        badge_texts.append(
            badge_text.replace("_", " ")
        )  # add the badge text to the list
    return badges



def collect_badges_from_dirs(dirs_list):
    # go to each directory and collect the badges
    badges = []
    for directory in dirs_list:
        new_badges_list = collect_badges(directory=directory)
        updated_badges = [
            badge for badge in new_badges_list if badge not in badges
        ]  # remove duplicates
        badges.extend(updated_badges)
    # join the badges together and return the string
    badges = "\n ".join(badges)
    return badges

def master_badge_function():
    badges = collect_badges(username="grahamwaters")
    keepers = [] # list to hold the badges that will be kept
    # if any badges have spaces then replace those spaces with "%20"
    for i in range(len(badges)):
        if " " in badges[i]:
            badges[i] = badges[i].replace(" ", "%20")
        # replace all but the final dash with "%2D"
        # badges[i] = badges[i].replace("-", "%2D", badges[i].count("-") - 1)
        # skip if there is a dash in the badge text
        # if more than one dash then dont add to keepers
        if badges[i].count("-") == 1:
            keepers.append(badges[i])
        else:
            print(badges[i])
    # the badges need to be joined together
    badges = " ".join(keepers) # join the badges together
    return badges

def master_badge_function_dirs():
    badges = collect_badges_from_dirs(
        dirs_list=["./data/prompts/specific_topics"]
    )  # can add user_defined_topics later

    return badges


# Read in the top, middle, and bottom sections of the README
with open("./docs/top.md", "r") as file:
    top = file.read()
    # Write the section to the top of the readme
    with open("README.md", "w") as file:
        file.write(top)


with open("./docs/bottom.md", "r") as file:
    bottom = file.read()
    # add a new line to the bottom
    bottom += "\n"
    # write the section to the bottom of the readme
    with open("README.md", "a") as file:
        # add a new line to the bottom
        bottom += "\n\n"
        file.write(bottom)

with open("./docs/middle.md", "r") as file:
    # middle = file.read()
    updated_middle = master_badge_function()  # collect the badges
    # Convert to HTML
    #!middle = mistune.markdown(updated_middle)
    middle = "\n<div align='center'>\n\n My Wall of Things I Love\n\n " + updated_middle + "\n</div>\n\n"
    # write the section to the bottom of the readme
    with open("README.md", "a") as file:
        file.write(middle)